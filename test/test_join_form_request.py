# coding: utf-8

"""
    MeshDB Data API

    Programmatic access to mesh core data, detailing our installs, members, etc.   To use an authorization token, use the \"Authorize\" button, and under \"tokenAuth\" enter `Token ` before the content of your token, like this: `Token xxxyyyyyzzz`  If you have username/password credentials (like those used on the admin UI) you can login via the admin UI or [DRF login page](/auth/login/?next=/api-docs/swagger/)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pymeshdb.models.join_form_request import JoinFormRequest

class TestJoinFormRequest(unittest.TestCase):
    """JoinFormRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JoinFormRequest:
        """Test JoinFormRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JoinFormRequest`
        """
        model = JoinFormRequest()
        if include_optional:
            return JoinFormRequest(
                first_name = '',
                last_name = '',
                email = '',
                phone = '',
                street_address = '',
                city = '',
                state = '',
                zip = 56,
                apartment = '',
                roof_access = True,
                referral = '',
                ncl = True
            )
        else:
            return JoinFormRequest(
                first_name = '',
                last_name = '',
                email = '',
                phone = '',
                street_address = '',
                city = '',
                state = '',
                zip = 56,
                apartment = '',
                roof_access = True,
                referral = '',
                ncl = True,
        )
        """

    def testJoinFormRequest(self):
        """Test JoinFormRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
