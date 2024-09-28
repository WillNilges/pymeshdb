# Member

A  ModelSerializer MixIn which sets `NestedKeyObjectRelatedField` as the default field class to use for the foreign key fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**all_email_addresses** | **List[str]** |  | [readonly] 
**all_phone_numbers** | **List[str]** |  | [readonly] 
**installs** | [**List[BuildingInstallsInner]**](BuildingInstallsInner.md) |  | [readonly] 
**name** | **str** | Member full name in the format: \&quot;First Last\&quot; | 
**primary_email_address** | **str** | Primary email address used to contact the member | [optional] 
**stripe_email_address** | **str** | Email address used by the member to donate via Stripe, if different to their primary email | [optional] 
**additional_email_addresses** | **List[str]** | Any additional email addresses associated with this member | [optional] 
**phone_number** | **str** | A primary contact phone number for this member | [optional] 
**additional_phone_numbers** | **List[str]** | Any additional phone numbers used by this member | [optional] 
**slack_handle** | **str** | The member&#39;s slack handle | [optional] 
**notes** | **str** | A free-form text description of how to contact this member, to track any additional information. For Members imported from the spreadsheet, this starts with a formatted block of information about the import process and original spreadsheet data. However this structure can be changed by admins at any time and should not be relied on by automated systems.  | [optional] 

## Example

```python
from pymeshdb.models.member import Member

# TODO update the JSON string below
json = "{}"
# create an instance of Member from a JSON string
member_instance = Member.from_json(json)
# print the JSON string representation of the object
print(Member.to_json())

# convert the object into a dict
member_dict = member_instance.to_dict()
# create an instance of Member from a dict
member_from_dict = Member.from_dict(member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


