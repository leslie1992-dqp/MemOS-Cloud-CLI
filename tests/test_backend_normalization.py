from __future__ import annotations

import unittest

from memos_cli.backend.normalizers import normalize_add_response, normalize_search_response


class BackendNormalizationTests(unittest.TestCase):
    def test_normalize_search_response_flattens_memory_and_preference_lists(self) -> None:
        payload = {
            "data": {
                "memory_detail_list": [
                    {"memory_id": "mem-1", "memory_value": "User likes coffee", "score": 0.9}
                ],
                "preference_detail_list": [
                    {
                        "preference_id": "pref-1",
                        "preference": "Prefers dark mode",
                        "preference_type": "explicit_preference",
                    }
                ],
            }
        }

        result = normalize_search_response(payload)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["id"], "mem-1")
        self.assertEqual(result[0]["memory"], "User likes coffee")
        self.assertEqual(result[1]["id"], "pref-1")
        self.assertEqual(result[1]["memory"], "Prefers dark mode")

    def test_normalize_add_response_wraps_single_data_item(self) -> None:
        payload = {
            "data": {
                "memory_id": "mem-2",
                "memory_value": "User is allergic to peanuts",
            }
        }

        result = normalize_add_response(payload, original_text="User is allergic to peanuts")

        self.assertEqual(result["results"][0]["id"], "mem-2")
        self.assertEqual(result["results"][0]["memory"], "User is allergic to peanuts")


if __name__ == "__main__":
    unittest.main()
