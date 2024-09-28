# ErrorResponseInternalFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | 

## Example

```python
from pymeshdb.models.error_response_internal_failure import ErrorResponseInternalFailure

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponseInternalFailure from a JSON string
error_response_internal_failure_instance = ErrorResponseInternalFailure.from_json(json)
# print the JSON string representation of the object
print(ErrorResponseInternalFailure.to_json())

# convert the object into a dict
error_response_internal_failure_dict = error_response_internal_failure_instance.to_dict()
# create an instance of ErrorResponseInternalFailure from a dict
error_response_internal_failure_from_dict = ErrorResponseInternalFailure.from_dict(error_response_internal_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


