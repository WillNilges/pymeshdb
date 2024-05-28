# coding: utf-8

"""
    MeshDB Data API

    Programmatic access to mesh core data, detailing our installs, members, etc.   To use an authorization token, use the \"Authorize\" button, and under \"tokenAuth\" enter `Token ` before the content of your token, like this: `Token xxxyyyyyzzz`  If you have username/password credentials (like those used on the admin UI) you can login via the admin UI or [DRF login page](/auth/login/?next=/api-docs/swagger/)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pymeshdb.api.sectors_api import SectorsApi


class TestSectorsApi(unittest.TestCase):
    """SectorsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SectorsApi()

    def tearDown(self) -> None:
        pass

    def test_api_v1_sectors_create(self) -> None:
        """Test case for api_v1_sectors_create

        """
        pass

    def test_api_v1_sectors_destroy(self) -> None:
        """Test case for api_v1_sectors_destroy

        """
        pass

    def test_api_v1_sectors_list(self) -> None:
        """Test case for api_v1_sectors_list

        """
        pass

    def test_api_v1_sectors_lookup_list(self) -> None:
        """Test case for api_v1_sectors_lookup_list

        """
        pass

    def test_api_v1_sectors_partial_update(self) -> None:
        """Test case for api_v1_sectors_partial_update

        """
        pass

    def test_api_v1_sectors_retrieve(self) -> None:
        """Test case for api_v1_sectors_retrieve

        """
        pass

    def test_api_v1_sectors_update(self) -> None:
        """Test case for api_v1_sectors_update

        """
        pass


if __name__ == '__main__':
    unittest.main()