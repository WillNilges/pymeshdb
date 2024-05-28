# coding: utf-8

"""
    MeshDB Data API

    Programmatic access to mesh core data, detailing our installs, members, etc.   To use an authorization token, use the \"Authorize\" button, and under \"tokenAuth\" enter `Token ` before the content of your token, like this: `Token xxxyyyyyzzz`  If you have username/password credentials (like those used on the admin UI) you can login via the admin UI or [DRF login page](/auth/login/?next=/api-docs/swagger/)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pymeshdb.api.legacy_query_form_api import LegacyQueryFormApi


class TestLegacyQueryFormApi(unittest.TestCase):
    """LegacyQueryFormApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LegacyQueryFormApi()

    def tearDown(self) -> None:
        pass

    def test_api_v1_query_buildings_list(self) -> None:
        """Test case for api_v1_query_buildings_list

        Query & filter based on Building attributes. Results are returned as flattened spreadsheet row style output
        """
        pass

    def test_api_v1_query_installs_list(self) -> None:
        """Test case for api_v1_query_installs_list

        Query & filter based on Install attributes. Results are returned as flattened spreadsheet row style output
        """
        pass

    def test_api_v1_query_members_list(self) -> None:
        """Test case for api_v1_query_members_list

        Query & filter based on Member attributes. Results are returned as flattened spreadsheet row style output
        """
        pass


if __name__ == '__main__':
    unittest.main()
