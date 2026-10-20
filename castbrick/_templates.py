from __future__ import annotations

from typing import Optional

from ._client import _Client
from ._models import PagedResult, Template


class TemplatesResource:
    def __init__(self, client: _Client) -> None:
        self._client = client

    def list(self, page: int = 1, page_size: int = 20) -> PagedResult[Template]:
        """List templates for the authenticated workspace."""
        res = self._client.get("/templates", {"page": page, "pageSize": page_size})
        return PagedResult._from_dict(res, Template)

    def create(
        self,
        name: str,
        content: str,
        subject: Optional[str] = None,
    ) -> str:
        """Create a new template."""
        data = {"name": name, "content": content}
        if subject is not None:
            data["subject"] = subject

        res = self._client.post("/templates", data)
        return str(res)

    def update(
        self,
        id: str,
        name: str,
        content: str,
        subject: Optional[str] = None,
    ) -> str:
        """Update an existing template."""
        data = {"name": name, "content": content}
        if subject is not None:
            data["subject"] = subject

        res = self._client.put(f"/templates/{id}", data)
        return str(res)

    def delete(self, id: str) -> None:
        """Delete a template."""
        self._client.delete(f"/templates/{id}")
