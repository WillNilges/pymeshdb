# LinkType

The technology used for this link 5Ghz, 60Ghz, fiber, etc.  * `5 GHz` - 5 GHz * `24 GHz` - 24 GHz * `60 GHz` - 60 GHz * `70-80 GHz` - 70-80 GHz * `VPN` - VPN * `Fiber` - Fiber * `Ethernet` - Ethernet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from pymeshdb.models.link_type import LinkType

# TODO update the JSON string below
json = "{}"
# create an instance of LinkType from a JSON string
link_type_instance = LinkType.from_json(json)
# print the JSON string representation of the object
print(LinkType.to_json())

# convert the object into a dict
link_type_dict = link_type_instance.to_dict()
# create an instance of LinkType from a dict
link_type_from_dict = LinkType.from_dict(link_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


