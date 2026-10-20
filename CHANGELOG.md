# Changelog

## 0.2.4 — 2026-10-20

### Bug Fixes
- Added `User-Agent: castbrick-python/0.2.4` header to prevent Cloudflare WAF Error 1010 from blocking default `Python-urllib` signatures.
- Fixed missing module files (`_billing.py`, `_segments.py`, `_templates.py`, `_webhooks.py`) in published PyPI package caused by `.gitignore` wildcard.
- Added `from __future__ import annotations` and fixed `list` method shadowing for Python 3.8-3.14 compatibility.

## 0.2.0 — 2026-07-18

### New Features
- Added support for `Billing` API (`castbrick.billing`)
- Added support for `Segments` API (`castbrick.segments`)
- Added support for `Templates` API (`castbrick.templates`)
- Added support for `Webhooks` API (`castbrick.webhooks`)

---

## 0.1.3 — 2026-06-01

### Bug Fixes
- **`sms.cancel_scheduled()`** — fixed endpoint from `POST /sms/cancel-scheduled` to `DELETE /sms/{id}` (was completely broken)
- **`contacts.create_list()`** — now correctly returns `str` (the new list ID) instead of trying to deserialize a `ContactList` object
- **`contacts.create()`** — removed unsupported `emails` parameter; API only accepts `phone_numbers`
- **`CastBrick` default `base_url`** — corrected to `https://api.castbrick.co` (was incorrectly including `/v1` path prefix causing all requests to 404)

### New Features
- **`sms.send()`** — added `fallback: bool | None` parameter to control sender ID fallback behaviour
- **`sms.list()`** — added `status`, `phone`, `from_date` and `to_date` filter parameters
- **`_Client.get()`** — now accepts an optional `params: dict` argument, building the query string with proper URL encoding

### Breaking Changes
- `contacts.create(emails=..., phone_numbers=...)` → `contacts.create(phone_numbers=...)`

---

## 0.1.2

- Initial release.
