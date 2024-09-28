# AccessPoint

A  ModelSerializer MixIn which sets `NestedKeyObjectRelatedField` as the default field class to use for the foreign key fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**links_from** | [**List[AccessPointLinksFromInner]**](AccessPointLinksFromInner.md) |  | [readonly] 
**links_to** | [**List[AccessPointLinksFromInner]**](AccessPointLinksFromInner.md) |  | [readonly] 
**name** | **str** | The name of this device, usually configured as the hostname in the device firmware, usually in the format nycmesh-xxxx-yyyy-zzzz, where xxxx is the network number for the node this device is located at, yyyy is the type of the device, and zzzz is the network number of the other side of the link this device creates (if applicable) | [optional] 
**status** | [**Status432Enum**](Status432Enum.md) | The current status of this device  * &#x60;Inactive&#x60; - Inactive * &#x60;Active&#x60; - Active * &#x60;Potential&#x60; - Potential | 
**install_date** | **date** | The date this device first became active on the mesh | [optional] 
**abandon_date** | **date** | The this device was abandoned, unplugged, or removed from service | [optional] 
**notes** | **str** | A free-form text description of this Device, to track any additional information. For imported Devices, this starts with a formatted block of information about the import processand original data. However this structure can be changed by admins at any time and should not be relied onby automated systems.  | [optional] 
**uisp_id** | **str** | The UUID used to indentify this device in UISP (if applicable) | [optional] 
**latitude** | **float** | Approximate AP latitude in decimal degrees (this will match the attached Node object in most cases, but has been manually moved around in some cases to more accurately reflect the device location) | 
**longitude** | **float** | Approximate AP longitude in decimal degrees (this will match the attached Node object in most cases, but has been manually moved around in some cases to more accurately reflect the device location) | 
**altitude** | **float** | Approximate AP altitude in \&quot;absolute\&quot; meters above mean sea level (this will match the attached Node object in most cases, but has been manually moved around in some cases to more accurately reflect the device location) | [optional] 
**node** | [**AccessPointNode**](AccessPointNode.md) |  | 

## Example

```python
from pymeshdb.models.access_point import AccessPoint

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPoint from a JSON string
access_point_instance = AccessPoint.from_json(json)
# print the JSON string representation of the object
print(AccessPoint.to_json())

# convert the object into a dict
access_point_dict = access_point_instance.to_dict()
# create an instance of AccessPoint from a dict
access_point_from_dict = AccessPoint.from_dict(access_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


