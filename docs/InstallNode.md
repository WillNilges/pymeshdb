# InstallNode

The node this install is associated with. This node's network_number field corresponds to the static IP address and OSPF ID of the router this install utilizes, the DHCP range it receives an address from, etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**network_number** | **int** |  | [optional] 

## Example

```python
from pymeshdb.models.install_node import InstallNode

# TODO update the JSON string below
json = "{}"
# create an instance of InstallNode from a JSON string
install_node_instance = InstallNode.from_json(json)
# print the JSON string representation of the object
print(InstallNode.to_json())

# convert the object into a dict
install_node_dict = install_node_instance.to_dict()
# create an instance of InstallNode from a dict
install_node_from_dict = InstallNode.from_dict(install_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


