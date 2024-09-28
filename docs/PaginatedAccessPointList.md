# PaginatedAccessPointList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[AccessPoint]**](AccessPoint.md) |  | 

## Example

```python
from pymeshdb.models.paginated_access_point_list import PaginatedAccessPointList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAccessPointList from a JSON string
paginated_access_point_list_instance = PaginatedAccessPointList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAccessPointList.to_json())

# convert the object into a dict
paginated_access_point_list_dict = paginated_access_point_list_instance.to_dict()
# create an instance of PaginatedAccessPointList from a dict
paginated_access_point_list_from_dict = PaginatedAccessPointList.from_dict(paginated_access_point_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


