# pymeshdb.UISPImportApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_uisp_import_nn_create**](UISPImportApi.md#api_v1_uisp_import_nn_create) | **POST** /api/v1/uisp-import/nn/{network_number}/ | 


# **api_v1_uisp_import_nn_create**
> api_v1_uisp_import_nn_create(network_number)

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
    api_instance = pymeshdb.UISPImportApi(api_client)
    network_number = 56 # int | 

    try:
        api_instance.api_v1_uisp_import_nn_create(network_number)
    except Exception as e:
        print("Exception when calling UISPImportApi->api_v1_uisp_import_nn_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_number** | **int**|  | 

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
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

