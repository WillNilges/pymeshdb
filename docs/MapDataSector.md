# MapDataSector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **int** |  | [readonly] 
**radius** | **float** | The radius to display this sector on the map (in km) | 
**azimuth** | **int** | The compass heading that this sector is pointed towards | 
**width** | **int** | The approximate width of the beam this sector produces | 
**status** | **str** |  | [readonly] 
**install_date** | **int** |  | 

## Example

```python
from pymeshdb.models.map_data_sector import MapDataSector

# TODO update the JSON string below
json = "{}"
# create an instance of MapDataSector from a JSON string
map_data_sector_instance = MapDataSector.from_json(json)
# print the JSON string representation of the object
print(MapDataSector.to_json())

# convert the object into a dict
map_data_sector_dict = map_data_sector_instance.to_dict()
# create an instance of MapDataSector from a dict
map_data_sector_from_dict = MapDataSector.from_dict(map_data_sector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


