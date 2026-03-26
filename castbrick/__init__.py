"""Official Python SDK for the CastBrick API."""

from ._client import CastBrickApiError
from ._models import (
    Broadcast,
    Contact,
    ContactList,
    PagedResult,
    SendSmsResponse,
    SmsMessage,
)
from ._sms import SmsResource
from ._contacts import ContactsResource
from ._broadcasts import BroadcastsResource
from ._client import _Client

__all__ = [
    "CastBrick",
    "CastBrickApiError",
    "Broadcast",
    "Contact",
    "ContactList",
    "PagedResult",
    "SendSmsResponse",
    "SmsMessage",
]

_DEFAULT_BASE_URL = "https://api.castbrick.co/v1"


class CastBrick:
    """Main CastBrick SDK client.

    Usage::

        cb = CastBrick(api_key="your_api_key")
        cb.sms.send(to=["+244923000000"], content="Hello!")
    """

    def __init__(self, *, api_key: str, base_url: str = _DEFAULT_BASE_URL) -> None:
        client = _Client(api_key, base_url)
        self.sms = SmsResource(client)
        self.contacts = ContactsResource(client)
        self.broadcasts = BroadcastsResource(client)
