# NodeEdit

A  ModelSerializer MixIn which sets `NestedKeyObjectRelatedField` as the default field class to use for the foreign key fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**buildings** | [**List[NodeBuildingsInner]**](NodeBuildingsInner.md) |  | [readonly] 
**devices** | [**List[NodeDevicesInner]**](NodeDevicesInner.md) |  | [readonly] 
**installs** | [**List[BuildingInstallsInner]**](BuildingInstallsInner.md) |  | [readonly] 
**network_number** | **int** |  | [readonly] 
**name** | **str** | The colloquial name of this node used among mesh volunteers, if applicable | [optional] 
**status** | [**Status2a6Enum**](Status2a6Enum.md) | The current status of this Node  * &#x60;Inactive&#x60; - Inactive * &#x60;Active&#x60; - Active * &#x60;Planned&#x60; - Planned | 
**type** | [**Type1bfEnum**](Type1bfEnum.md) | The type of node this is, controls the icon used on the network map  * &#x60;Standard&#x60; - Standard * &#x60;Hub&#x60; - Hub * &#x60;Supernode&#x60; - Supernode * &#x60;POP&#x60; - POP * &#x60;AP&#x60; - AP * &#x60;Remote&#x60; - Remote | [optional] 
**latitude** | **float** | Approximate Node latitude in decimal degrees (this will match one of the attached Building objects in most cases, but has been manually moved around in some cases to more accurately reflect node location) | 
**longitude** | **float** | Approximate Node longitude in decimal degrees (this will match one of the attached Building objects in most cases, but has been manually moved around in some cases to more accurately reflect node location) | 
**altitude** | **float** | Approximate Node altitude in \&quot;absolute\&quot; meters above mean sea level (this will match one of the attached Building objects in most cases, but has been manually moved around in some cases to more accurately reflect node location) | [optional] 
**install_date** | **date** | The date the first Install or Device associated with this Node became active on the mesh | [optional] 
**abandon_date** | **date** | The date the last Install or Device associated with this Node was abandoned, unplugged, or removed from service | [optional] 
**notes** | **str** | A free-form text description of this Node, to track any additional information. For Nodes imported from the spreadsheet, this starts with a formatted block of information about the import process and original spreadsheet data. However this structure can be changed by admins at any time and should not be relied on by automated systems.  | [optional] 

## Example

```python
from pymeshdb.models.node_edit import NodeEdit

# TODO update the JSON string below
json = "{}"
# create an instance of NodeEdit from a JSON string
node_edit_instance = NodeEdit.from_json(json)
# print the JSON string representation of the object
print(NodeEdit.to_json())

# convert the object into a dict
node_edit_dict = node_edit_instance.to_dict()
# create an instance of NodeEdit from a dict
node_edit_from_dict = NodeEdit.from_dict(node_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


