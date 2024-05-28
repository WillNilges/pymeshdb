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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from pymeshdb.models.status195_enum import Status195Enum
from typing import Optional, Set
from typing_extensions import Self

class PatchedInstall(BaseModel):
    """
    PatchedInstall
    """ # noqa: E501
    install_number: Optional[StrictInt] = None
    network_number: Optional[Annotated[int, Field(le=8192, strict=True, ge=-2147483648)]] = None
    status: Optional[Status195Enum] = Field(default=None, description="The current status of this install  * `Request Received` - Request Received * `Pending` - Pending * `Blocked` - Blocked * `Active` - Active * `Inactive` - Inactive * `Closed` - Closed * `NN Reassigned` - Nn Reassigned")
    ticket_id: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = Field(default=None, description="The ID of the OSTicket used to track communications with the member about this install")
    request_date: Optional[date] = Field(default=None, description="The date that this install request was received")
    install_date: Optional[date] = Field(default=None, description="The date this install was completed and deployed to the mesh")
    abandon_date: Optional[date] = Field(default=None, description="The date this install was abandoned, unplugged, or disassembled")
    unit: Optional[StrictStr] = Field(default=None, description="Line 2 of this install's mailing address")
    roof_access: Optional[StrictBool] = Field(default=False, description="True if the member indicated they had access to the roof when they submitted the join form")
    referral: Optional[StrictStr] = Field(default=None, description="The \"How did you hear about us?\" information provided to us when the member submitted the join form")
    notes: Optional[StrictStr] = Field(default=None, description="A free-form text description of this Install, to track any additional information. For Installs imported from the spreadsheet, this starts with a formatted block of information about the import process and original spreadsheet data. However this structure can be changed by admins at any time and should not be relied on by automated systems. ")
    diy: Optional[StrictBool] = Field(default=None, description="Was this install conducted by the member themselves? If not, it was done by a volunteer installer on their behalf")
    building: Optional[StrictInt] = Field(default=None, description="The building where the install is located. In the case of a structure with multiple buildings, this will be the building whose address makes sense for this install's unit.")
    member: Optional[StrictInt] = Field(default=None, description="The member this install is associated with")
    __properties: ClassVar[List[str]] = ["install_number", "network_number", "status", "ticket_id", "request_date", "install_date", "abandon_date", "unit", "roof_access", "referral", "notes", "diy", "building", "member"]

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
        """Create an instance of PatchedInstall from a JSON string"""
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
            "install_number",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if network_number (nullable) is None
        # and model_fields_set contains the field
        if self.network_number is None and "network_number" in self.model_fields_set:
            _dict['network_number'] = None

        # set to None if ticket_id (nullable) is None
        # and model_fields_set contains the field
        if self.ticket_id is None and "ticket_id" in self.model_fields_set:
            _dict['ticket_id'] = None

        # set to None if install_date (nullable) is None
        # and model_fields_set contains the field
        if self.install_date is None and "install_date" in self.model_fields_set:
            _dict['install_date'] = None

        # set to None if abandon_date (nullable) is None
        # and model_fields_set contains the field
        if self.abandon_date is None and "abandon_date" in self.model_fields_set:
            _dict['abandon_date'] = None

        # set to None if unit (nullable) is None
        # and model_fields_set contains the field
        if self.unit is None and "unit" in self.model_fields_set:
            _dict['unit'] = None

        # set to None if referral (nullable) is None
        # and model_fields_set contains the field
        if self.referral is None and "referral" in self.model_fields_set:
            _dict['referral'] = None

        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        # set to None if diy (nullable) is None
        # and model_fields_set contains the field
        if self.diy is None and "diy" in self.model_fields_set:
            _dict['diy'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedInstall from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "install_number": obj.get("install_number"),
            "network_number": obj.get("network_number"),
            "status": obj.get("status"),
            "ticket_id": obj.get("ticket_id"),
            "request_date": obj.get("request_date"),
            "install_date": obj.get("install_date"),
            "abandon_date": obj.get("abandon_date"),
            "unit": obj.get("unit"),
            "roof_access": obj.get("roof_access") if obj.get("roof_access") is not None else False,
            "referral": obj.get("referral"),
            "notes": obj.get("notes"),
            "diy": obj.get("diy"),
            "building": obj.get("building"),
            "member": obj.get("member")
        })
        return _obj


