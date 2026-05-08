from __future__ import annotations

import unittest

from memos_cli.backend.memory_api import MemoryAPI


class StubTransport:
    def __init__(self) -> None:
        self.calls: list[tuple[str, str, dict]] = []

    def request_json(self, method: str, path: str, **kwargs):
        self.calls.append((method, path, kwargs))
        return {
            "code": 0,
            "data": {
                "memory_detail_list": [],
                "preference_detail_list": [],
                "tool_memory_detail_list": [],
                "pages": 1,
            },
        }

    def request_first_json(self, method: str, paths: list[str], **kwargs):
        self.calls.append((method, paths[0], kwargs))
        return {"data": {"memories": []}}


class MemoryApiListTests(unittest.TestCase):
    def test_list_memories_caps_page_size_at_50(self) -> None:
        transport = StubTransport()
        api = MemoryAPI(transport)

        api.list_memories(user_id="user-123", page_size=100)

        _, _, kwargs = transport.calls[0]
        self.assertEqual(kwargs["json_body"]["size"], 50)


if __name__ == "__main__":
    unittest.main()
