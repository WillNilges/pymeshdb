# coding: utf-8

"""
    MeshDB Data API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class InstallFeeBillingDatumStatusEnum(str, Enum):
    """
    * `ToBeBilled` - To Be Billed * `Billed` - Billed * `NotBillingDuplicate` - Not Billing - Duplicate * `NotBillingOther` - Not Billing - Other
    """

    """
    allowed enum values
    """
    TOBEBILLED = 'ToBeBilled'
    BILLED = 'Billed'
    NOTBILLINGDUPLICATE = 'NotBillingDuplicate'
    NOTBILLINGOTHER = 'NotBillingOther'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of InstallFeeBillingDatumStatusEnum from a JSON string"""
        return cls(json.loads(json_str))


