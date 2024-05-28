# NetworkNumberAssignmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | 
**install_number** | **int** |  | 

## Example

```python
from pymeshdb.models.network_number_assignment_request import NetworkNumberAssignmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkNumberAssignmentRequest from a JSON string
network_number_assignment_request_instance = NetworkNumberAssignmentRequest.from_json(json)
# print the JSON string representation of the object
print(NetworkNumberAssignmentRequest.to_json())

# convert the object into a dict
network_number_assignment_request_dict = network_number_assignment_request_instance.to_dict()
# create an instance of NetworkNumberAssignmentRequest from a dict
network_number_assignment_request_from_dict = NetworkNumberAssignmentRequest.from_dict(network_number_assignment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


