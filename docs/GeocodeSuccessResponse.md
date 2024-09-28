# GeocodeSuccessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bin** | **int** |  | 
**latitude** | **float** |  | 
**longitude** | **float** |  | 
**altitude** | **float** |  | [optional] 

## Example

```python
from pymeshdb.models.geocode_success_response import GeocodeSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GeocodeSuccessResponse from a JSON string
geocode_success_response_instance = GeocodeSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(GeocodeSuccessResponse.to_json())

# convert the object into a dict
geocode_success_response_dict = geocode_success_response_instance.to_dict()
# create an instance of GeocodeSuccessResponse from a dict
geocode_success_response_from_dict = GeocodeSuccessResponse.from_dict(geocode_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


