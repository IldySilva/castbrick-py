from __future__ import annotations

import json
import urllib.request
import urllib.error
import urllib.parse
from typing import Any, Optional


class CastBrickApiError(Exception):
    def __init__(self, status_code: int, body: str) -> None:
        self.status_code = status_code
        self.body = body
        super().__init__(f"CastBrick API error {status_code}: {body}")


class _Client:
    def __init__(self, api_key: str, base_url: str) -> None:
        self._api_key = api_key
        self._base_url = base_url.rstrip("/")

    def _request(self, method: str, path: str, body: Any = None) -> Any:
        url = self._base_url + path
        data = json.dumps(body).encode() if body is not None else None
        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Accept": "application/json",
        }
        if data is not None:
            headers["Content-Type"] = "application/json"

        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req) as resp:
                raw = resp.read()
                if not raw:
                    return None
                return json.loads(raw)
        except urllib.error.HTTPError as e:
            body = e.read().decode(errors="replace")
            raise CastBrickApiError(e.code, body) from e

    def get(self, path: str, params: Optional[dict] = None) -> Any:
        if params:
            filtered = {k: str(v) for k, v in params.items() if v is not None}
            if filtered:
                path = path + "?" + urllib.parse.urlencode(filtered)
        return self._request("GET", path)

    def post(self, path: str, body: Any = None) -> Any:
        return self._request("POST", path, body)

    def put(self, path: str, body: Any) -> Any:
        return self._request("PUT", path, body)

    def delete(self, path: str) -> None:
        self._request("DELETE", path)
