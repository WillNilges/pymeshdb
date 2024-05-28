# PaginatedInstallList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Install]**](Install.md) |  | 

## Example

```python
from pymeshdb.models.paginated_install_list import PaginatedInstallList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedInstallList from a JSON string
paginated_install_list_instance = PaginatedInstallList.from_json(json)
# print the JSON string representation of the object
print(PaginatedInstallList.to_json())

# convert the object into a dict
paginated_install_list_dict = paginated_install_list_instance.to_dict()
# create an instance of PaginatedInstallList from a dict
paginated_install_list_from_dict = PaginatedInstallList.from_dict(paginated_install_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


