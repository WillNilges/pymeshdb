# PatchedDevice

A  ModelSerializer MixIn which sets `NestedKeyObjectRelatedField` as the default field class to use for the foreign key fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**latitude** | **float** | Approximate Device latitude in decimal degrees (this is read through from the attached Node object, not stored separately) | [optional] [readonly] 
**longitude** | **float** | Approximate Device longitude in decimal degrees (this is read through from the attached Node object, not stored separately) | [optional] [readonly] 
**altitude** | **float** | Approximate Device altitude in \&quot;absolute\&quot; meters above mean sea level (this is read through from the attached Node object, not stored separately) | [optional] [readonly] 
**links_from** | [**List[AccessPointLinksFromInner]**](AccessPointLinksFromInner.md) |  | [optional] [readonly] 
**links_to** | [**List[AccessPointLinksFromInner]**](AccessPointLinksFromInner.md) |  | [optional] [readonly] 
**name** | **str** | The name of this device, usually configured as the hostname in the device firmware, usually in the format nycmesh-xxxx-yyyy-zzzz, where xxxx is the network number for the node this device is located at, yyyy is the type of the device, and zzzz is the network number of the other side of the link this device creates (if applicable) | [optional] 
**status** | [**Status432Enum**](Status432Enum.md) | The current status of this device  * &#x60;Inactive&#x60; - Inactive * &#x60;Active&#x60; - Active * &#x60;Potential&#x60; - Potential | [optional] 
**install_date** | **date** | The date this device first became active on the mesh | [optional] 
**abandon_date** | **date** | The this device was abandoned, unplugged, or removed from service | [optional] 
**notes** | **str** | A free-form text description of this Device, to track any additional information. For imported Devices, this starts with a formatted block of information about the import processand original data. However this structure can be changed by admins at any time and should not be relied onby automated systems.  | [optional] 
**uisp_id** | **str** | The UUID used to indentify this device in UISP (if applicable) | [optional] 
**node** | [**AccessPointNode**](AccessPointNode.md) |  | [optional] 

## Example

```python
from pymeshdb.models.patched_device import PatchedDevice

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedDevice from a JSON string
patched_device_instance = PatchedDevice.from_json(json)
# print the JSON string representation of the object
print(PatchedDevice.to_json())

# convert the object into a dict
patched_device_dict = patched_device_instance.to_dict()
# create an instance of PatchedDevice from a dict
patched_device_from_dict = PatchedDevice.from_dict(patched_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


