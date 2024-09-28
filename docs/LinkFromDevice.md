# LinkFromDevice

The device on one side of this network link, from/to are not meaningful except to disambiguate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from pymeshdb.models.link_from_device import LinkFromDevice

# TODO update the JSON string below
json = "{}"
# create an instance of LinkFromDevice from a JSON string
link_from_device_instance = LinkFromDevice.from_json(json)
# print the JSON string representation of the object
print(LinkFromDevice.to_json())

# convert the object into a dict
link_from_device_dict = link_from_device_instance.to_dict()
# create an instance of LinkFromDevice from a dict
link_from_device_from_dict = LinkFromDevice.from_dict(link_from_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


