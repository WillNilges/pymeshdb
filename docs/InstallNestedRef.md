# InstallNestedRef

A  ModelSerializer MixIn which sets `NestedKeyObjectRelatedField` as the default field class to use for the foreign key fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**install_number** | **int** |  | [readonly] 
**id** | **str** |  | [readonly] 
**node** | [**InstallNode**](InstallNode.md) |  | [optional] 

## Example

```python
from pymeshdb.models.install_nested_ref import InstallNestedRef

# TODO update the JSON string below
json = "{}"
# create an instance of InstallNestedRef from a JSON string
install_nested_ref_instance = InstallNestedRef.from_json(json)
# print the JSON string representation of the object
print(InstallNestedRef.to_json())

# convert the object into a dict
install_nested_ref_dict = install_nested_ref_instance.to_dict()
# create an instance of InstallNestedRef from a dict
install_nested_ref_from_dict = InstallNestedRef.from_dict(install_nested_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


