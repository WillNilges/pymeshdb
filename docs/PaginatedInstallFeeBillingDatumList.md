# PaginatedInstallFeeBillingDatumList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[InstallFeeBillingDatum]**](InstallFeeBillingDatum.md) |  | 

## Example

```python
from pymeshdb.models.paginated_install_fee_billing_datum_list import PaginatedInstallFeeBillingDatumList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedInstallFeeBillingDatumList from a JSON string
paginated_install_fee_billing_datum_list_instance = PaginatedInstallFeeBillingDatumList.from_json(json)
# print the JSON string representation of the object
print(PaginatedInstallFeeBillingDatumList.to_json())

# convert the object into a dict
paginated_install_fee_billing_datum_list_dict = paginated_install_fee_billing_datum_list_instance.to_dict()
# create an instance of PaginatedInstallFeeBillingDatumList from a dict
paginated_install_fee_billing_datum_list_from_dict = PaginatedInstallFeeBillingDatumList.from_dict(paginated_install_fee_billing_datum_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


