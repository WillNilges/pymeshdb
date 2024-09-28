# InstallBuilding

The building where the install is located. In the case of a structure with multiple buildings, this will be the building whose address makes sense for this install's unit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from pymeshdb.models.install_building import InstallBuilding

# TODO update the JSON string below
json = "{}"
# create an instance of InstallBuilding from a JSON string
install_building_instance = InstallBuilding.from_json(json)
# print the JSON string representation of the object
print(InstallBuilding.to_json())

# convert the object into a dict
install_building_dict = install_building_instance.to_dict()
# create an instance of InstallBuilding from a dict
install_building_from_dict = InstallBuilding.from_dict(install_building_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


