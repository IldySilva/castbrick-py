from __future__ import annotations
from typing import List, Optional
from urllib.parse import quote

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
    ) -> SendSmsResponse:
        body: dict = {"recipients": to, "content": content}
        if sender_id:
            body["senderId"] = sender_id
        if scheduled_at:
            body["scheduledAt"] = scheduled_at
        if contact_list_id:
            body["contactListId"] = contact_list_id
        return SendSmsResponse._from_dict(self._c.post("/sms/send", body))

    def list(self, page: int = 1, page_size: int = 20) -> PagedResult[SmsMessage]:
        return PagedResult._from_dict(
            self._c.get(f"/sms?pageNumber={page}&pageSize={page_size}"),
            SmsMessage,
        )

    def cancel_scheduled(self, message_id: str) -> None:
        self._c.post("/sms/cancel-scheduled", {"messageId": message_id})
