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
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from pymeshdb.models.blank_enum import BlankEnum
from pymeshdb.models.link_type_enum import LinkTypeEnum
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

LINKTYPE_ONE_OF_SCHEMAS = ["BlankEnum", "LinkTypeEnum"]

class LinkType(BaseModel):
    """
    The technology used for this link 5Ghz, 60Ghz, fiber, etc.  * `5 GHz` - Five Ghz * `24 GHz` - Twentyfour Ghz * `60 GHz` - Sixty Ghz * `70-80 GHz` - Seventy Eighty Ghz * `VPN` - Vpn * `Fiber` - Fiber * `Ethernet` - Ethernet
    """
    # data type: LinkTypeEnum
    oneof_schema_1_validator: Optional[LinkTypeEnum] = None
    # data type: BlankEnum
    oneof_schema_2_validator: Optional[BlankEnum] = None
    actual_instance: Optional[Union[BlankEnum, LinkTypeEnum]] = None
    one_of_schemas: Set[str] = { "BlankEnum", "LinkTypeEnum" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        if v is None:
            return v

        instance = LinkType.model_construct()
        error_messages = []
        match = 0
        # validate data type: LinkTypeEnum
        if not isinstance(v, LinkTypeEnum):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LinkTypeEnum`")
        else:
            match += 1
        # validate data type: BlankEnum
        if not isinstance(v, BlankEnum):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BlankEnum`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in LinkType with oneOf schemas: BlankEnum, LinkTypeEnum. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in LinkType with oneOf schemas: BlankEnum, LinkTypeEnum. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: Optional[str]) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        if json_str is None:
            return instance

        error_messages = []
        match = 0

        # deserialize data into LinkTypeEnum
        try:
            instance.actual_instance = LinkTypeEnum.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BlankEnum
        try:
            instance.actual_instance = BlankEnum.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into LinkType with oneOf schemas: BlankEnum, LinkTypeEnum. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into LinkType with oneOf schemas: BlankEnum, LinkTypeEnum. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], BlankEnum, LinkTypeEnum]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


