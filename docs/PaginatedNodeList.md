# PaginatedNodeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Node]**](Node.md) |  | 

## Example

```python
from pymeshdb.models.paginated_node_list import PaginatedNodeList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedNodeList from a JSON string
paginated_node_list_instance = PaginatedNodeList.from_json(json)
# print the JSON string representation of the object
print(PaginatedNodeList.to_json())

# convert the object into a dict
paginated_node_list_dict = paginated_node_list_instance.to_dict()
# create an instance of PaginatedNodeList from a dict
paginated_node_list_from_dict = PaginatedNodeList.from_dict(paginated_node_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


