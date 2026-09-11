# castbrick-pypi

Official Python SDK for the CastBrick API. Published as `castbrick` on PyPI. Zero dependencies — stdlib only.

## Commands

```bash
python -m build          # build sdist + wheel into dist/
twine upload dist/*      # manual publish (first time only)
pip install -e .         # install locally for testing
```

## Version

Current: `0.2.0` — bump in `pyproject.toml` before releasing.

## Source files

```
castbrick/
├── __init__.py     # CastBrick class + _DEFAULT_BASE_URL
├── _client.py      # _Client (urllib, no dependencies)
├── _models.py      # Dataclasses for all types
├── _sms.py         # SmsResource
├── _contacts.py    # ContactsResource
├── _broadcasts.py  # BroadcastsResource
├── _billing.py     # BillingResource
├── _segments.py    # SegmentsResource
├── _templates.py   # TemplatesResource
└── _webhooks.py    # WebhooksResource
```

## API base URL

`_DEFAULT_BASE_URL = "https://api.castbrick.co"` — **no `/v1`**.

## Correct API facts

- `sms.cancel_scheduled(message_id)` → `DELETE /sms/{id}`
- `contacts.create_list(name)` → returns `str` (ID), not `ContactList`
- `contacts.create(phone_numbers=...)` — no `emails` param
- `sms.list(status=, phone=, from_date=, to_date=, page=, page_size=)` — all optional filters
- `sms.send(..., fallback=True)` — fallback param supported
- `_Client.get(path, params=None)` — params dict is URL-encoded properly

## Publishing

Tag `v0.1.x` on `main` triggers GitHub Actions → publishes to PyPI via trusted publishing (OIDC).
First publish must be done manually with `twine upload dist/*` since the package didn't exist on PyPI.

## Build system

`pyproject.toml` uses `setuptools.build_meta` (not `setuptools.backends.legacy:build`).
License is `license = "MIT"` (SPDX string, not table format).
