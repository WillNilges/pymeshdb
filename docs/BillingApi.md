# pymeshdb.BillingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_billing_install_fee_data_create**](BillingApi.md#api_v1_billing_install_fee_data_create) | **POST** /api/v1/billing/install-fee-data/ | 
[**api_v1_billing_install_fee_data_destroy**](BillingApi.md#api_v1_billing_install_fee_data_destroy) | **DELETE** /api/v1/billing/install-fee-data/{id}/ | 
[**api_v1_billing_install_fee_data_list**](BillingApi.md#api_v1_billing_install_fee_data_list) | **GET** /api/v1/billing/install-fee-data/ | 
[**api_v1_billing_install_fee_data_partial_update**](BillingApi.md#api_v1_billing_install_fee_data_partial_update) | **PATCH** /api/v1/billing/install-fee-data/{id}/ | 
[**api_v1_billing_install_fee_data_retrieve**](BillingApi.md#api_v1_billing_install_fee_data_retrieve) | **GET** /api/v1/billing/install-fee-data/{id}/ | 
[**api_v1_billing_install_fee_data_update**](BillingApi.md#api_v1_billing_install_fee_data_update) | **PUT** /api/v1/billing/install-fee-data/{id}/ | 


# **api_v1_billing_install_fee_data_create**
> InstallFeeBillingDatum api_v1_billing_install_fee_data_create(install_fee_billing_datum)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.install_fee_billing_datum import InstallFeeBillingDatum
from pymeshdb.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymeshdb.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: Session ID
configuration.api_key['Session ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session ID'] = 'Bearer'

# Enter a context with an instance of the API client
with pymeshdb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymeshdb.BillingApi(api_client)
    install_fee_billing_datum = pymeshdb.InstallFeeBillingDatum() # InstallFeeBillingDatum | 

    try:
        api_response = api_instance.api_v1_billing_install_fee_data_create(install_fee_billing_datum)
        print("The response of BillingApi->api_v1_billing_install_fee_data_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->api_v1_billing_install_fee_data_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_fee_billing_datum** | [**InstallFeeBillingDatum**](InstallFeeBillingDatum.md)|  | 

### Return type

[**InstallFeeBillingDatum**](InstallFeeBillingDatum.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [Session ID](../README.md#Session ID)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_billing_install_fee_data_destroy**
> api_v1_billing_install_fee_data_destroy(id)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymeshdb.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: Session ID
configuration.api_key['Session ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session ID'] = 'Bearer'

# Enter a context with an instance of the API client
with pymeshdb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymeshdb.BillingApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.api_v1_billing_install_fee_data_destroy(id)
    except Exception as e:
        print("Exception when calling BillingApi->api_v1_billing_install_fee_data_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth), [Session ID](../README.md#Session ID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_billing_install_fee_data_list**
> PaginatedInstallFeeBillingDatumList api_v1_billing_install_fee_data_list(page=page, page_size=page_size)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.paginated_install_fee_billing_datum_list import PaginatedInstallFeeBillingDatumList
from pymeshdb.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymeshdb.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: Session ID
configuration.api_key['Session ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session ID'] = 'Bearer'

# Enter a context with an instance of the API client
with pymeshdb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymeshdb.BillingApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = api_instance.api_v1_billing_install_fee_data_list(page=page, page_size=page_size)
        print("The response of BillingApi->api_v1_billing_install_fee_data_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->api_v1_billing_install_fee_data_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedInstallFeeBillingDatumList**](PaginatedInstallFeeBillingDatumList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [Session ID](../README.md#Session ID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_billing_install_fee_data_partial_update**
> InstallFeeBillingDatum api_v1_billing_install_fee_data_partial_update(id, patched_install_fee_billing_datum=patched_install_fee_billing_datum)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.install_fee_billing_datum import InstallFeeBillingDatum
from pymeshdb.models.patched_install_fee_billing_datum import PatchedInstallFeeBillingDatum
from pymeshdb.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymeshdb.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: Session ID
configuration.api_key['Session ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session ID'] = 'Bearer'

# Enter a context with an instance of the API client
with pymeshdb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymeshdb.BillingApi(api_client)
    id = 'id_example' # str | 
    patched_install_fee_billing_datum = pymeshdb.PatchedInstallFeeBillingDatum() # PatchedInstallFeeBillingDatum |  (optional)

    try:
        api_response = api_instance.api_v1_billing_install_fee_data_partial_update(id, patched_install_fee_billing_datum=patched_install_fee_billing_datum)
        print("The response of BillingApi->api_v1_billing_install_fee_data_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->api_v1_billing_install_fee_data_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **patched_install_fee_billing_datum** | [**PatchedInstallFeeBillingDatum**](PatchedInstallFeeBillingDatum.md)|  | [optional] 

### Return type

[**InstallFeeBillingDatum**](InstallFeeBillingDatum.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [Session ID](../README.md#Session ID)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_billing_install_fee_data_retrieve**
> InstallFeeBillingDatum api_v1_billing_install_fee_data_retrieve(id)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.install_fee_billing_datum import InstallFeeBillingDatum
from pymeshdb.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymeshdb.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: Session ID
configuration.api_key['Session ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session ID'] = 'Bearer'

# Enter a context with an instance of the API client
with pymeshdb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymeshdb.BillingApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.api_v1_billing_install_fee_data_retrieve(id)
        print("The response of BillingApi->api_v1_billing_install_fee_data_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->api_v1_billing_install_fee_data_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**InstallFeeBillingDatum**](InstallFeeBillingDatum.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [Session ID](../README.md#Session ID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_billing_install_fee_data_update**
> InstallFeeBillingDatum api_v1_billing_install_fee_data_update(id, install_fee_billing_datum)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.install_fee_billing_datum import InstallFeeBillingDatum
from pymeshdb.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymeshdb.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: Session ID
configuration.api_key['Session ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session ID'] = 'Bearer'

# Enter a context with an instance of the API client
with pymeshdb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymeshdb.BillingApi(api_client)
    id = 'id_example' # str | 
    install_fee_billing_datum = pymeshdb.InstallFeeBillingDatum() # InstallFeeBillingDatum | 

    try:
        api_response = api_instance.api_v1_billing_install_fee_data_update(id, install_fee_billing_datum)
        print("The response of BillingApi->api_v1_billing_install_fee_data_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->api_v1_billing_install_fee_data_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **install_fee_billing_datum** | [**InstallFeeBillingDatum**](InstallFeeBillingDatum.md)|  | 

### Return type

[**InstallFeeBillingDatum**](InstallFeeBillingDatum.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [Session ID](../README.md#Session ID)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

