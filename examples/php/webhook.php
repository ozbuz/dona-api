<?php
// Dona webhook signature verification (Standard Webhooks) — no dependencies.
//
// Headers on every delivery: webhook-id · webhook-timestamp · webhook-signature.
//   signature = space-delimited "v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id.ts.rawBody)>"
//   (two entries for 24 h after a secret rotation — accept if ANY matches)
//
// ⚠ Verify the RAW request bytes: file_get_contents('php://input'), never json_encode(json_decode(...)).
//   Then dedupe on webhook-id (the event id) for 24 h.
//
//   $raw = file_get_contents('php://input');
//   try {
//       dona_verify_webhook(getenv('DONA_WEBHOOK_SECRET'), [
//           'webhook-id' => $_SERVER['HTTP_WEBHOOK_ID'] ?? '',
//           'webhook-timestamp' => $_SERVER['HTTP_WEBHOOK_TIMESTAMP'] ?? '',
//           'webhook-signature' => $_SERVER['HTTP_WEBHOOK_SIGNATURE'] ?? '',
//       ], $raw);
//   } catch (DonaWebhookVerificationError) { http_response_code(401); exit; }
//   http_response_code(204); // acknowledge fast; process asynchronously
declare(strict_types=1);

const DONA_WEBHOOK_TOLERANCE_SECONDS = 300;

final class DonaWebhookVerificationError extends RuntimeException {}

/**
 * @param array<string,string> $headers webhook-id, webhook-timestamp, webhook-signature (lower-case keys)
 * @throws DonaWebhookVerificationError unless the delivery is authentic and fresh
 */
function dona_verify_webhook(string $secret, array $headers, string $rawBody, ?int $now = null): void
{
    $id = $headers['webhook-id'] ?? '';
    $ts = $headers['webhook-timestamp'] ?? '';
    $signatures = $headers['webhook-signature'] ?? '';
    if ($id === '' || $ts === '' || $signatures === '') {
        throw new DonaWebhookVerificationError('missing webhook-* headers');
    }
    if (!ctype_digit($ts)) {
        throw new DonaWebhookVerificationError('bad webhook-timestamp');
    }
    $now ??= time();
    if (abs($now - (int) $ts) > DONA_WEBHOOK_TOLERANCE_SECONDS) {
        throw new DonaWebhookVerificationError('timestamp outside tolerance');
    }
    $key = base64_decode(str_starts_with($secret, 'whsec_') ? substr($secret, 6) : $secret, true);
    if ($key === false) {
        throw new DonaWebhookVerificationError('secret is not base64 after whsec_');
    }
    $expected = base64_encode(hash_hmac('sha256', "{$id}.{$ts}.{$rawBody}", $key, true));
    foreach (explode(' ', $signatures) as $entry) {
        [$version, $sig] = array_pad(explode(',', $entry, 2), 2, '');
        if ($version === 'v1' && $sig !== '' && hash_equals($expected, $sig)) {
            return;
        }
    }
    throw new DonaWebhookVerificationError('no matching signature');
}
