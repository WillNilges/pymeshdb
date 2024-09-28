# ErrorResponseMissingFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **Dict[str, object]** |  | 

## Example

```python
from pymeshdb.models.error_response_missing_fields import ErrorResponseMissingFields

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponseMissingFields from a JSON string
error_response_missing_fields_instance = ErrorResponseMissingFields.from_json(json)
# print the JSON string representation of the object
print(ErrorResponseMissingFields.to_json())

# convert the object into a dict
error_response_missing_fields_dict = error_response_missing_fields_instance.to_dict()
# create an instance of ErrorResponseMissingFields from a dict
error_response_missing_fields_from_dict = ErrorResponseMissingFields.from_dict(error_response_missing_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


