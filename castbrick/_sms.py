from __future__ import annotations
from typing import List, Optional

from ._client import _Client
from ._models import PagedResult, SendSmsResponse, SmsMessage


class SmsResource:
    def __init__(self, client: _Client) -> None:
        self._c = client

    def send(
        self,
        *,
        to: List[str],
        content: str,
        sender_id: Optional[str] = None,
        scheduled_at: Optional[str] = None,
        contact_list_id: Optional[str] = None,
        fallback: Optional[bool] = None,
    ) -> SendSmsResponse:
        body: dict = {"recipients": to, "content": content}
        if sender_id:
            body["senderId"] = sender_id
        if scheduled_at:
            body["scheduledAt"] = scheduled_at
        if contact_list_id:
            body["contactListId"] = contact_list_id
        if fallback is not None:
            body["fallback"] = fallback
        return SendSmsResponse._from_dict(self._c.post("/sms/send", body))

    def list(
        self,
        page: int = 1,
        page_size: int = 20,
        status: Optional[str] = None,
        phone: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
    ) -> PagedResult[SmsMessage]:
        params: dict = {"pageNumber": page, "pageSize": page_size}
        if status:
            params["status"] = status
        if phone:
            params["phone"] = phone
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date
        return PagedResult._from_dict(self._c.get("/sms", params), SmsMessage)

    def cancel_scheduled(self, message_id: str) -> None:
        """Cancel a scheduled SMS by its ID."""
        self._c.delete(f"/sms/{message_id}")
