# coding: utf-8

"""
    MeshDB Data API

    Programmatic access to mesh core data, detailing our installs, members, etc.   To use an authorization token, use the \"Authorize\" button, and under \"tokenAuth\" enter `Token ` before the content of your token, like this: `Token xxxyyyyyzzz`  If you have username/password credentials (like those used on the admin UI) you can login via the admin UI or [DRF login page](/auth/login/?next=/api-docs/swagger/)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pymeshdb.api.devices_api import DevicesApi


class TestDevicesApi(unittest.TestCase):
    """DevicesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DevicesApi()

    def tearDown(self) -> None:
        pass

    def test_api_v1_devices_create(self) -> None:
        """Test case for api_v1_devices_create

        """
        pass

    def test_api_v1_devices_destroy(self) -> None:
        """Test case for api_v1_devices_destroy

        """
        pass

    def test_api_v1_devices_list(self) -> None:
        """Test case for api_v1_devices_list

        """
        pass

    def test_api_v1_devices_lookup_list(self) -> None:
        """Test case for api_v1_devices_lookup_list

        """
        pass

    def test_api_v1_devices_partial_update(self) -> None:
        """Test case for api_v1_devices_partial_update

        """
        pass

    def test_api_v1_devices_retrieve(self) -> None:
        """Test case for api_v1_devices_retrieve

        """
        pass

    def test_api_v1_devices_update(self) -> None:
        """Test case for api_v1_devices_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
