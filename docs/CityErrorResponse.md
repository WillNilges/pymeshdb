# CityErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | 

## Example

```python
from pymeshdb.models.city_error_response import CityErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CityErrorResponse from a JSON string
city_error_response_instance = CityErrorResponse.from_json(json)
# print the JSON string representation of the object
print(CityErrorResponse.to_json())

# convert the object into a dict
city_error_response_dict = city_error_response_instance.to_dict()
# create an instance of CityErrorResponse from a dict
city_error_response_from_dict = CityErrorResponse.from_dict(city_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


