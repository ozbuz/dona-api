<?php
// Runs the shared vectors (examples/testdata/webhook-vectors.json) through dona_verify_webhook.
declare(strict_types=1);

require __DIR__ . '/webhook.php';

$vectors = json_decode(file_get_contents(__DIR__ . '/../testdata/webhook-vectors.json'), true, flags: JSON_THROW_ON_ERROR);
$failed = 0;
foreach ($vectors['cases'] as $c) {
    $headers = ['webhook-id' => $c['id'], 'webhook-timestamp' => (string) $c['timestamp'], 'webhook-signature' => $c['signature']];
    try {
        dona_verify_webhook($c['secret'], $headers, $c['body'], $c['now']);
        $valid = true;
    } catch (DonaWebhookVerificationError) {
        $valid = false;
    }
    if ($valid !== $c['valid']) {
        $failed++;
        fwrite(STDERR, sprintf("FAIL %s: got valid=%s, want %s\n", $c['name'], var_export($valid, true), var_export($c['valid'], true)));
    }
}
printf("php webhook: %d/%d vectors\n", count($vectors['cases']) - $failed, count($vectors['cases']));
exit($failed ? 1 : 0);
