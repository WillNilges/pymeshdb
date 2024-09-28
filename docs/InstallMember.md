# InstallMember

The member this install is associated with

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from pymeshdb.models.install_member import InstallMember

# TODO update the JSON string below
json = "{}"
# create an instance of InstallMember from a JSON string
install_member_instance = InstallMember.from_json(json)
# print the JSON string representation of the object
print(InstallMember.to_json())

# convert the object into a dict
install_member_dict = install_member_instance.to_dict()
# create an instance of InstallMember from a dict
install_member_from_dict = InstallMember.from_dict(install_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


