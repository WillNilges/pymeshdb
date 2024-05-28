# PaginatedQueryFormList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[QueryForm]**](QueryForm.md) |  | 

## Example

```python
from pymeshdb.models.paginated_query_form_list import PaginatedQueryFormList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedQueryFormList from a JSON string
paginated_query_form_list_instance = PaginatedQueryFormList.from_json(json)
# print the JSON string representation of the object
print(PaginatedQueryFormList.to_json())

# convert the object into a dict
paginated_query_form_list_dict = paginated_query_form_list_instance.to_dict()
# create an instance of PaginatedQueryFormList from a dict
paginated_query_form_list_from_dict = PaginatedQueryFormList.from_dict(paginated_query_form_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


