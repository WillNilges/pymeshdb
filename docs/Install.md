# Install

A  ModelSerializer MixIn which sets `NestedKeyObjectRelatedField` as the default field class to use for the foreign key fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**request_date** | **datetime** |  | 
**install_fee_billing_datum** | [**InstallInstallFeeBillingDatum**](InstallInstallFeeBillingDatum.md) |  | 
**install_number** | **int** |  | [readonly] 
**status** | [**Status4ffEnum**](Status4ffEnum.md) | The current status of this install  * &#x60;Request Received&#x60; - Request Received * &#x60;Pending&#x60; - Pending * &#x60;Blocked&#x60; - Blocked * &#x60;Active&#x60; - Active * &#x60;Inactive&#x60; - Inactive * &#x60;Closed&#x60; - Closed * &#x60;NN Reassigned&#x60; - NN Reassigned | 
**ticket_number** | **str** | The ticket number of the OSTicket used to track communications with the member about this install. Note that although this appears to be an integer, it is not. Leading zeros are important, so this should be stored as a string at all times | [optional] 
**install_date** | **date** | The date this install was completed and deployed to the mesh | [optional] 
**abandon_date** | **date** | The date this install was abandoned, unplugged, or disassembled | [optional] 
**unit** | **str** | Line 2 of this install&#39;s mailing address | [optional] 
**roof_access** | **bool** | True if the member indicated they had access to the roof when they submitted the join form | [optional] [default to False]
**referral** | **str** | The \&quot;How did you hear about us?\&quot; information provided to us when the member submitted the join form | [optional] 
**notes** | **str** | A free-form text description of this Install, to track any additional information. For Installs imported from the spreadsheet, this starts with a formatted block of information about the import process and original spreadsheet data. However this structure can be changed by admins at any time and should not be relied on by automated systems.  | [optional] 
**diy** | **bool** | Was this install conducted by the member themselves? If not, it was done by a volunteer installer on their behalf | [optional] 
**node** | [**InstallNode**](InstallNode.md) |  | [optional] 
**building** | [**InstallBuilding**](InstallBuilding.md) |  | 
**member** | [**InstallMember**](InstallMember.md) |  | 
**additional_members** | [**List[InstallAdditionalMembersInner]**](InstallAdditionalMembersInner.md) | Any additional members associated with this install. E.g. roommates, parents, caretakers etc. Anyone that might contact us on behalf of this install belongs here | [optional] 

## Example

```python
from pymeshdb.models.install import Install

# TODO update the JSON string below
json = "{}"
# create an instance of Install from a JSON string
install_instance = Install.from_json(json)
# print the JSON string representation of the object
print(Install.to_json())

# convert the object into a dict
install_dict = install_instance.to_dict()
# create an instance of Install from a dict
install_from_dict = Install.from_dict(install_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


