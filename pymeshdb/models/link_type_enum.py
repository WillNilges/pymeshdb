# coding: utf-8

"""
    MeshDB Data API

    Programmatic access to mesh core data, detailing our installs, members, etc.   To use an authorization token, use the \"Authorize\" button, and under \"tokenAuth\" enter `Token ` before the content of your token, like this: `Token xxxyyyyyzzz`  If you have username/password credentials (like those used on the admin UI) you can login via the admin UI or [DRF login page](/auth/login/?next=/api-docs/swagger/)

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
    * `5 GHz` - Five Ghz * `24 GHz` - Twentyfour Ghz * `60 GHz` - Sixty Ghz * `70-80 GHz` - Seventy Eighty Ghz * `VPN` - Vpn * `Fiber` - Fiber * `Ethernet` - Ethernet
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


