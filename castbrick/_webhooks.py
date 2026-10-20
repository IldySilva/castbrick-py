from __future__ import annotations

from typing import List, Optional

from ._client import _Client
from ._models import PagedResult, Webhook, WebhookLog


class WebhooksResource:
    def __init__(self, client: _Client) -> None:
        self._client = client

    def list(self, page: int = 1, page_size: int = 10) -> PagedResult[Webhook]:
        """List webhooks for the authenticated workspace."""
        res = self._client.get("/webhooks", {"pageNumber": page, "pageSize": page_size})
        return PagedResult._from_dict(res, Webhook)

    def get(self, id: str) -> Webhook:
        """Get a webhook by ID."""
        res = self._client.get(f"/webhooks/{id}")
        return Webhook._from_dict(res)

    def create(self, endpoint: str, event_type: str) -> str:
        """Create/register a new webhook."""
        data = {"endpoint": endpoint, "eventType": event_type}
        res = self._client.post("/webhooks", data)
        return str(res)

    def toggle(self, id: str) -> None:
        """Toggle the active status of a webhook."""
        self._client.put(f"/webhooks/{id}/toggle", {})

    def test(self, webhook_id: str, payload: str) -> None:
        """Send a sample event payload to verify endpoint connectivity."""
        data = {"webhookId": webhook_id, "payload": payload}
        self._client.post("/webhooks/test", data)

    def list_logs(self, id: str, limit: int = 50) -> List[WebhookLog]:
        """List delivery attempt logs for a specific webhook."""
        res = self._client.get(f"/webhooks/{id}/logs", {"limit": limit})
        return [WebhookLog._from_dict(item) for item in res]

    def retry(self, log_id: str) -> None:
        """Retry delivery of a failed webhook event by log entry ID."""
        self._client.post(f"/webhooks/logs/{log_id}/retry", {})

    def delete(self, id: str) -> None:
        """Delete a webhook configuration."""
        self._client.delete(f"/webhooks/{id}")
