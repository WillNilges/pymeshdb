# JoinFormRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | 
**street_address** | **str** |  | 
**city** | **str** |  | 
**state** | **str** |  | 
**zip** | **int** |  | 
**apartment** | **str** |  | 
**roof_access** | **bool** |  | 
**referral** | **str** |  | 
**ncl** | **bool** |  | 

## Example

```python
from pymeshdb.models.join_form_request import JoinFormRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JoinFormRequest from a JSON string
join_form_request_instance = JoinFormRequest.from_json(json)
# print the JSON string representation of the object
print(JoinFormRequest.to_json())

# convert the object into a dict
join_form_request_dict = join_form_request_instance.to_dict()
# create an instance of JoinFormRequest from a dict
join_form_request_from_dict = JoinFormRequest.from_dict(join_form_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


