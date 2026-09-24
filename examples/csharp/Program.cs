// Dona API examples (C#).
//
//   DONA_API_KEY=dona_sk_live_… dotnet run -- quickstart
//   dotnet run -- webhook-selftest
using DonaExamples;

return args.FirstOrDefault() switch
{
    "quickstart" => await Quickstart.RunAsync(),
    "webhook-selftest" => WebhookSelfTest.Run(),
    _ => Usage(),
};

static int Usage()
{
    Console.Error.WriteLine("usage: dotnet run -- quickstart | webhook-selftest");
    return 2;
}
