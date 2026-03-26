from __future__ import annotations
from typing import Optional

from ._client import _Client
from ._models import Broadcast, PagedResult


class BroadcastsResource:
    def __init__(self, client: _Client) -> None:
        self._c = client

    def list(self, page: int = 1, page_size: int = 20) -> PagedResult[Broadcast]:
        return PagedResult._from_dict(
            self._c.get(f"/broadcasts?pageNumber={page}&pageSize={page_size}"),
            Broadcast,
        )

    def get(self, id: str) -> Broadcast:
        return Broadcast._from_dict(self._c.get(f"/broadcasts/{id}"))

    def create(
        self,
        *,
        name: str,
        message: str,
        contact_list_id: Optional[str] = None,
        sender_id: Optional[str] = None,
    ) -> str:
        body: dict = {"name": name, "message": message}
        if contact_list_id:
            body["contactListId"] = contact_list_id
        if sender_id:
            body["senderId"] = sender_id
        return self._c.post("/broadcasts", body)

    def update(
        self,
        id: str,
        *,
        name: str,
        message: str,
        contact_list_id: Optional[str] = None,
        sender_id: Optional[str] = None,
        schedule_at: Optional[str] = None,
    ) -> str:
        body: dict = {"name": name, "message": message}
        if contact_list_id:
            body["contactListId"] = contact_list_id
        if sender_id:
            body["senderId"] = sender_id
        if schedule_at:
            body["scheduleAt"] = schedule_at
        return self._c.put(f"/broadcasts/{id}", body)

    def send(self, id: str) -> None:
        self._c.post(f"/broadcasts/{id}/send", {})

    def cancel(self, id: str) -> None:
        self._c.post(f"/broadcasts/{id}/cancel", {})

    def duplicate(self, id: str) -> str:
        return self._c.post(f"/broadcasts/{id}/duplicate", {})

    def delete(self, id: str) -> None:
        self._c.delete(f"/broadcasts/{id}")
