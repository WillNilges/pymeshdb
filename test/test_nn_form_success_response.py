# coding: utf-8

"""
    MeshDB Data API

    Programmatic access to mesh core data, detailing our installs, members, etc.   To use an authorization token, use the \"Authorize\" button, and under \"tokenAuth\" enter `Token ` before the content of your token, like this: `Token xxxyyyyyzzz`  If you have username/password credentials (like those used on the admin UI) you can login via the admin UI or [DRF login page](/auth/login/?next=/api-docs/swagger/)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pymeshdb.models.nn_form_success_response import NNFormSuccessResponse

class TestNNFormSuccessResponse(unittest.TestCase):
    """NNFormSuccessResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NNFormSuccessResponse:
        """Test NNFormSuccessResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NNFormSuccessResponse`
        """
        model = NNFormSuccessResponse()
        if include_optional:
            return NNFormSuccessResponse(
                detail = '',
                building_id = 56,
                install_number = 56,
                network_number = 56,
                created = True
            )
        else:
            return NNFormSuccessResponse(
                detail = '',
                building_id = 56,
                install_number = 56,
                network_number = 56,
                created = True,
        )
        """

    def testNNFormSuccessResponse(self):
        """Test NNFormSuccessResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
