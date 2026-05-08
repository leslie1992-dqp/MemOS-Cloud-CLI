from __future__ import annotations

import unittest

from memos_cli.backend.transport import MemOSTransport


class TransportUrlTests(unittest.TestCase):
    def test_build_url_strips_duplicate_v1_prefix_when_base_already_has_v1(self) -> None:
        transport = MemOSTransport(
            base_url="https://memos.memtensor.cn/api/openmem/v1",
            api_key="test-key",
        )

        result = transport._build_url("/v1/memories/")

        self.assertEqual(result, "https://memos.memtensor.cn/api/openmem/v1/memories/")

    def test_build_url_keeps_v1_prefix_when_base_does_not_have_it(self) -> None:
        transport = MemOSTransport(
            base_url="https://memos.memtensor.cn/api/openmem",
            api_key="test-key",
        )

        result = transport._build_url("/v1/memories/")

        self.assertEqual(result, "https://memos.memtensor.cn/api/openmem/v1/memories/")


if __name__ == "__main__":
    unittest.main()
