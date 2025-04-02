# coding: utf-8

"""
    MeshDB Data API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pymeshdb.models.query_form import QueryForm

class TestQueryForm(unittest.TestCase):
    """QueryForm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QueryForm:
        """Test QueryForm
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QueryForm`
        """
        model = QueryForm()
        if include_optional:
            return QueryForm(
                install_number = 56,
                street_address = '',
                unit = '',
                city = '',
                state = '',
                zip_code = '',
                name = '',
                phone_number = '',
                additional_phone_numbers = [
                    ''
                    ],
                primary_email_address = '',
                stripe_email_address = '',
                additional_email_addresses = [
                    ''
                    ],
                notes = '',
                network_number = 56,
                network_number_status = '',
                status = 'Request Received'
            )
        else:
            return QueryForm(
                install_number = 56,
                street_address = '',
                city = '',
                state = '',
                zip_code = '',
                name = '',
                phone_number = '',
                additional_phone_numbers = [
                    ''
                    ],
                primary_email_address = '',
                stripe_email_address = '',
                additional_email_addresses = [
                    ''
                    ],
                notes = '',
                network_number = 56,
                network_number_status = '',
                status = 'Request Received',
        )
        """

    def testQueryForm(self):
        """Test QueryForm"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
