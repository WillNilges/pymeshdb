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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from pymeshdb.models.address_truth_sources_enum import AddressTruthSourcesEnum
from pymeshdb.models.building_installs_inner import BuildingInstallsInner
from pymeshdb.models.building_nodes_inner import BuildingNodesInner
from pymeshdb.models.building_primary_node import BuildingPrimaryNode
from typing import Optional, Set
from typing_extensions import Self

class Building(BaseModel):
    """
    A  ModelSerializer MixIn which sets `NestedKeyObjectRelatedField` as the default field class to use for the foreign key fields
    """ # noqa: E501
    id: StrictStr
    installs: List[BuildingInstallsInner]
    bin: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=0)]] = Field(default=None, description="NYC DOB Identifier for the structure containing this building")
    street_address: Optional[StrictStr] = Field(default=None, description="Line 1 only of the address of this building: i.e. <house num> <street>")
    city: Optional[StrictStr] = Field(default=None, description="The name of the borough this building is in for buildings within NYC, \"New York\" for Manhattan to match street addresses. The actual city name for anything outside NYC")
    state: Optional[StrictStr] = Field(default=None, description="The 2 letter abreviation of the US State this building is contained within, e.g. \"NY\" or \"NJ\"")
    zip_code: Optional[StrictStr] = Field(default=None, description="The five digit ZIP code this building is contained within")
    address_truth_sources: List[AddressTruthSourcesEnum] = Field(description="A list of strings that answers the question: How was the content of the street address, city, state, and ZIP fields determined? This is useful in understanding the level of validation applied to spreadsheet imported data. Possible values are: OSMNominatim, OSMNominatimZIPOnly, NYCPlanningLabs, PeliasStringParsing, ReverseGeocodeFromCoordinates, HumanEntry. Check the import script for details")
    latitude: Union[StrictFloat, StrictInt] = Field(description="Building latitude in decimal degrees")
    longitude: Union[StrictFloat, StrictInt] = Field(description="Building longitude in decimal degrees")
    altitude: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Building rooftop altitude in \"absolute\" meters above mean sea level")
    notes: Optional[StrictStr] = Field(default=None, description="A free-form text description of this building, to track any additional information. For Buidings imported from the spreadsheet, this starts with a formatted block of information about the import process and original spreadsheet data. However this structure can be changed by admins at any time and should not be relied on by automated systems. ")
    panoramas: Optional[List[Annotated[str, Field(strict=True, max_length=200)]]] = Field(default=None, description="Panoramas taken from the roof of this Building")
    primary_node: Optional[BuildingPrimaryNode] = None
    nodes: Optional[List[BuildingNodesInner]] = Field(default=None, description="All nodes located on the same structure (i.e. a discrete man-made place identified by the same BIN) that this Building is located within.")
    __properties: ClassVar[List[str]] = ["id", "installs", "bin", "street_address", "city", "state", "zip_code", "address_truth_sources", "latitude", "longitude", "altitude", "notes", "panoramas", "primary_node", "nodes"]

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
        """Create an instance of Building from a JSON string"""
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
            "id",
            "installs",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in installs (list)
        _items = []
        if self.installs:
            for _item in self.installs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['installs'] = _items
        # override the default output from pydantic by calling `to_dict()` of primary_node
        if self.primary_node:
            _dict['primary_node'] = self.primary_node.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in nodes (list)
        _items = []
        if self.nodes:
            for _item in self.nodes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['nodes'] = _items
        # set to None if bin (nullable) is None
        # and model_fields_set contains the field
        if self.bin is None and "bin" in self.model_fields_set:
            _dict['bin'] = None

        # set to None if street_address (nullable) is None
        # and model_fields_set contains the field
        if self.street_address is None and "street_address" in self.model_fields_set:
            _dict['street_address'] = None

        # set to None if city (nullable) is None
        # and model_fields_set contains the field
        if self.city is None and "city" in self.model_fields_set:
            _dict['city'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if zip_code (nullable) is None
        # and model_fields_set contains the field
        if self.zip_code is None and "zip_code" in self.model_fields_set:
            _dict['zip_code'] = None

        # set to None if altitude (nullable) is None
        # and model_fields_set contains the field
        if self.altitude is None and "altitude" in self.model_fields_set:
            _dict['altitude'] = None

        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        # set to None if panoramas (nullable) is None
        # and model_fields_set contains the field
        if self.panoramas is None and "panoramas" in self.model_fields_set:
            _dict['panoramas'] = None

        # set to None if primary_node (nullable) is None
        # and model_fields_set contains the field
        if self.primary_node is None and "primary_node" in self.model_fields_set:
            _dict['primary_node'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Building from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "installs": [BuildingInstallsInner.from_dict(_item) for _item in obj["installs"]] if obj.get("installs") is not None else None,
            "bin": obj.get("bin"),
            "street_address": obj.get("street_address"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "zip_code": obj.get("zip_code"),
            "address_truth_sources": obj.get("address_truth_sources"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "altitude": obj.get("altitude"),
            "notes": obj.get("notes"),
            "panoramas": obj.get("panoramas"),
            "primary_node": BuildingPrimaryNode.from_dict(obj["primary_node"]) if obj.get("primary_node") is not None else None,
            "nodes": [BuildingNodesInner.from_dict(_item) for _item in obj["nodes"]] if obj.get("nodes") is not None else None
        })
        return _obj


