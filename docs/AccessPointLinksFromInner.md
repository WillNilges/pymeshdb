# AccessPointLinksFromInner

A reference to a Link object, via one or more of the following keys: ['id']

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from pymeshdb.models.access_point_links_from_inner import AccessPointLinksFromInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPointLinksFromInner from a JSON string
access_point_links_from_inner_instance = AccessPointLinksFromInner.from_json(json)
# print the JSON string representation of the object
print(AccessPointLinksFromInner.to_json())

# convert the object into a dict
access_point_links_from_inner_dict = access_point_links_from_inner_instance.to_dict()
# create an instance of AccessPointLinksFromInner from a dict
access_point_links_from_inner_from_dict = AccessPointLinksFromInner.from_dict(access_point_links_from_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


