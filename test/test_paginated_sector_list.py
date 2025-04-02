# coding: utf-8

"""
    MeshDB Data API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pymeshdb.models.paginated_sector_list import PaginatedSectorList

class TestPaginatedSectorList(unittest.TestCase):
    """PaginatedSectorList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedSectorList:
        """Test PaginatedSectorList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedSectorList`
        """
        model = PaginatedSectorList()
        if include_optional:
            return PaginatedSectorList(
                count = 123,
                next = 'http://api.example.org/accounts/?page=4',
                previous = 'http://api.example.org/accounts/?page=2',
                results = [
                    pymeshdb.models.sector.Sector(
                        id = '', 
                        latitude = 1.337, 
                        longitude = 1.337, 
                        altitude = 1.337, 
                        links_from = [
                            pymeshdb.models.access_point_links_from_inner.AccessPoint_links_from_inner(
                                id = '', )
                            ], 
                        links_to = [
                            pymeshdb.models.access_point_links_from_inner.AccessPoint_links_from_inner(
                                id = '', )
                            ], 
                        name = '', 
                        status = null, 
                        install_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        abandon_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        notes = '', 
                        uisp_id = '', 
                        radius = 0, 
                        azimuth = 0, 
                        width = 0, 
                        node = pymeshdb.models.access_point_node.AccessPoint_node(
                            id = '', 
                            network_number = -2147483648, ), )
                    ]
            )
        else:
            return PaginatedSectorList(
                count = 123,
                results = [
                    pymeshdb.models.sector.Sector(
                        id = '', 
                        latitude = 1.337, 
                        longitude = 1.337, 
                        altitude = 1.337, 
                        links_from = [
                            pymeshdb.models.access_point_links_from_inner.AccessPoint_links_from_inner(
                                id = '', )
                            ], 
                        links_to = [
                            pymeshdb.models.access_point_links_from_inner.AccessPoint_links_from_inner(
                                id = '', )
                            ], 
                        name = '', 
                        status = null, 
                        install_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        abandon_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        notes = '', 
                        uisp_id = '', 
                        radius = 0, 
                        azimuth = 0, 
                        width = 0, 
                        node = pymeshdb.models.access_point_node.AccessPoint_node(
                            id = '', 
                            network_number = -2147483648, ), )
                    ],
        )
        """

    def testPaginatedSectorList(self):
        """Test PaginatedSectorList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
