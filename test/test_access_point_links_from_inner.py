# coding: utf-8

"""
    MeshDB Data API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pymeshdb.models.access_point_links_from_inner import AccessPointLinksFromInner

class TestAccessPointLinksFromInner(unittest.TestCase):
    """AccessPointLinksFromInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccessPointLinksFromInner:
        """Test AccessPointLinksFromInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessPointLinksFromInner`
        """
        model = AccessPointLinksFromInner()
        if include_optional:
            return AccessPointLinksFromInner(
                id = ''
            )
        else:
            return AccessPointLinksFromInner(
        )
        """

    def testAccessPointLinksFromInner(self):
        """Test AccessPointLinksFromInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
