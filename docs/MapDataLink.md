# MapDataLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **int** |  | [readonly] 
**to** | **int** |  | [readonly] 
**status** | **str** |  | [readonly] 
**install_date** | **int** |  | 

## Example

```python
from pymeshdb.models.map_data_link import MapDataLink

# TODO update the JSON string below
json = "{}"
# create an instance of MapDataLink from a JSON string
map_data_link_instance = MapDataLink.from_json(json)
# print the JSON string representation of the object
print(MapDataLink.to_json())

# convert the object into a dict
map_data_link_dict = map_data_link_instance.to_dict()
# create an instance of MapDataLink from a dict
map_data_link_from_dict = MapDataLink.from_dict(map_data_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


