# DisambiguateNumberSuccessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolved_node** | [**DisambiguateNumberSuccessResponseResolvedNode**](DisambiguateNumberSuccessResponseResolvedNode.md) |  | 
**supporting_data** | [**DisambiguateNumberSupportingData**](DisambiguateNumberSupportingData.md) |  | 

## Example

```python
from pymeshdb.models.disambiguate_number_success_response import DisambiguateNumberSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DisambiguateNumberSuccessResponse from a JSON string
disambiguate_number_success_response_instance = DisambiguateNumberSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(DisambiguateNumberSuccessResponse.to_json())

# convert the object into a dict
disambiguate_number_success_response_dict = disambiguate_number_success_response_instance.to_dict()
# create an instance of DisambiguateNumberSuccessResponse from a dict
disambiguate_number_success_response_from_dict = DisambiguateNumberSuccessResponse.from_dict(disambiguate_number_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


