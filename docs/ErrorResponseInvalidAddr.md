# ErrorResponseInvalidAddr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | 

## Example

```python
from pymeshdb.models.error_response_invalid_addr import ErrorResponseInvalidAddr

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponseInvalidAddr from a JSON string
error_response_invalid_addr_instance = ErrorResponseInvalidAddr.from_json(json)
# print the JSON string representation of the object
print(ErrorResponseInvalidAddr.to_json())

# convert the object into a dict
error_response_invalid_addr_dict = error_response_invalid_addr_instance.to_dict()
# create an instance of ErrorResponseInvalidAddr from a dict
error_response_invalid_addr_from_dict = ErrorResponseInvalidAddr.from_dict(error_response_invalid_addr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


