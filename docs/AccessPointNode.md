# AccessPointNode

The logical node this Device is located within. This node's network_number field corresponds to the static IP address and OSPF ID of this device or the DHCP range it receives an address from. The network number is also usually found in the device name

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**network_number** | **int** |  | [optional] 

## Example

```python
from pymeshdb.models.access_point_node import AccessPointNode

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPointNode from a JSON string
access_point_node_instance = AccessPointNode.from_json(json)
# print the JSON string representation of the object
print(AccessPointNode.to_json())

# convert the object into a dict
access_point_node_dict = access_point_node_instance.to_dict()
# create an instance of AccessPointNode from a dict
access_point_node_from_dict = AccessPointNode.from_dict(access_point_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


