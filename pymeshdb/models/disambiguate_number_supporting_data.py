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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from pymeshdb.models.disambiguate_number_supporting_data_exact_match_node import DisambiguateNumberSupportingDataExactMatchNode
from pymeshdb.models.install_nested_ref import InstallNestedRef
from typing import Optional, Set
from typing_extensions import Self

class DisambiguateNumberSupportingData(BaseModel):
    """
    DisambiguateNumberSupportingData
    """ # noqa: E501
    exact_match_install: InstallNestedRef = Field(description="An install  with the install number exactly matching the requested number, if that install has NOT had its install number recycled (or null if none exists)")
    exact_match_recycled_install: InstallNestedRef = Field(description="An install with the install number exactly matching the requested number, if that install HAS had its install number recycled (or null if none exists). When this field is non-null, exact_match_node will also be populated with that node")
    exact_match_node: DisambiguateNumberSupportingDataExactMatchNode
    __properties: ClassVar[List[str]] = ["exact_match_install", "exact_match_recycled_install", "exact_match_node"]

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
        """Create an instance of DisambiguateNumberSupportingData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of exact_match_install
        if self.exact_match_install:
            _dict['exact_match_install'] = self.exact_match_install.to_dict()
        # override the default output from pydantic by calling `to_dict()` of exact_match_recycled_install
        if self.exact_match_recycled_install:
            _dict['exact_match_recycled_install'] = self.exact_match_recycled_install.to_dict()
        # override the default output from pydantic by calling `to_dict()` of exact_match_node
        if self.exact_match_node:
            _dict['exact_match_node'] = self.exact_match_node.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DisambiguateNumberSupportingData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "exact_match_install": InstallNestedRef.from_dict(obj["exact_match_install"]) if obj.get("exact_match_install") is not None else None,
            "exact_match_recycled_install": InstallNestedRef.from_dict(obj["exact_match_recycled_install"]) if obj.get("exact_match_recycled_install") is not None else None,
            "exact_match_node": DisambiguateNumberSupportingDataExactMatchNode.from_dict(obj["exact_match_node"]) if obj.get("exact_match_node") is not None else None
        })
        return _obj


