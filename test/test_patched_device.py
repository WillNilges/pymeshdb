# coding: utf-8

"""
    MeshDB Data API

    Programmatic access to mesh core data, detailing our installs, members, etc.   To use an authorization token, use the \"Authorize\" button, and under \"tokenAuth\" enter `Token ` before the content of your token, like this: `Token xxxyyyyyzzz`  If you have username/password credentials (like those used on the admin UI) you can login via the admin UI or [DRF login page](/auth/login/?next=/api-docs/swagger/)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pymeshdb.models.patched_device import PatchedDevice

class TestPatchedDevice(unittest.TestCase):
    """PatchedDevice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedDevice:
        """Test PatchedDevice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedDevice`
        """
        model = PatchedDevice()
        if include_optional:
            return PatchedDevice(
                id = 56,
                network_number = -2147483648,
                links_from = [
                    56
                    ],
                links_to = [
                    56
                    ],
                name = '',
                model = '',
                type = 'ap',
                status = 'Inactive',
                latitude = 1.337,
                longitude = 1.337,
                altitude = 1.337,
                install_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                abandon_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                notes = '',
                uisp_id = '',
                ssid = '',
                ip_address = ''
            )
        else:
            return PatchedDevice(
        )
        """

    def testPatchedDevice(self):
        """Test PatchedDevice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()