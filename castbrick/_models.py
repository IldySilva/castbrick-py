from __future__ import annotations
from dataclasses import dataclass, field
from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")


@dataclass
class PagedResult(Generic[T]):
    items: List[T]
    total_count: int
    page_number: int
    total_pages: int
    has_next_page: bool
    has_previous_page: bool

    @classmethod
    def _from_dict(cls, data: dict, item_cls):
        return cls(
            items=[item_cls._from_dict(i) for i in data.get("items", [])],
            total_count=data.get("totalCount", 0),
            page_number=data.get("pageNumber", 1),
            total_pages=data.get("totalPages", 1),
            has_next_page=data.get("hasNextPage", False),
            has_previous_page=data.get("hasPreviousPage", False),
        )


# ── SMS ──────────────────────────────────────────────────────────────────────

@dataclass
class SendSmsResponse:
    message_id: str
    status: str
    recipient_count: int
    timestamp: str
    error: Optional[str] = None

    @classmethod
    def _from_dict(cls, d: dict) -> "SendSmsResponse":
        return cls(
            message_id=d["messageId"],
            status=d["status"],
            recipient_count=d["recipientCount"],
            timestamp=d["timestamp"],
            error=d.get("error"),
        )


@dataclass
class SmsMessage:
    id: str
    recipient_phone: str
    message: str
    status: str
    retry_count: int
    contact_name: Optional[str] = None
    campaign_name: Optional[str] = None
    campaign_id: Optional[str] = None
    sender_id: Optional[str] = None
    error_message: Optional[str] = None
    scheduled_at: Optional[str] = None
    sent_at: Optional[str] = None
    delivered_at: Optional[str] = None

    @classmethod
    def _from_dict(cls, d: dict) -> "SmsMessage":
        return cls(
            id=d["id"],
            recipient_phone=d["recipientPhone"],
            message=d["message"],
            status=d["status"],
            retry_count=d.get("retryCount", 0),
            contact_name=d.get("contactName"),
            campaign_name=d.get("campaignName"),
            campaign_id=d.get("campaignId"),
            sender_id=d.get("senderId"),
            error_message=d.get("errorMessage"),
            scheduled_at=d.get("scheduledAt"),
            sent_at=d.get("sentAt"),
            delivered_at=d.get("deliveredAt"),
        )


# ── Contacts ─────────────────────────────────────────────────────────────────

@dataclass
class Contact:
    id: str
    tenant_id: str
    created_at: str
    name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None

    @classmethod
    def _from_dict(cls, d: dict) -> "Contact":
        return cls(
            id=d["id"],
            tenant_id=d["tenantId"],
            created_at=d["createdAt"],
            name=d.get("name"),
            phone_number=d.get("phoneNumber"),
            email=d.get("email"),
        )


@dataclass
class ContactList:
    id: str
    name: str
    tenant_id: str
    contact_count: int
    created_at: str

    @classmethod
    def _from_dict(cls, d: dict) -> "ContactList":
        return cls(
            id=d["id"],
            name=d["name"],
            tenant_id=d["tenantId"],
            contact_count=d["contactCount"],
            created_at=d["createdAt"],
        )


# ── Broadcasts ───────────────────────────────────────────────────────────────

@dataclass
class Broadcast:
    id: str
    name: str
    status: str
    message: str
    created_at: str
    sender_id: Optional[str] = None
    contact_list_id: Optional[str] = None
    scheduled_at: Optional[str] = None

    @classmethod
    def _from_dict(cls, d: dict) -> "Broadcast":
        return cls(
            id=d["id"],
            name=d["name"],
            status=d["status"],
            message=d["message"],
            created_at=d["createdAt"],
            sender_id=d.get("senderId"),
            contact_list_id=d.get("contactListId"),
            scheduled_at=d.get("scheduledAt"),
        )
