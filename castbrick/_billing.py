from __future__ import annotations

from typing import List, Optional, Tuple

from ._client import _Client
from ._models import BillingBalance, CreditLedgerEntry, CreditPack, InitiatePaymentResponse, PagedResult, PaymentInfo


class BillingResource:
    def __init__(self, client: _Client) -> None:
        self._client = client

    def get_balance(self) -> BillingBalance:
        """Get the current billing credit balance and configuration."""
        res = self._client.get("/billing/balance")
        return BillingBalance._from_dict(res)

    def list_packages(self) -> list[CreditPack]:
        """List available credit packages."""
        res = self._client.get("/billing/packages")
        return [CreditPack._from_dict(item) for item in res]

    def initiate_payment(
        self,
        package_id: str,
        provider: str,
        method: str,
        currency: str,
        return_url: str,
        cancel_url: str,
        success_url: str,
        failure_url: str,
    ) -> InitiatePaymentResponse:
        """Initiate a credit package purchase transaction."""
        data = {
            "packageId": package_id,
            "provider": provider,
            "method": method,
            "currency": currency,
            "returnUrl": return_url,
            "cancelUrl": cancel_url,
            "successUrl": success_url,
            "failureUrl": failure_url,
        }
        res = self._client.post("/billing/payments/initiate", data)
        return InitiatePaymentResponse._from_dict(res)

    def list_payments(
        self,
        cursor: Optional[str] = None,
        limit: Optional[int] = None,
        status: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
    ) -> tuple[list[PaymentInfo], Optional[str]]:
        """List payments for the authenticated workspace."""
        params = {}
        if cursor is not None:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = limit
        if status is not None:
            params["status"] = status
        if from_date is not None:
            params["from"] = from_date
        if to_date is not None:
            params["to"] = to_date

        res = self._client.get("/billing/payments", params)
        items = [PaymentInfo._from_dict(item) for item in res.get("items", [])]
        return items, res.get("nextCursor")

    def list_transactions(self, cursor: Optional[str] = None) -> tuple[list[CreditLedgerEntry], Optional[str]]:
        """List balance transaction history / ledger entries."""
        params = {}
        if cursor is not None:
            params["cursor"] = cursor

        res = self._client.get("/billing/transactions", params)
        items = [CreditLedgerEntry._from_dict(item) for item in res.get("items", [])]
        return items, res.get("nextCursor")
