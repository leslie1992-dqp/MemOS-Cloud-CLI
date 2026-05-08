from __future__ import annotations

import unittest

from memos_cli.config import DEFAULT_CONVERSATION_ID, DEFAULT_USER_ID, MemOSConfig
from memos_cli.state import apply_runtime_overrides, set_runtime_options


class RuntimeStateTests(unittest.TestCase):
    def test_apply_runtime_overrides_replaces_platform_values(self) -> None:
        config = MemOSConfig()
        config.platform.api_key = "file-key"
        config.platform.base_url = "https://example.com"

        set_runtime_options(api_key="cli-key", base_url="https://override.example.com")
        overridden = apply_runtime_overrides(config)

        self.assertEqual(overridden.platform.api_key, "cli-key")
        self.assertEqual(overridden.platform.base_url, "https://override.example.com")
        self.assertEqual(config.platform.api_key, "file-key")
        self.assertEqual(config.platform.base_url, "https://example.com")

    def test_default_user_id_is_present(self) -> None:
        config = MemOSConfig()
        self.assertEqual(config.defaults.user_id, DEFAULT_USER_ID)
        self.assertEqual(config.defaults.conversation_id, DEFAULT_CONVERSATION_ID)


if __name__ == "__main__":
    unittest.main()
