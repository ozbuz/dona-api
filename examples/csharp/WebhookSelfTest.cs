// Runs the shared vectors (examples/testdata/webhook-vectors.json) through DonaWebhook.Verify.
using System.Text;
using System.Text.Json;

namespace DonaExamples;

public static class WebhookSelfTest
{
    public static int Run()
    {
        var path = Path.Combine(AppContext.BaseDirectory, "testdata", "webhook-vectors.json");
        using var doc = JsonDocument.Parse(File.ReadAllText(path));
        int total = 0, failed = 0;
        foreach (var c in doc.RootElement.GetProperty("cases").EnumerateArray())
        {
            total++;
            bool valid = true;
            try
            {
                DonaWebhook.Verify(c.GetProperty("secret").GetString()!, c.GetProperty("id").GetString()!,
                    c.GetProperty("timestamp").GetInt64().ToString(), c.GetProperty("signature").GetString()!,
                    Encoding.UTF8.GetBytes(c.GetProperty("body").GetString()!),
                    DateTimeOffset.FromUnixTimeSeconds(c.GetProperty("now").GetInt64()));
            }
            catch (DonaWebhookVerificationException) { valid = false; }
            if (valid != c.GetProperty("valid").GetBoolean())
            {
                failed++;
                Console.Error.WriteLine($"FAIL {c.GetProperty("name").GetString()}: got valid={valid}");
            }
        }
        Console.WriteLine($"csharp webhook: {total - failed}/{total} vectors");
        return failed == 0 ? 0 : 1;
    }
}
