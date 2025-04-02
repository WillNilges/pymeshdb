# JoinFormSuccessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | 
**building_id** | **str** |  | 
**member_id** | **str** |  | 
**install_id** | **str** |  | 
**install_number** | **int** |  | 
**member_exists** | **bool** |  | 
**changed_info** | **Dict[str, object]** |  | 

## Example

```python
from pymeshdb.models.join_form_success_response import JoinFormSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JoinFormSuccessResponse from a JSON string
join_form_success_response_instance = JoinFormSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(JoinFormSuccessResponse.to_json())

# convert the object into a dict
join_form_success_response_dict = join_form_success_response_instance.to_dict()
# create an instance of JoinFormSuccessResponse from a dict
join_form_success_response_from_dict = JoinFormSuccessResponse.from_dict(join_form_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


