# coding: utf-8

"""
    MeshDB Data API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pymeshdb.models.kiosk_data import KioskData

class TestKioskData(unittest.TestCase):
    """KioskData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KioskData:
        """Test KioskData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KioskData`
        """
        model = KioskData()
        if include_optional:
            return KioskData(
                street_address = '',
                type = '',
                id = 56,
                coordinates = [
                    1.337
                    ],
                status = ''
            )
        else:
            return KioskData(
                street_address = '',
                type = '',
                id = 56,
                coordinates = [
                    1.337
                    ],
        )
        """

    def testKioskData(self):
        """Test KioskData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
