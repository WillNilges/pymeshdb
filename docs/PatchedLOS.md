# PatchedLOS

A  ModelSerializer MixIn which sets `NestedKeyObjectRelatedField` as the default field class to use for the foreign key fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**analysis_date** | **date** | The date we conducted the analysis that concluded this LOS exists. Important since new buildings might have been built which block the LOS after this date | [optional] 
**source** | [**SourceEnum**](SourceEnum.md) | The source of information that tells us this LOS exists  * &#x60;Human Annotated&#x60; - Human Annotated * &#x60;Existing Link&#x60; - Existing Link | [optional] 
**notes** | **str** | A free-form text description of this LOS, to track any additional information. | [optional] 
**from_building** | [**LOSFromBuilding**](LOSFromBuilding.md) |  | [optional] 
**to_building** | [**LOSFromBuilding**](LOSFromBuilding.md) |  | [optional] 

## Example

```python
from pymeshdb.models.patched_los import PatchedLOS

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedLOS from a JSON string
patched_los_instance = PatchedLOS.from_json(json)
# print the JSON string representation of the object
print(PatchedLOS.to_json())

# convert the object into a dict
patched_los_dict = patched_los_instance.to_dict()
# create an instance of PatchedLOS from a dict
patched_los_from_dict = PatchedLOS.from_dict(patched_los_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


