# coding: utf-8

"""
    MeshDB Data API

    Programmatic access to mesh core data, detailing our installs, members, etc.   To use an authorization token, use the \"Authorize\" button, and under \"tokenAuth\" enter `Token ` before the content of your token, like this: `Token xxxyyyyyzzz`  If you have username/password credentials (like those used on the admin UI) you can login via the admin UI or [DRF login page](/auth/login/?next=/api-docs/swagger/)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pymeshdb.models.paginated_link_list import PaginatedLinkList

class TestPaginatedLinkList(unittest.TestCase):
    """PaginatedLinkList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedLinkList:
        """Test PaginatedLinkList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedLinkList`
        """
        model = PaginatedLinkList()
        if include_optional:
            return PaginatedLinkList(
                count = 123,
                next = 'http://api.example.org/accounts/?page=4',
                previous = 'http://api.example.org/accounts/?page=2',
                results = [
                    pymeshdb.models.link.Link(
                        id = 56, 
                        status = null, 
                        type = null, 
                        install_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        abandon_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        description = '', 
                        notes = '', 
                        uisp_id = '', 
                        from_device = 56, 
                        to_device = 56, )
                    ]
            )
        else:
            return PaginatedLinkList(
                count = 123,
                results = [
                    pymeshdb.models.link.Link(
                        id = 56, 
                        status = null, 
                        type = null, 
                        install_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        abandon_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        description = '', 
                        notes = '', 
                        uisp_id = '', 
                        from_device = 56, 
                        to_device = 56, )
                    ],
        )
        """

    def testPaginatedLinkList(self):
        """Test PaginatedLinkList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
