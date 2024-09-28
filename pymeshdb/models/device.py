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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from pymeshdb.models.access_point_links_from_inner import AccessPointLinksFromInner
from pymeshdb.models.access_point_node import AccessPointNode
from pymeshdb.models.status432_enum import Status432Enum
from typing import Optional, Set
from typing_extensions import Self

class Device(BaseModel):
    """
    A  ModelSerializer MixIn which sets `NestedKeyObjectRelatedField` as the default field class to use for the foreign key fields
    """ # noqa: E501
    id: StrictStr
    latitude: Union[StrictFloat, StrictInt] = Field(description="Approximate Device latitude in decimal degrees (this is read through from the attached Node object, not stored separately)")
    longitude: Union[StrictFloat, StrictInt] = Field(description="Approximate Device longitude in decimal degrees (this is read through from the attached Node object, not stored separately)")
    altitude: Union[StrictFloat, StrictInt] = Field(description="Approximate Device altitude in \"absolute\" meters above mean sea level (this is read through from the attached Node object, not stored separately)")
    links_from: List[AccessPointLinksFromInner]
    links_to: List[AccessPointLinksFromInner]
    name: Optional[StrictStr] = Field(default=None, description="The name of this device, usually configured as the hostname in the device firmware, usually in the format nycmesh-xxxx-yyyy-zzzz, where xxxx is the network number for the node this device is located at, yyyy is the type of the device, and zzzz is the network number of the other side of the link this device creates (if applicable)")
    status: Status432Enum = Field(description="The current status of this device  * `Inactive` - Inactive * `Active` - Active * `Potential` - Potential")
    install_date: Optional[date] = Field(default=None, description="The date this device first became active on the mesh")
    abandon_date: Optional[date] = Field(default=None, description="The this device was abandoned, unplugged, or removed from service")
    notes: Optional[StrictStr] = Field(default=None, description="A free-form text description of this Device, to track any additional information. For imported Devices, this starts with a formatted block of information about the import processand original data. However this structure can be changed by admins at any time and should not be relied onby automated systems. ")
    uisp_id: Optional[StrictStr] = Field(default=None, description="The UUID used to indentify this device in UISP (if applicable)")
    node: AccessPointNode
    __properties: ClassVar[List[str]] = ["id", "latitude", "longitude", "altitude", "links_from", "links_to", "name", "status", "install_date", "abandon_date", "notes", "uisp_id", "node"]

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
        """Create an instance of Device from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "latitude",
            "longitude",
            "altitude",
            "links_from",
            "links_to",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in links_from (list)
        _items = []
        if self.links_from:
            for _item in self.links_from:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links_from'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links_to (list)
        _items = []
        if self.links_to:
            for _item in self.links_to:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links_to'] = _items
        # override the default output from pydantic by calling `to_dict()` of node
        if self.node:
            _dict['node'] = self.node.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if install_date (nullable) is None
        # and model_fields_set contains the field
        if self.install_date is None and "install_date" in self.model_fields_set:
            _dict['install_date'] = None

        # set to None if abandon_date (nullable) is None
        # and model_fields_set contains the field
        if self.abandon_date is None and "abandon_date" in self.model_fields_set:
            _dict['abandon_date'] = None

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
        """Create an instance of Device from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "altitude": obj.get("altitude"),
            "links_from": [AccessPointLinksFromInner.from_dict(_item) for _item in obj["links_from"]] if obj.get("links_from") is not None else None,
            "links_to": [AccessPointLinksFromInner.from_dict(_item) for _item in obj["links_to"]] if obj.get("links_to") is not None else None,
            "name": obj.get("name"),
            "status": obj.get("status"),
            "install_date": obj.get("install_date"),
            "abandon_date": obj.get("abandon_date"),
            "notes": obj.get("notes"),
            "uisp_id": obj.get("uisp_id"),
            "node": AccessPointNode.from_dict(obj["node"]) if obj.get("node") is not None else None
        })
        return _obj


