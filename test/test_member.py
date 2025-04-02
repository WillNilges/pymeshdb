# coding: utf-8

"""
    MeshDB Data API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pymeshdb.models.member import Member

class TestMember(unittest.TestCase):
    """Member unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Member:
        """Test Member
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Member`
        """
        model = Member()
        if include_optional:
            return Member(
                id = '',
                all_email_addresses = [
                    ''
                    ],
                all_phone_numbers = [
                    ''
                    ],
                installs = [
                    pymeshdb.models.building_installs_inner.Building_installs_inner(
                        id = '', 
                        install_number = 56, )
                    ],
                name = '',
                primary_email_address = '',
                stripe_email_address = '',
                additional_email_addresses = [
                    ''
                    ],
                phone_number = '',
                additional_phone_numbers = [
                    ''
                    ],
                slack_handle = '',
                notes = ''
            )
        else:
            return Member(
                id = '',
                all_email_addresses = [
                    ''
                    ],
                all_phone_numbers = [
                    ''
                    ],
                installs = [
                    pymeshdb.models.building_installs_inner.Building_installs_inner(
                        id = '', 
                        install_number = 56, )
                    ],
                name = '',
        )
        """

    def testMember(self):
        """Test Member"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
