# NodeBuildingsInner

A reference to a Building object, via one or more of the following keys: ['id']

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from pymeshdb.models.node_buildings_inner import NodeBuildingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of NodeBuildingsInner from a JSON string
node_buildings_inner_instance = NodeBuildingsInner.from_json(json)
# print the JSON string representation of the object
print(NodeBuildingsInner.to_json())

# convert the object into a dict
node_buildings_inner_dict = node_buildings_inner_instance.to_dict()
# create an instance of NodeBuildingsInner from a dict
node_buildings_inner_from_dict = NodeBuildingsInner.from_dict(node_buildings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


