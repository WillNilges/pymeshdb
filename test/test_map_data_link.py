# coding: utf-8

"""
    MeshDB Data API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pymeshdb.models.map_data_link import MapDataLink

class TestMapDataLink(unittest.TestCase):
    """MapDataLink unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MapDataLink:
        """Test MapDataLink
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MapDataLink`
        """
        model = MapDataLink()
        if include_optional:
            return MapDataLink(
                var_from = 56,
                to = 56,
                status = '',
                install_date = 56
            )
        else:
            return MapDataLink(
                var_from = 56,
                to = 56,
                status = '',
                install_date = 56,
        )
        """

    def testMapDataLink(self):
        """Test MapDataLink"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
