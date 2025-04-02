# DisambiguateNumberSuccessResponseResolvedNode

The node that we guess this number represents. This is an exact NN match if that node exists, otherwise we treat the input number as an install number and return the related node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**network_number** | **int** |  | [optional] 

## Example

```python
from pymeshdb.models.disambiguate_number_success_response_resolved_node import DisambiguateNumberSuccessResponseResolvedNode

# TODO update the JSON string below
json = "{}"
# create an instance of DisambiguateNumberSuccessResponseResolvedNode from a JSON string
disambiguate_number_success_response_resolved_node_instance = DisambiguateNumberSuccessResponseResolvedNode.from_json(json)
# print the JSON string representation of the object
print(DisambiguateNumberSuccessResponseResolvedNode.to_json())

# convert the object into a dict
disambiguate_number_success_response_resolved_node_dict = disambiguate_number_success_response_resolved_node_instance.to_dict()
# create an instance of DisambiguateNumberSuccessResponseResolvedNode from a dict
disambiguate_number_success_response_resolved_node_from_dict = DisambiguateNumberSuccessResponseResolvedNode.from_dict(disambiguate_number_success_response_resolved_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


