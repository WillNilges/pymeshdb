# PaginatedBuildingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Building]**](Building.md) |  | 

## Example

```python
from pymeshdb.models.paginated_building_list import PaginatedBuildingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedBuildingList from a JSON string
paginated_building_list_instance = PaginatedBuildingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedBuildingList.to_json())

# convert the object into a dict
paginated_building_list_dict = paginated_building_list_instance.to_dict()
# create an instance of PaginatedBuildingList from a dict
paginated_building_list_from_dict = PaginatedBuildingList.from_dict(paginated_building_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


