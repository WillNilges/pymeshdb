# coding: utf-8

"""
    MeshDB Data API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pymeshdb.models.error_response_missing_fields import ErrorResponseMissingFields

class TestErrorResponseMissingFields(unittest.TestCase):
    """ErrorResponseMissingFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ErrorResponseMissingFields:
        """Test ErrorResponseMissingFields
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorResponseMissingFields`
        """
        model = ErrorResponseMissingFields()
        if include_optional:
            return ErrorResponseMissingFields(
                detail = {
                    'key' : null
                    }
            )
        else:
            return ErrorResponseMissingFields(
                detail = {
                    'key' : null
                    },
        )
        """

    def testErrorResponseMissingFields(self):
        """Test ErrorResponseMissingFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
