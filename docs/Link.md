# Link

A  ModelSerializer MixIn which sets `NestedKeyObjectRelatedField` as the default field class to use for the foreign key fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**status** | [**LinkStatusEnum**](LinkStatusEnum.md) | The current status of this link  * &#x60;Inactive&#x60; - Inactive * &#x60;Planned&#x60; - Planned * &#x60;Active&#x60; - Active | 
**type** | [**LinkType**](LinkType.md) |  | [optional] 
**install_date** | **date** | The date this link was created | [optional] 
**abandon_date** | **date** | The date this link was powered off, disassembled, or abandoned | [optional] 
**description** | **str** | A short description of \&quot;where to where\&quot; this link connects in human readable language | [optional] 
**notes** | **str** | A free-form text description of this Link, to track any additional information. | [optional] 
**uisp_id** | **str** | The UUID used to indentify this link in UISP (if applicable) | [optional] 
**from_device** | [**LinkFromDevice**](LinkFromDevice.md) |  | 
**to_device** | [**LinkFromDevice**](LinkFromDevice.md) |  | 

## Example

```python
from pymeshdb.models.link import Link

# TODO update the JSON string below
json = "{}"
# create an instance of Link from a JSON string
link_instance = Link.from_json(json)
# print the JSON string representation of the object
print(Link.to_json())

# convert the object into a dict
link_dict = link_instance.to_dict()
# create an instance of Link from a dict
link_from_dict = Link.from_dict(link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


