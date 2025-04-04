# coding: utf-8

"""
    MeshDB Data API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pymeshdb.api.geographic_kml_data_api import GeographicKMLDataApi


class TestGeographicKMLDataApi(unittest.TestCase):
    """GeographicKMLDataApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GeographicKMLDataApi()

    def tearDown(self) -> None:
        pass

    def test_api_v1_geography_nyc_geocode_v2_search_retrieve(self) -> None:
        """Test case for api_v1_geography_nyc_geocode_v2_search_retrieve

        Use the NYC geocoding APIs to look up an address, and return the lat/lon/alt corresponding to it or 404 if the address cannot be found within NYC
        """
        pass

    def test_api_v1_geography_whole_mesh_kml_retrieve(self) -> None:
        """Test case for api_v1_geography_whole_mesh_kml_retrieve

        Generate a KML file which contains all nodes and links on the mesh
        """
        pass


if __name__ == '__main__':
    unittest.main()
