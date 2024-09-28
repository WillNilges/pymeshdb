# NodeDevicesInner

A reference to a Device object, via one or more of the following keys: ['id']

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from pymeshdb.models.node_devices_inner import NodeDevicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of NodeDevicesInner from a JSON string
node_devices_inner_instance = NodeDevicesInner.from_json(json)
# print the JSON string representation of the object
print(NodeDevicesInner.to_json())

# convert the object into a dict
node_devices_inner_dict = node_devices_inner_instance.to_dict()
# create an instance of NodeDevicesInner from a dict
node_devices_inner_from_dict = NodeDevicesInner.from_dict(node_devices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


