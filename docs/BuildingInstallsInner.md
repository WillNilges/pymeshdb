# BuildingInstallsInner

A reference to a Install object, via one or more of the following keys: ['id', 'install_number']

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**install_number** | **int** |  | [optional] 

## Example

```python
from pymeshdb.models.building_installs_inner import BuildingInstallsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BuildingInstallsInner from a JSON string
building_installs_inner_instance = BuildingInstallsInner.from_json(json)
# print the JSON string representation of the object
print(BuildingInstallsInner.to_json())

# convert the object into a dict
building_installs_inner_dict = building_installs_inner_instance.to_dict()
# create an instance of BuildingInstallsInner from a dict
building_installs_inner_from_dict = BuildingInstallsInner.from_dict(building_installs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


