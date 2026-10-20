from __future__ import annotations

from typing import Optional

from ._client import _Client
from ._models import PagedResult, Segment


class SegmentsResource:
    def __init__(self, client: _Client) -> None:
        self._client = client

    def list(
        self,
        page: int = 1,
        page_size: int = 50,
        search: Optional[str] = None,
    ) -> PagedResult[Segment]:
        """List segments for the authenticated workspace."""
        params = {"pageNumber": page, "pageSize": page_size}
        if search is not None:
            params["search"] = search

        res = self._client.get("/audience/segments", params)
        return PagedResult._from_dict(res, Segment)

    def create(
        self,
        name: str,
        description: Optional[str] = None,
        rules_operator: Optional[str] = None,
        rules: Optional[str] = None,
    ) -> str:
        """Create a new dynamic segment."""
        data = {"name": name}
        if description is not None:
            data["description"] = description
        if rules_operator is not None:
            data["rulesOperator"] = rules_operator
        if rules is not None:
            data["rules"] = rules

        res = self._client.post("/audience/segments", data)
        return str(res)

    def update(
        self,
        id: str,
        name: str,
        description: Optional[str] = None,
        rules_operator: Optional[str] = None,
        rules: Optional[str] = None,
    ) -> None:
        """Update an existing segment."""
        data = {"name": name}
        if description is not None:
            data["description"] = description
        if rules_operator is not None:
            data["rulesOperator"] = rules_operator
        if rules is not None:
            data["rules"] = rules

        self._client.put(f"/audience/segments/{id}", data)

    def delete(self, id: str) -> None:
        """Delete a segment."""
        self._client.delete(f"/audience/segments/{id}")
