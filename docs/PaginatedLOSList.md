# PaginatedLOSList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[LOS]**](LOS.md) |  | 

## Example

```python
from pymeshdb.models.paginated_los_list import PaginatedLOSList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedLOSList from a JSON string
paginated_los_list_instance = PaginatedLOSList.from_json(json)
# print the JSON string representation of the object
print(PaginatedLOSList.to_json())

# convert the object into a dict
paginated_los_list_dict = paginated_los_list_instance.to_dict()
# create an instance of PaginatedLOSList from a dict
paginated_los_list_from_dict = PaginatedLOSList.from_dict(paginated_los_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


