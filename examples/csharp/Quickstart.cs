// Dona API quickstart — the portal's "Boshlash" steps 2–4, in C#.
//
// 1. GET /me                   who the key is: shop, tier, limits
// 2. GET /products?limit=5     the first page of the catalogue
// 3. POST /stock?dry_run=true  re-sends the first product's CURRENT stock as a rehearsal: validated,
//                              guarded and rolled back — nothing is written, whatever the answer.
//
// Optional: DONA_API_BASE_URL (defaults to production, the only environment).
using System.Text.Json;
using Dona.Api.Api;
using Dona.Api.Client;
using Dona.Api.Extensions;
using Dona.Api.Model;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

namespace DonaExamples;

public static class Quickstart
{
    public const string BaseUrl = "https://api.dona.im/seller-api/v1";
    private const string Integration = "dona-api-examples/csharp";

    public static async Task<int> RunAsync()
    {
        var apiKey = Environment.GetEnvironmentVariable("DONA_API_KEY");
        if (string.IsNullOrEmpty(apiKey))
        {
            Console.Error.WriteLine("Set DONA_API_KEY (dona_sk_live_…) — the shop owner mints it in Sozlamalar › API.");
            return 2;
        }
        var baseUrl = Environment.GetEnvironmentVariable("DONA_API_BASE_URL") ?? BaseUrl;

        using var host = Host.CreateDefaultBuilder()
            .ConfigureLogging(l => l.SetMinimumLevel(LogLevel.Warning))
            .ConfigureApi((_, options) =>
            {
                options.AddTokens(new BearerToken(apiKey)); // Authorization: Bearer <key>
                options.AddApiHttpClients(client =>
                {
                    client.BaseAddress = new Uri(baseUrl);
                    client.Timeout = TimeSpan.FromSeconds(30);
                });
            })
            .Build();

        // 1 ─ who am I
        var me = await host.Services.GetRequiredService<IAccountApi>().GetMeAsync(xDonaIntegration: Integration);
        if (!me.TryOk(out var meBody)) return Fail("GET /me", me);
        Console.WriteLine($"shop: {meBody.Shop.Name} ({meBody.Shop.Status}) · tier {meBody.Tier} · writes_enabled {(meBody.WritesEnabled ? "true" : "false")}");
        Console.WriteLine($"rate limit: {Header(me, "X-RateLimit-Remaining")}/{Header(me, "X-RateLimit-Limit")} left · policy {Header(me, "RateLimit-Policy")}");

        // 2 ─ first five products
        var page = await host.Services.GetRequiredService<ICatalogApi>().ListProductsAsync(limit: 5, xDonaIntegration: Integration);
        if (!page.TryOk(out var pageBody)) return Fail("GET /products", page);
        foreach (var p in pageBody.Items)
            Console.WriteLine($"  {p.Id}  {p.SellerSku ?? "-"}  stock {p.Stock}  {p.Title.Uz ?? p.Title.Ru}");

        // 3 ─ rehearse a stock write
        var first = pageBody.Items.FirstOrDefault();
        if (first is null)
        {
            Console.WriteLine("no products yet — skipping the POST /stock rehearsal");
            return 0;
        }
        var variant = first.Variants.FirstOrDefault();
        var line = variant is null
            ? new StockLine(first.Stock, productId: new Option<Guid?>(first.Id))
            : new StockLine(variant.Stock, productId: new Option<Guid?>(first.Id), variantId: new Option<Guid?>(variant.Id));

        var stock = await host.Services.GetRequiredService<IStockPricesApi>().SetStockAsync(
            // One key per logical write. Re-send the SAME key on a retry: the answer is replayed for 24 h.
            idempotencyKey: Guid.NewGuid().ToString(),
            stockRequest: new StockRequest([line]),
            dryRun: true,
            xDonaIntegration: Integration);
        if (stock.TryAccepted(out var held))
            Console.WriteLine($"POST /stock held for review: rule {held.Rule} · approval {held.ApprovalId} — nothing was written");
        else if (stock.TryOk(out var result))
            Console.WriteLine($"POST /stock dry_run={(result.DryRun ? "true" : "false")}: ok {result.Summary.Ok} · error {result.Summary.Error} · held {result.Summary.Held}");
        else
            return Fail("POST /stock", stock);
        return 0;
    }

    private static string Header(IApiResponse r, string name) =>
        r.Headers.TryGetValues(name, out var v) ? string.Join(",", v) : "?";

    /// Prints the error envelope. Branch on `error` (a stable code), never on `message` (localised).
    private static int Fail(string step, IApiResponse r)
    {
        string code = "", message = r.RawContent;
        try
        {
            using var doc = JsonDocument.Parse(r.RawContent);
            code = doc.RootElement.TryGetProperty("error", out var e) ? e.GetString() ?? "" : "";
            message = doc.RootElement.TryGetProperty("message", out var m) ? m.GetString() ?? "" : message;
        }
        catch (JsonException) { }
        Console.Error.WriteLine($"{step} → HTTP {(int)r.StatusCode} {code}: {message}");
        if (r.Headers.RetryAfter is { } ra)
            Console.Error.WriteLine($"  retry after {ra.Delta?.TotalSeconds}s ({Header(r, "Dona-Rate-Limited-Reason")})");
        return 1;
    }
}
