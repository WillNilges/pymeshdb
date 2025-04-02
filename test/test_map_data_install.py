# coding: utf-8

"""
    MeshDB Data API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pymeshdb.models.map_data_install import MapDataInstall

class TestMapDataInstall(unittest.TestCase):
    """MapDataInstall unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MapDataInstall:
        """Test MapDataInstall
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MapDataInstall`
        """
        model = MapDataInstall()
        if include_optional:
            return MapDataInstall(
                id = 56,
                name = '',
                status = '',
                coordinates = [
                    1.337
                    ],
                request_date = 56,
                install_date = 56,
                roof_access = True,
                notes = '',
                panoramas = [
                    ''
                    ]
            )
        else:
            return MapDataInstall(
                id = 56,
                name = '',
                status = '',
                coordinates = [
                    1.337
                    ],
                request_date = 56,
                install_date = 56,
                roof_access = True,
                notes = '',
                panoramas = [
                    ''
                    ],
        )
        """

    def testMapDataInstall(self):
        """Test MapDataInstall"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
