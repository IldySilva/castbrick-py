# castbrick

Official Python SDK for the [CastBrick](https://castbrick.co) API — send SMS, manage contacts and run broadcasts.

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
    sender_id="MyApp",                    # optional — your approved Sender ID
    scheduled_at="2026-11-28T09:00:00Z",  # optional — schedule for later
    fallback=True,                        # optional — fall back to CastBrick sender if senderId unavailable
)

# List (with optional filters)
page = cb.sms.list(
    page=1,
    page_size=20,
    status="delivered",           # pending | sent | delivered | failed | scheduled
    phone="+244923000000",
    from_date="2026-01-01T00:00:00Z",
    to_date="2026-06-01T00:00:00Z",
)
print(page.total_count)

# Cancel a scheduled SMS
cb.sms.cancel_scheduled("message-id")
```

## Contacts

```python
# List (with optional search)
page = cb.contacts.list(search="joão")

# Get
contact = cb.contacts.get("contact-id")

# Create — comma or newline-separated phone numbers
cb.contacts.create(phone_numbers="+244923000000\n+244912000000")

# Delete
cb.contacts.delete("contact-id")

# Contact lists
list_id = cb.contacts.create_list("VIP Customers")  # returns the new list ID (str)
cb.contacts.add_to_list(list_id, contact.id)
cb.contacts.remove_from_list(list_id, contact.id)
```

## Broadcasts

```python
# Create
broadcast_id = cb.broadcasts.create(
    name="Black Friday",
    message="50% off everything today!",
    contact_list_id="list-id",  # optional
    sender_id="MyApp",          # optional
)

# Send immediately
cb.broadcasts.send(broadcast_id)

# Update with schedule
cb.broadcasts.update(
    broadcast_id,
    name="Black Friday",
    message="50% off everything today!",
    schedule_at="2026-11-28T09:00:00Z",
)

# Other operations
cb.broadcasts.cancel(broadcast_id)
new_id = cb.broadcasts.duplicate(broadcast_id)
cb.broadcasts.delete(broadcast_id)
```

## Billing

```python
# Get current credit balance
balance = cb.billing.get_balance()

# List available credit packages
packages = cb.billing.list_packages()

# List credit consumption/transaction history
history = cb.billing.list_transactions()
```

## Segments, Templates & Webhooks

The SDK also provides native access to `cb.segments`, `cb.templates`, and `cb.webhooks`.

```python
# Example: Create a Webhook
cb.webhooks.create(
    url="https://yourapp.com/webhooks/castbrick",
    events=["sms.delivered", "sms.failed"]
)
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

## License

MIT
