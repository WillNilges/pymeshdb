# BuildingPrimaryNode

The primary node for this Building, for cases where it has more than one. This is the node bearing the network number that the building is collquially referred to by volunteers and is usually the first NN held by any equipment on the building. If present, this must also be included in nodes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**network_number** | **int** |  | [optional] 

## Example

```python
from pymeshdb.models.building_primary_node import BuildingPrimaryNode

# TODO update the JSON string below
json = "{}"
# create an instance of BuildingPrimaryNode from a JSON string
building_primary_node_instance = BuildingPrimaryNode.from_json(json)
# print the JSON string representation of the object
print(BuildingPrimaryNode.to_json())

# convert the object into a dict
building_primary_node_dict = building_primary_node_instance.to_dict()
# create an instance of BuildingPrimaryNode from a dict
building_primary_node_from_dict = BuildingPrimaryNode.from_dict(building_primary_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


