# KioskData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street_address** | **str** |  | 
**type** | **str** |  | 
**id** | **int** |  | 
**coordinates** | **List[float]** |  | 
**status** | **str** |  | [optional] 

## Example

```python
from pymeshdb.models.kiosk_data import KioskData

# TODO update the JSON string below
json = "{}"
# create an instance of KioskData from a JSON string
kiosk_data_instance = KioskData.from_json(json)
# print the JSON string representation of the object
print(KioskData.to_json())

# convert the object into a dict
kiosk_data_dict = kiosk_data_instance.to_dict()
# create an instance of KioskData from a dict
kiosk_data_from_dict = KioskData.from_dict(kiosk_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


