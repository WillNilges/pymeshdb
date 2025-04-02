# DisambiguateNumberSupportingData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exact_match_install** | [**InstallNestedRef**](InstallNestedRef.md) | An install  with the install number exactly matching the requested number, if that install has NOT had its install number recycled (or null if none exists) | 
**exact_match_recycled_install** | [**InstallNestedRef**](InstallNestedRef.md) | An install with the install number exactly matching the requested number, if that install HAS had its install number recycled (or null if none exists). When this field is non-null, exact_match_node will also be populated with that node | 
**exact_match_node** | [**DisambiguateNumberSupportingDataExactMatchNode**](DisambiguateNumberSupportingDataExactMatchNode.md) |  | 

## Example

```python
from pymeshdb.models.disambiguate_number_supporting_data import DisambiguateNumberSupportingData

# TODO update the JSON string below
json = "{}"
# create an instance of DisambiguateNumberSupportingData from a JSON string
disambiguate_number_supporting_data_instance = DisambiguateNumberSupportingData.from_json(json)
# print the JSON string representation of the object
print(DisambiguateNumberSupportingData.to_json())

# convert the object into a dict
disambiguate_number_supporting_data_dict = disambiguate_number_supporting_data_instance.to_dict()
# create an instance of DisambiguateNumberSupportingData from a dict
disambiguate_number_supporting_data_from_dict = DisambiguateNumberSupportingData.from_dict(disambiguate_number_supporting_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


