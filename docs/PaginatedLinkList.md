# PaginatedLinkList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Link]**](Link.md) |  | 

## Example

```python
from pymeshdb.models.paginated_link_list import PaginatedLinkList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedLinkList from a JSON string
paginated_link_list_instance = PaginatedLinkList.from_json(json)
# print the JSON string representation of the object
print(PaginatedLinkList.to_json())

# convert the object into a dict
paginated_link_list_dict = paginated_link_list_instance.to_dict()
# create an instance of PaginatedLinkList from a dict
paginated_link_list_from_dict = PaginatedLinkList.from_dict(paginated_link_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


