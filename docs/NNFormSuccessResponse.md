# NNFormSuccessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | 
**building_id** | **str** |  | 
**install_id** | **str** |  | 
**install_number** | **int** |  | 
**network_number** | **int** |  | 
**created** | **bool** |  | 

## Example

```python
from pymeshdb.models.nn_form_success_response import NNFormSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NNFormSuccessResponse from a JSON string
nn_form_success_response_instance = NNFormSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(NNFormSuccessResponse.to_json())

# convert the object into a dict
nn_form_success_response_dict = nn_form_success_response_instance.to_dict()
# create an instance of NNFormSuccessResponse from a dict
nn_form_success_response_from_dict = NNFormSuccessResponse.from_dict(nn_form_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


