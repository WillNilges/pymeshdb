# coding: utf-8

"""
    MeshDB Data API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pymeshdb.models.paginated_node_list import PaginatedNodeList

class TestPaginatedNodeList(unittest.TestCase):
    """PaginatedNodeList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedNodeList:
        """Test PaginatedNodeList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedNodeList`
        """
        model = PaginatedNodeList()
        if include_optional:
            return PaginatedNodeList(
                count = 123,
                next = 'http://api.example.org/accounts/?page=4',
                previous = 'http://api.example.org/accounts/?page=2',
                results = [
                    pymeshdb.models.node.Node(
                        id = '', 
                        buildings = [
                            pymeshdb.models.node_buildings_inner.Node_buildings_inner(
                                id = '', )
                            ], 
                        devices = [
                            pymeshdb.models.node_devices_inner.Node_devices_inner(
                                id = '', )
                            ], 
                        installs = [
                            pymeshdb.models.building_installs_inner.Building_installs_inner(
                                id = '', 
                                install_number = 56, )
                            ], 
                        network_number = -2147483648, 
                        name = '', 
                        status = null, 
                        type = null, 
                        latitude = 1.337, 
                        longitude = 1.337, 
                        altitude = 1.337, 
                        install_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        abandon_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        notes = '', )
                    ]
            )
        else:
            return PaginatedNodeList(
                count = 123,
                results = [
                    pymeshdb.models.node.Node(
                        id = '', 
                        buildings = [
                            pymeshdb.models.node_buildings_inner.Node_buildings_inner(
                                id = '', )
                            ], 
                        devices = [
                            pymeshdb.models.node_devices_inner.Node_devices_inner(
                                id = '', )
                            ], 
                        installs = [
                            pymeshdb.models.building_installs_inner.Building_installs_inner(
                                id = '', 
                                install_number = 56, )
                            ], 
                        network_number = -2147483648, 
                        name = '', 
                        status = null, 
                        type = null, 
                        latitude = 1.337, 
                        longitude = 1.337, 
                        altitude = 1.337, 
                        install_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        abandon_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        notes = '', )
                    ],
        )
        """

    def testPaginatedNodeList(self):
        """Test PaginatedNodeList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
