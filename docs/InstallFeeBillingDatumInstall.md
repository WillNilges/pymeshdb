# InstallFeeBillingDatumInstall

Which Install object does this billing data refer to

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**install_number** | **int** |  | [optional] 

## Example

```python
from pymeshdb.models.install_fee_billing_datum_install import InstallFeeBillingDatumInstall

# TODO update the JSON string below
json = "{}"
# create an instance of InstallFeeBillingDatumInstall from a JSON string
install_fee_billing_datum_install_instance = InstallFeeBillingDatumInstall.from_json(json)
# print the JSON string representation of the object
print(InstallFeeBillingDatumInstall.to_json())

# convert the object into a dict
install_fee_billing_datum_install_dict = install_fee_billing_datum_install_instance.to_dict()
# create an instance of InstallFeeBillingDatumInstall from a dict
install_fee_billing_datum_install_from_dict = InstallFeeBillingDatumInstall.from_dict(install_fee_billing_datum_install_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


