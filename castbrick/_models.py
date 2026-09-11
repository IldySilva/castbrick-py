from __future__ import annotations
from dataclasses import dataclass
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


# ── Templates ────────────────────────────────────────────────────────────────

@dataclass
class Template:
    id: str
    name: str
    content: str
    created_at: str
    subject: Optional[str] = None

    @classmethod
    def _from_dict(cls, d: dict) -> "Template":
        return cls(
            id=d["id"],
            name=d["name"],
            content=d["content"],
            created_at=d["createdAt"],
            subject=d.get("subject"),
        )


# ── Webhooks ─────────────────────────────────────────────────────────────────

@dataclass
class Webhook:
    id: str
    endpoint: str
    event_type: str
    is_active: bool
    created_at: str

    @classmethod
    def _from_dict(cls, d: dict) -> "Webhook":
        return cls(
            id=d["id"],
            endpoint=d["endpoint"],
            event_type=d["eventType"],
            is_active=d["isActive"],
            created_at=d["createdAt"],
        )


@dataclass
class WebhookLog:
    id: str
    webhook_id: str
    event_type: str
    status_code: int
    attempt: int
    delivered_at: str

    @classmethod
    def _from_dict(cls, d: dict) -> "WebhookLog":
        return cls(
            id=d["id"],
            webhook_id=d["webhookId"],
            event_type=d["eventType"],
            status_code=d["statusCode"],
            attempt=d["attempt"],
            delivered_at=d["deliveredAt"],
        )


# ── Segments ─────────────────────────────────────────────────────────────────

@dataclass
class Segment:
    id: str
    name: str
    contact_count: int
    created_at: str
    description: Optional[str] = None
    rules_operator: Optional[str] = None

    @classmethod
    def _from_dict(cls, d: dict) -> "Segment":
        return cls(
            id=d["id"],
            name=d["name"],
            contact_count=d["contactCount"],
            created_at=d["createdAt"],
            description=d.get("description"),
            rules_operator=d.get("rulesOperator"),
        )


# ── Billing ──────────────────────────────────────────────────────────────────

@dataclass
class BillingBalance:
    balance: float
    low_balance_threshold: float
    alert_email: str
    last_alert_sent_at: Optional[str] = None

    @classmethod
    def _from_dict(cls, d: dict) -> "BillingBalance":
        return cls(
            balance=d["balance"],
            low_balance_threshold=d["lowBalanceThreshold"],
            alert_email=d["alertEmail"],
            last_alert_sent_at=d.get("lastAlertSentAt"),
        )


@dataclass
class CreditPack:
    id: str
    name: str
    credits: int
    price: float
    currency: str
    price_per_sms: float

    @classmethod
    def _from_dict(cls, d: dict) -> "CreditPack":
        return cls(
            id=d["id"],
            name=d["name"],
            credits=d["credits"],
            price=d["price"],
            currency=d["currency"],
            price_per_sms=d["pricePerSms"],
        )


@dataclass
class InitiatePaymentResponse:
    payment_url: str
    provider_ref: str
    payment_id: str

    @classmethod
    def _from_dict(cls, d: dict) -> "InitiatePaymentResponse":
        return cls(
            payment_url=d["paymentUrl"],
            provider_ref=d["providerRef"],
            payment_id=d["paymentId"],
        )


@dataclass
class PaymentInfo:
    id: str
    amount: float
    currency: str
    status: str
    provider_ref: str
    credits_granted: int
    created_at: str

    @classmethod
    def _from_dict(cls, d: dict) -> "PaymentInfo":
        return cls(
            id=d["id"],
            amount=d["amount"],
            currency=d["currency"],
            status=d["status"],
            provider_ref=d["providerRef"],
            credits_granted=d["creditsGranted"],
            created_at=d["createdAt"],
        )


@dataclass
class CreditLedgerEntry:
    id: str
    amount: float
    type: str
    description: str
    created_at: str

    @classmethod
    def _from_dict(cls, d: dict) -> "CreditLedgerEntry":
        return cls(
            id=d["id"],
            amount=d["amount"],
            type=d["type"],
            description=d["description"],
            created_at=d["createdAt"],
        )
