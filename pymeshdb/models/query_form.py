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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pymeshdb.models.status195_enum import Status195Enum
from typing import Optional, Set
from typing_extensions import Self

class QueryForm(BaseModel):
    """
    Objects which approximate the CSV output from the legacy docs query form. These approximately correspond to the spreadsheet row format, by flattening attributes across many models into a single JSON object
    """ # noqa: E501
    install_number: StrictInt
    street_address: StrictStr
    unit: Optional[StrictStr] = Field(default=None, description="Line 2 of this install's mailing address")
    city: StrictStr
    state: StrictStr
    zip_code: StrictStr
    name: StrictStr
    phone_number: StrictStr
    primary_email_address: StrictStr
    stripe_email_address: StrictStr
    additional_email_addresses: List[StrictStr]
    notes: StrictStr
    network_number: Optional[StrictInt]
    status: Status195Enum = Field(description="The current status of this install  * `Request Received` - Request Received * `Pending` - Pending * `Blocked` - Blocked * `Active` - Active * `Inactive` - Inactive * `Closed` - Closed * `NN Reassigned` - Nn Reassigned")
    __properties: ClassVar[List[str]] = ["install_number", "street_address", "unit", "city", "state", "zip_code", "name", "phone_number", "primary_email_address", "stripe_email_address", "additional_email_addresses", "notes", "network_number", "status"]

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
        """Create an instance of QueryForm from a JSON string"""
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
            "install_number",
            "notes",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if unit (nullable) is None
        # and model_fields_set contains the field
        if self.unit is None and "unit" in self.model_fields_set:
            _dict['unit'] = None

        # set to None if network_number (nullable) is None
        # and model_fields_set contains the field
        if self.network_number is None and "network_number" in self.model_fields_set:
            _dict['network_number'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QueryForm from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "install_number": obj.get("install_number"),
            "street_address": obj.get("street_address"),
            "unit": obj.get("unit"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "zip_code": obj.get("zip_code"),
            "name": obj.get("name"),
            "phone_number": obj.get("phone_number"),
            "primary_email_address": obj.get("primary_email_address"),
            "stripe_email_address": obj.get("stripe_email_address"),
            "additional_email_addresses": obj.get("additional_email_addresses"),
            "notes": obj.get("notes"),
            "network_number": obj.get("network_number"),
            "status": obj.get("status")
        })
        return _obj

