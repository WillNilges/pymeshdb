# coding: utf-8

"""
    MeshDB Data API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pymeshdb.models.install_install_fee_billing_datum import InstallInstallFeeBillingDatum

class TestInstallInstallFeeBillingDatum(unittest.TestCase):
    """InstallInstallFeeBillingDatum unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InstallInstallFeeBillingDatum:
        """Test InstallInstallFeeBillingDatum
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InstallInstallFeeBillingDatum`
        """
        model = InstallInstallFeeBillingDatum()
        if include_optional:
            return InstallInstallFeeBillingDatum(
                id = ''
            )
        else:
            return InstallInstallFeeBillingDatum(
        )
        """

    def testInstallInstallFeeBillingDatum(self):
        """Test InstallInstallFeeBillingDatum"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
