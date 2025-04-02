# InstallFeeBillingDatum

A  ModelSerializer MixIn which sets `NestedKeyObjectRelatedField` as the default field class to use for the foreign key fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**status** | [**InstallFeeBillingDatumStatusEnum**](InstallFeeBillingDatumStatusEnum.md) | The billing status of the associated install  * &#x60;ToBeBilled&#x60; - To Be Billed * &#x60;Billed&#x60; - Billed * &#x60;NotBillingDuplicate&#x60; - Not Billing - Duplicate * &#x60;NotBillingOther&#x60; - Not Billing - Other | [optional] 
**billing_date** | **date** | The date that the associated install was billed to the responsible organization | [optional] 
**invoice_number** | **str** | The invoice number that the associated install was billed via | [optional] 
**notes** | **str** | A free-form text description, to track any additional information. | [optional] 
**install** | [**InstallFeeBillingDatumInstall**](InstallFeeBillingDatumInstall.md) |  | 

## Example

```python
from pymeshdb.models.install_fee_billing_datum import InstallFeeBillingDatum

# TODO update the JSON string below
json = "{}"
# create an instance of InstallFeeBillingDatum from a JSON string
install_fee_billing_datum_instance = InstallFeeBillingDatum.from_json(json)
# print the JSON string representation of the object
print(InstallFeeBillingDatum.to_json())

# convert the object into a dict
install_fee_billing_datum_dict = install_fee_billing_datum_instance.to_dict()
# create an instance of InstallFeeBillingDatum from a dict
install_fee_billing_datum_from_dict = InstallFeeBillingDatum.from_dict(install_fee_billing_datum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


