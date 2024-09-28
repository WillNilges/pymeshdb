# BuildingNodesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**network_number** | **int** |  | [optional] 

## Example

```python
from pymeshdb.models.building_nodes_inner import BuildingNodesInner

# TODO update the JSON string below
json = "{}"
# create an instance of BuildingNodesInner from a JSON string
building_nodes_inner_instance = BuildingNodesInner.from_json(json)
# print the JSON string representation of the object
print(BuildingNodesInner.to_json())

# convert the object into a dict
building_nodes_inner_dict = building_nodes_inner_instance.to_dict()
# create an instance of BuildingNodesInner from a dict
building_nodes_inner_from_dict = BuildingNodesInner.from_dict(building_nodes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


