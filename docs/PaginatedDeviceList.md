# PaginatedDeviceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Device]**](Device.md) |  | 

## Example

```python
from pymeshdb.models.paginated_device_list import PaginatedDeviceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDeviceList from a JSON string
paginated_device_list_instance = PaginatedDeviceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDeviceList.to_json())

# convert the object into a dict
paginated_device_list_dict = paginated_device_list_instance.to_dict()
# create an instance of PaginatedDeviceList from a dict
paginated_device_list_from_dict = PaginatedDeviceList.from_dict(paginated_device_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


