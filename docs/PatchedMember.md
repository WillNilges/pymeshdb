# PatchedMember

A  ModelSerializer MixIn which sets `NestedKeyObjectRelatedField` as the default field class to use for the foreign key fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**all_email_addresses** | **List[str]** |  | [optional] [readonly] 
**all_phone_numbers** | **List[str]** |  | [optional] [readonly] 
**installs** | [**List[BuildingInstallsInner]**](BuildingInstallsInner.md) |  | [optional] [readonly] 
**name** | **str** | Member full name in the format: \&quot;First Last\&quot; | [optional] 
**primary_email_address** | **str** | Primary email address used to contact the member | [optional] 
**stripe_email_address** | **str** | Email address used by the member to donate via Stripe, if different to their primary email | [optional] 
**additional_email_addresses** | **List[str]** | Any additional email addresses associated with this member | [optional] 
**phone_number** | **str** | A primary contact phone number for this member | [optional] 
**additional_phone_numbers** | **List[str]** | Any additional phone numbers used by this member | [optional] 
**slack_handle** | **str** | The member&#39;s slack handle | [optional] 
**notes** | **str** | A free-form text description of how to contact this member, to track any additional information. For Members imported from the spreadsheet, this starts with a formatted block of information about the import process and original spreadsheet data. However this structure can be changed by admins at any time and should not be relied on by automated systems.  | [optional] 

## Example

```python
from pymeshdb.models.patched_member import PatchedMember

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMember from a JSON string
patched_member_instance = PatchedMember.from_json(json)
# print the JSON string representation of the object
print(PatchedMember.to_json())

# convert the object into a dict
patched_member_dict = patched_member_instance.to_dict()
# create an instance of PatchedMember from a dict
patched_member_from_dict = PatchedMember.from_dict(patched_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


