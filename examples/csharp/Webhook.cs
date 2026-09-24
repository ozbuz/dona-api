// Dona webhook signature verification (Standard Webhooks) — base class library only.
//
// Headers on every delivery: webhook-id · webhook-timestamp · webhook-signature.
//   signature = space-delimited "v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id.ts.rawBody)>"
//   (two entries for 24 h after a secret rotation — accept if ANY matches)
//
// ⚠ Verify the RAW request bytes; re-serialised JSON never matches. Then dedupe on webhook-id for 24 h.
//
//   app.MapPost("/dona/webhooks", async (HttpRequest req) => {
//       using var ms = new MemoryStream(); await req.Body.CopyToAsync(ms);
//       try { DonaWebhook.Verify(secret, req.Headers["webhook-id"]!, req.Headers["webhook-timestamp"]!,
//                                req.Headers["webhook-signature"]!, ms.ToArray()); }
//       catch (DonaWebhookVerificationException) { return Results.Unauthorized(); }
//       return Results.NoContent();   // acknowledge fast; process asynchronously
//   });
using System.Security.Cryptography;
using System.Text;

namespace DonaExamples;

public sealed class DonaWebhookVerificationException(string message) : Exception(message);

public static class DonaWebhook
{
    public static readonly TimeSpan Tolerance = TimeSpan.FromSeconds(300);

    /// Throws DonaWebhookVerificationException unless the delivery is authentic and fresh.
    public static void Verify(string secret, string id, string timestamp, string signatures, byte[] rawBody, DateTimeOffset? now = null)
    {
        if (string.IsNullOrEmpty(id) || string.IsNullOrEmpty(timestamp) || string.IsNullOrEmpty(signatures))
            throw new DonaWebhookVerificationException("missing webhook-* headers");
        if (!long.TryParse(timestamp, out var ts))
            throw new DonaWebhookVerificationException("bad webhook-timestamp");
        var skew = (now ?? DateTimeOffset.UtcNow).ToUnixTimeSeconds() - ts;
        if (Math.Abs(skew) > Tolerance.TotalSeconds)
            throw new DonaWebhookVerificationException("timestamp outside tolerance");

        byte[] key;
        try { key = Convert.FromBase64String(secret.StartsWith("whsec_", StringComparison.Ordinal) ? secret[6..] : secret); }
        catch (FormatException) { throw new DonaWebhookVerificationException("secret is not base64 after whsec_"); }

        byte[] message = [.. Encoding.UTF8.GetBytes($"{id}.{timestamp}."), .. rawBody];
        var expected = HMACSHA256.HashData(key, message);
        foreach (var entry in signatures.Split(' '))
        {
            var comma = entry.IndexOf(',');
            if (comma < 0 || entry[..comma] != "v1") continue;
            byte[] got;
            try { got = Convert.FromBase64String(entry[(comma + 1)..]); }
            catch (FormatException) { continue; }
            if (CryptographicOperations.FixedTimeEquals(got, expected)) return;
        }
        throw new DonaWebhookVerificationException("no matching signature");
    }
}
