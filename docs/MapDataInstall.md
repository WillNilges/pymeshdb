# MapDataInstall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | [readonly] 
**status** | **str** |  | [readonly] 
**coordinates** | **List[float]** |  | [readonly] 
**request_date** | **int** |  | 
**install_date** | **int** |  | 
**roof_access** | **bool** |  | 
**notes** | **str** |  | [readonly] 
**panoramas** | **List[str]** |  | [readonly] 

## Example

```python
from pymeshdb.models.map_data_install import MapDataInstall

# TODO update the JSON string below
json = "{}"
# create an instance of MapDataInstall from a JSON string
map_data_install_instance = MapDataInstall.from_json(json)
# print the JSON string representation of the object
print(MapDataInstall.to_json())

# convert the object into a dict
map_data_install_dict = map_data_install_instance.to_dict()
# create an instance of MapDataInstall from a dict
map_data_install_from_dict = MapDataInstall.from_dict(map_data_install_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


