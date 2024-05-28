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
from typing_extensions import Annotated
from pymeshdb.models.status432_enum import Status432Enum
from pymeshdb.models.type75b_enum import Type75bEnum
from typing import Optional, Set
from typing_extensions import Self

class PatchedSector(BaseModel):
    """
    PatchedSector
    """ # noqa: E501
    id: Optional[StrictInt] = None
    network_number: Optional[Annotated[int, Field(le=8192, strict=True, ge=-2147483648)]] = None
    links_from: Optional[List[StrictInt]] = None
    links_to: Optional[List[StrictInt]] = None
    name: Optional[StrictStr] = Field(default=None, description="The colloquial name of this node used among mesh volunteers, if applicable")
    model: Optional[StrictStr] = Field(default=None, description="The manufacturer model name of this device, e.g. OmniTik or LBEGen2")
    type: Optional[Type75bEnum] = Field(default=None, description="The general type of device that this is, the role it fills on the mesh. e.g. ap, ptp, station, etc. This lines up with the UISP 'role' property  * `ap` - Ap * `gateway` - Gateway * `gpon` - Gpon * `convertor` - Convertor * `other` - Other * `ptp` - Ptp * `router` - Router * `server` - Server * `station` - Station * `switch` - Switch * `ups` - Ups * `wireless` - Wireless * `homeWiFi` - Homewifi * `wirelessDevice` - Wirelessdevice")
    status: Optional[Status432Enum] = Field(default=None, description="The current status of this device  * `Inactive` - Inactive * `Active` - Active * `Potential` - Potential")
    latitude: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Approximate Device latitude in decimal degrees (this will match the attached Node object in most cases, but has been manually moved around in some cases to more accurately reflect the device location)")
    longitude: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Approximate Device longitude in decimal degrees (this will match the attached Node object in most cases, but has been manually moved around in some cases to more accurately reflect the device location)")
    altitude: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Approximate Device altitude in \"absolute\" meters above mean sea level (this will match the attached Node object in most cases, but has been manually moved around in some cases to more accurately reflect the device location)")
    install_date: Optional[date] = Field(default=None, description="The date this device first became active on the mesh")
    abandon_date: Optional[date] = Field(default=None, description="The this device was abandoned, unplugged, or removed from service")
    notes: Optional[StrictStr] = Field(default=None, description="A free-form text description of this Device, to track any additional information. For imported Devices, this starts with a formatted block of information about the import processand original data. However this structure can be changed by admins at any time and should not be relied onby automated systems. ")
    uisp_id: Optional[StrictStr] = Field(default=None, description="The UUID used to indentify this device in UISP (if applicable)")
    ssid: Optional[StrictStr] = Field(default=None, description="The SSID being broadcast by this device")
    ip_address: Optional[StrictStr] = Field(default=None, description="The IP address of this device within the 10.x network")
    radius: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="The radius to display this sector on the map (in km)")
    azimuth: Optional[Annotated[int, Field(le=360, strict=True, ge=0)]] = Field(default=None, description="The compass heading that this sector is pointed towards")
    width: Optional[Annotated[int, Field(le=360, strict=True, ge=0)]] = Field(default=None, description="The approximate width of the beam this sector produces")
    __properties: ClassVar[List[str]] = ["id", "network_number", "links_from", "links_to", "name", "model", "type", "status", "latitude", "longitude", "altitude", "install_date", "abandon_date", "notes", "uisp_id", "ssid", "ip_address", "radius", "azimuth", "width"]

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
        """Create an instance of PatchedSector from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "id",
            "links_from",
            "links_to",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if altitude (nullable) is None
        # and model_fields_set contains the field
        if self.altitude is None and "altitude" in self.model_fields_set:
            _dict['altitude'] = None

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

        # set to None if ssid (nullable) is None
        # and model_fields_set contains the field
        if self.ssid is None and "ssid" in self.model_fields_set:
            _dict['ssid'] = None

        # set to None if ip_address (nullable) is None
        # and model_fields_set contains the field
        if self.ip_address is None and "ip_address" in self.model_fields_set:
            _dict['ip_address'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedSector from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "network_number": obj.get("network_number"),
            "links_from": obj.get("links_from"),
            "links_to": obj.get("links_to"),
            "name": obj.get("name"),
            "model": obj.get("model"),
            "type": obj.get("type"),
            "status": obj.get("status"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "altitude": obj.get("altitude"),
            "install_date": obj.get("install_date"),
            "abandon_date": obj.get("abandon_date"),
            "notes": obj.get("notes"),
            "uisp_id": obj.get("uisp_id"),
            "ssid": obj.get("ssid"),
            "ip_address": obj.get("ip_address"),
            "radius": obj.get("radius"),
            "azimuth": obj.get("azimuth"),
            "width": obj.get("width")
        })
        return _obj


