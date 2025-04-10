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


class Status432Enum(str, Enum):
    """
    * `Inactive` - Inactive * `Active` - Active * `Potential` - Potential
    """

    """
    allowed enum values
    """
    INACTIVE = 'Inactive'
    ACTIVE = 'Active'
    POTENTIAL = 'Potential'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Status432Enum from a JSON string"""
        return cls(json.loads(json_str))


