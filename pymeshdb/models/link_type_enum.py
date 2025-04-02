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


class LinkTypeEnum(str, Enum):
    """
    * `5 GHz` - 5 GHz * `24 GHz` - 24 GHz * `60 GHz` - 60 GHz * `70-80 GHz` - 70-80 GHz * `VPN` - VPN * `Fiber` - Fiber * `Ethernet` - Ethernet
    """

    """
    allowed enum values
    """
    ENUM_5_GHZ = '5 GHz'
    ENUM_24_GHZ = '24 GHz'
    ENUM_60_GHZ = '60 GHz'
    ENUM_70_MINUS_80_GHZ = '70-80 GHz'
    VPN = 'VPN'
    FIBER = 'Fiber'
    ETHERNET = 'Ethernet'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LinkTypeEnum from a JSON string"""
        return cls(json.loads(json_str))


