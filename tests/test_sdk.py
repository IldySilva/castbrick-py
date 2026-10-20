"""
Comprehensive tests for castbrick Python SDK against the mock server.
"""

import os
import subprocess
import time
import unittest
import urllib.request
from pathlib import Path
from castbrick import CastBrick, CastBrickApiError

BASE_URL = os.getenv("CASTBRICK_BASE_URL", "http://127.0.0.1:8787/v1")
API_KEY = os.getenv("CASTBRICK_API_KEY", "test_api_key")


class TestCastBrickSdk(unittest.TestCase):
    mock_proc = None

    @classmethod
    def setUpClass(cls):
        health_url = BASE_URL.replace("/v1", "").rstrip("/") + "/health"
        try:
            with urllib.request.urlopen(health_url, timeout=1) as response:
                if response.status == 200:
                    return
        except Exception:
            pass

        server_script = Path(__file__).resolve().parent.parent / "tools" / "mock-server" / "server.js"
        if server_script.exists():
            cls.mock_proc = subprocess.Popen(
                ["node", str(server_script), "8787"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            time.sleep(0.5)

    @classmethod
    def tearDownClass(cls):
        if cls.mock_proc:
            cls.mock_proc.terminate()
            cls.mock_proc.wait()

    def setUp(self):
        self.cb = CastBrick(api_key=API_KEY, base_url=BASE_URL)

    def test_resources_initialized(self):
        self.assertIsNotNone(self.cb.sms)
        self.assertIsNotNone(self.cb.contacts)
        self.assertIsNotNone(self.cb.broadcasts)
        self.assertIsNotNone(self.cb.billing)

    def test_sms_send(self):
        res = self.cb.sms.send(
            to=["+244923000000"],
            content="Hello from Python SDK test!",
        )
        self.assertTrue(bool(res.message_id))
        self.assertEqual(res.status, "Queued")
        self.assertEqual(res.recipient_count, 1)

    def test_sms_list(self):
        res = self.cb.sms.list(page=1, page_size=10)
        self.assertIsInstance(res.items, list)
        self.assertGreaterEqual(res.total_count, 1)

    def test_contacts_list(self):
        res = self.cb.contacts.list(page=1, page_size=10)
        self.assertIsInstance(res.items, list)

    def test_contacts_create(self):
        # create does not return data, ensures no error is raised
        self.cb.contacts.create(phone_numbers="+244923000000")

    def test_broadcasts_create_and_list(self):
        bc = self.cb.broadcasts.create(
            name="Test Campaign",
            message="Campaign message",
        )
        self.assertTrue(bool(bc.get("id") if isinstance(bc, dict) else bc))

        res = self.cb.broadcasts.list(page=1, page_size=10)
        self.assertIsInstance(res.items, list)

    def test_billing_get_balance(self):
        bal = self.cb.billing.get_balance()
        self.assertEqual(bal.balance, 50000.0)
        self.assertEqual(bal.low_balance_threshold, 500.0)

    def test_unauthorized_error(self):
        bad_cb = CastBrick(api_key="invalid_key", base_url=BASE_URL)
        with self.assertRaises(CastBrickApiError) as ctx:
            bad_cb.sms.send(to=["+244923000000"], content="fail")
        self.assertEqual(ctx.exception.status_code, 401)


if __name__ == "__main__":
    unittest.main()
