from __future__ import annotations
from typing import Optional
from urllib.parse import quote

from ._client import _Client
from ._models import Contact, ContactList, PagedResult


class ContactsResource:
    def __init__(self, client: _Client) -> None:
        self._c = client

    def list(
        self, page: int = 1, page_size: int = 20, search: Optional[str] = None
    ) -> PagedResult[Contact]:
        path = f"/audience/contacts?pageNumber={page}&pageSize={page_size}"
        if search:
            path += f"&search={quote(search)}"
        return PagedResult._from_dict(self._c.get(path), Contact)

    def get(self, id: str) -> Contact:
        return Contact._from_dict(self._c.get(f"/audience/contacts/{id}"))

    def create(
        self,
        *,
        emails: Optional[str] = None,
        phone_numbers: Optional[str] = None,
    ) -> int:
        body = {}
        if emails:
            body["emails"] = emails
        if phone_numbers:
            body["phoneNumbers"] = phone_numbers
        return self._c.post("/audience/contacts", body)

    def delete(self, id: str) -> None:
        self._c.delete(f"/audience/contacts/{id}")

    def list_lists(self, page: int = 1, page_size: int = 20) -> PagedResult[ContactList]:
        return PagedResult._from_dict(
            self._c.get(f"/audience/lists?pageNumber={page}&pageSize={page_size}"),
            ContactList,
        )

    def get_list(self, id: str) -> ContactList:
        return ContactList._from_dict(self._c.get(f"/audience/lists/{id}"))

    def create_list(self, name: str) -> ContactList:
        return ContactList._from_dict(self._c.post("/audience/lists", {"name": name}))

    def add_to_list(self, list_id: str, contact_id: str) -> None:
        self._c.post(f"/audience/lists/{list_id}/contacts", {"contactId": contact_id})

    def remove_from_list(self, list_id: str, contact_id: str) -> None:
        self._c.delete(f"/audience/lists/{list_id}/contacts/{contact_id}")
