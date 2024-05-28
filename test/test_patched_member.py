# coding: utf-8

"""
    MeshDB Data API

    Programmatic access to mesh core data, detailing our installs, members, etc.   To use an authorization token, use the \"Authorize\" button, and under \"tokenAuth\" enter `Token ` before the content of your token, like this: `Token xxxyyyyyzzz`  If you have username/password credentials (like those used on the admin UI) you can login via the admin UI or [DRF login page](/auth/login/?next=/api-docs/swagger/)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pymeshdb.models.patched_member import PatchedMember

class TestPatchedMember(unittest.TestCase):
    """PatchedMember unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedMember:
        """Test PatchedMember
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedMember`
        """
        model = PatchedMember()
        if include_optional:
            return PatchedMember(
                id = 56,
                all_email_addresses = [
                    ''
                    ],
                installs = [
                    56
                    ],
                name = '',
                primary_email_address = '',
                stripe_email_address = '',
                additional_email_addresses = [
                    ''
                    ],
                phone_number = '',
                slack_handle = '',
                notes = ''
            )
        else:
            return PatchedMember(
        )
        """

    def testPatchedMember(self):
        """Test PatchedMember"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
