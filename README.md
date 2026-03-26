# castbrick

Official Python SDK for the [CastBrick](https://castbrick.com) API — send SMS, manage contacts and run broadcasts.

Zero dependencies. Works with Python 3.8+.

## Installation

```bash
pip install castbrick
```

## Quick start

```python
import os
from castbrick import CastBrick

cb = CastBrick(api_key=os.environ["CASTBRICK_API_KEY"])

result = cb.sms.send(
    to=["+244923000000"],
    content="Hello from CastBrick!",
)
print(result.message_id, result.status)
```

## SMS

```python
# Send
result = cb.sms.send(
    to=["+244923000000", "+244912000000"],
    content="Your OTP is 1234",
    sender_id="MyApp",                          # optional
    scheduled_at="2026-11-28T09:00:00Z",        # optional
)

# Get
msg = cb.sms.get("message-id")
print(msg.status)

# List
page = cb.sms.list(page=1, page_size=20)
print(page.total_count)

# Cancel scheduled
cb.sms.cancel_scheduled("message-id")
```

## Contacts

```python
# List (with optional search)
page = cb.contacts.list(search="joão")

# Get
contact = cb.contacts.get("contact-id")

# Create (comma-separated phone numbers or emails)
cb.contacts.create(phone_numbers="+244923000000,+244912000000")
cb.contacts.create(emails="alice@example.com")

# Delete
cb.contacts.delete("contact-id")

# Contact lists
lst = cb.contacts.create_list("VIP Customers")
cb.contacts.add_to_list(lst.id, contact.id)
cb.contacts.remove_from_list(lst.id, contact.id)
```

## Broadcasts

```python
# Create
id = cb.broadcasts.create(
    name="Black Friday",
    message="50% off everything today!",
    contact_list_id="list-id",  # optional
    sender_id="MyApp",          # optional
)

# Send immediately
cb.broadcasts.send(id)

# Update with schedule
cb.broadcasts.update(
    id,
    name="Black Friday",
    message="50% off everything today!",
    schedule_at="2026-11-28T09:00:00Z",
)

# Other operations
cb.broadcasts.cancel(id)
new_id = cb.broadcasts.duplicate(id)
cb.broadcasts.delete(id)
```

## Error handling

```python
from castbrick import CastBrickApiError

try:
    cb.sms.send(to=["+244923000000"], content="Hello!")
except CastBrickApiError as e:
    print(f"{e.status_code}: {e.body}")
    # 401 → invalid or revoked API key
    # 402 → insufficient credits
    # 422 → validation error
```

## Publishing

```bash
pip install build twine
python -m build
twine upload dist/*
```

## License

MIT
