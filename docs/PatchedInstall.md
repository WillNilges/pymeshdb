# PatchedInstall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**install_number** | **int** |  | [optional] [readonly] 
**network_number** | **int** |  | [optional] 
**status** | [**Status195Enum**](Status195Enum.md) | The current status of this install  * &#x60;Request Received&#x60; - Request Received * &#x60;Pending&#x60; - Pending * &#x60;Blocked&#x60; - Blocked * &#x60;Active&#x60; - Active * &#x60;Inactive&#x60; - Inactive * &#x60;Closed&#x60; - Closed * &#x60;NN Reassigned&#x60; - Nn Reassigned | [optional] 
**ticket_id** | **int** | The ID of the OSTicket used to track communications with the member about this install | [optional] 
**request_date** | **date** | The date that this install request was received | [optional] 
**install_date** | **date** | The date this install was completed and deployed to the mesh | [optional] 
**abandon_date** | **date** | The date this install was abandoned, unplugged, or disassembled | [optional] 
**unit** | **str** | Line 2 of this install&#39;s mailing address | [optional] 
**roof_access** | **bool** | True if the member indicated they had access to the roof when they submitted the join form | [optional] [default to False]
**referral** | **str** | The \&quot;How did you hear about us?\&quot; information provided to us when the member submitted the join form | [optional] 
**notes** | **str** | A free-form text description of this Install, to track any additional information. For Installs imported from the spreadsheet, this starts with a formatted block of information about the import process and original spreadsheet data. However this structure can be changed by admins at any time and should not be relied on by automated systems.  | [optional] 
**diy** | **bool** | Was this install conducted by the member themselves? If not, it was done by a volunteer installer on their behalf | [optional] 
**building** | **int** | The building where the install is located. In the case of a structure with multiple buildings, this will be the building whose address makes sense for this install&#39;s unit. | [optional] 
**member** | **int** | The member this install is associated with | [optional] 

## Example

```python
from pymeshdb.models.patched_install import PatchedInstall

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedInstall from a JSON string
patched_install_instance = PatchedInstall.from_json(json)
# print the JSON string representation of the object
print(PatchedInstall.to_json())

# convert the object into a dict
patched_install_dict = patched_install_instance.to_dict()
# create an instance of PatchedInstall from a dict
patched_install_from_dict = PatchedInstall.from_dict(patched_install_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


