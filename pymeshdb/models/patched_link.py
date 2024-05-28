# coding: utf-8

"""
    MeshDB Data API

    Programmatic access to mesh core data, detailing our installs, members, etc.   To use an authorization token, use the \"Authorize\" button, and under \"tokenAuth\" enter `Token ` before the content of your token, like this: `Token xxxyyyyyzzz`  If you have username/password credentials (like those used on the admin UI) you can login via the admin UI or [DRF login page](/auth/login/?next=/api-docs/swagger/)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pymeshdb.models.link_status_enum import LinkStatusEnum
from pymeshdb.models.link_type import LinkType
from typing import Optional, Set
from typing_extensions import Self

class PatchedLink(BaseModel):
    """
    PatchedLink
    """ # noqa: E501
    id: Optional[StrictInt] = None
    status: Optional[LinkStatusEnum] = Field(default=None, description="The current status of this link  * `Inactive` - Inactive * `Planned` - Planned * `Active` - Active")
    type: Optional[LinkType] = None
    install_date: Optional[date] = Field(default=None, description="The date this link was created")
    abandon_date: Optional[date] = Field(default=None, description="The date this link was powered off, disassembled, or abandoned")
    description: Optional[StrictStr] = Field(default=None, description="A short description of \"where to where\" this link connects in human readable language")
    notes: Optional[StrictStr] = Field(default=None, description="A free-form text description of this Link, to track any additional information.")
    uisp_id: Optional[StrictStr] = Field(default=None, description="The UUID used to indentify this link in UISP (if applicable)")
    from_device: Optional[StrictInt] = Field(default=None, description="The device on one side of this network link, from/to are not meaningful except to disambiguate")
    to_device: Optional[StrictInt] = Field(default=None, description="The device on one side of this network link, from/to are not meaningful except to disambiguate")
    __properties: ClassVar[List[str]] = ["id", "status", "type", "install_date", "abandon_date", "description", "notes", "uisp_id", "from_device", "to_device"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PatchedLink from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if install_date (nullable) is None
        # and model_fields_set contains the field
        if self.install_date is None and "install_date" in self.model_fields_set:
            _dict['install_date'] = None

        # set to None if abandon_date (nullable) is None
        # and model_fields_set contains the field
        if self.abandon_date is None and "abandon_date" in self.model_fields_set:
            _dict['abandon_date'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        # set to None if uisp_id (nullable) is None
        # and model_fields_set contains the field
        if self.uisp_id is None and "uisp_id" in self.model_fields_set:
            _dict['uisp_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedLink from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "status": obj.get("status"),
            "type": LinkType.from_dict(obj["type"]) if obj.get("type") is not None else None,
            "install_date": obj.get("install_date"),
            "abandon_date": obj.get("abandon_date"),
            "description": obj.get("description"),
            "notes": obj.get("notes"),
            "uisp_id": obj.get("uisp_id"),
            "from_device": obj.get("from_device"),
            "to_device": obj.get("to_device")
        })
        return _obj

