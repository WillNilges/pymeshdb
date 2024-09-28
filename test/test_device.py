# coding: utf-8

"""
    MeshDB Data API

    Programmatic access to mesh core data, detailing our installs, members, etc.   To use an authorization token, use the \"Authorize\" button, and under \"tokenAuth\" enter `Token ` before the content of your token, like this: `Token xxxyyyyyzzz`  If you have username/password credentials (like those used on the admin UI) you can login via the admin UI or [DRF login page](/auth/login/?next=/api-docs/swagger/)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pymeshdb.models.device import Device

class TestDevice(unittest.TestCase):
    """Device unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Device:
        """Test Device
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Device`
        """
        model = Device()
        if include_optional:
            return Device(
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
                status = 'Inactive',
                install_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                abandon_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                notes = '',
                uisp_id = '',
                node = pymeshdb.models.access_point_node.AccessPoint_node(
                    id = '', 
                    network_number = -2147483648, )
            )
        else:
            return Device(
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
                status = 'Inactive',
                node = pymeshdb.models.access_point_node.AccessPoint_node(
                    id = '', 
                    network_number = -2147483648, ),
        )
        """

    def testDevice(self):
        """Test Device"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
