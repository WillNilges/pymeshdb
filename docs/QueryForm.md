# QueryForm

Objects which approximate the CSV output from the legacy docs query form. These approximately correspond to the spreadsheet row format, by flattening attributes across many models into a single JSON object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**install_number** | **int** |  | [readonly] 
**street_address** | **str** |  | 
**unit** | **str** | Line 2 of this install&#39;s mailing address | [optional] 
**city** | **str** |  | 
**state** | **str** |  | 
**zip_code** | **str** |  | 
**name** | **str** |  | 
**phone_number** | **str** |  | 
**additional_phone_numbers** | **List[str]** |  | 
**primary_email_address** | **str** |  | 
**stripe_email_address** | **str** |  | 
**additional_email_addresses** | **List[str]** |  | 
**notes** | **str** |  | [readonly] 
**network_number** | **int** |  | 
**network_number_status** | **str** |  | 
**status** | [**Status4ffEnum**](Status4ffEnum.md) | The current status of this install  * &#x60;Request Received&#x60; - Request Received * &#x60;Pending&#x60; - Pending * &#x60;Blocked&#x60; - Blocked * &#x60;Active&#x60; - Active * &#x60;Inactive&#x60; - Inactive * &#x60;Closed&#x60; - Closed * &#x60;NN Reassigned&#x60; - NN Reassigned | 

## Example

```python
from pymeshdb.models.query_form import QueryForm

# TODO update the JSON string below
json = "{}"
# create an instance of QueryForm from a JSON string
query_form_instance = QueryForm.from_json(json)
# print the JSON string representation of the object
print(QueryForm.to_json())

# convert the object into a dict
query_form_dict = query_form_instance.to_dict()
# create an instance of QueryForm from a dict
query_form_from_dict = QueryForm.from_dict(query_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


