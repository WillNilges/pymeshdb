# coding: utf-8

"""
    MeshDB Data API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class MapDataSector(BaseModel):
    """
    MapDataSector
    """ # noqa: E501
    node_id: Optional[StrictInt] = Field(alias="nodeId")
    radius: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="The radius to display this sector on the map (in km)")
    azimuth: Annotated[int, Field(le=360, strict=True, ge=0)] = Field(description="The compass heading that this sector is pointed towards")
    width: Annotated[int, Field(le=360, strict=True, ge=0)] = Field(description="The approximate width of the beam this sector produces")
    status: StrictStr
    install_date: StrictInt = Field(alias="installDate")
    __properties: ClassVar[List[str]] = ["nodeId", "radius", "azimuth", "width", "status", "installDate"]

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
        """Create an instance of MapDataSector from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "node_id",
            "status",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if node_id (nullable) is None
        # and model_fields_set contains the field
        if self.node_id is None and "node_id" in self.model_fields_set:
            _dict['nodeId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MapDataSector from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "nodeId": obj.get("nodeId"),
            "radius": obj.get("radius"),
            "azimuth": obj.get("azimuth"),
            "width": obj.get("width"),
            "status": obj.get("status"),
            "installDate": obj.get("installDate")
        })
        return _obj


