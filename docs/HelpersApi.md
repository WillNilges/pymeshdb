# pymeshdb.HelpersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_disambiguate_number_retrieve**](HelpersApi.md#api_v1_disambiguate_number_retrieve) | **GET** /api/v1/disambiguate-number/ | Identify a number as either an NN or an install number (or both) based on MeshDB data about Installs and/or Nodes with that number


# **api_v1_disambiguate_number_retrieve**
> DisambiguateNumberSuccessResponse api_v1_disambiguate_number_retrieve(number)

Identify a number as either an NN or an install number (or both) based on MeshDB data about Installs and/or Nodes with that number

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.disambiguate_number_success_response import DisambiguateNumberSuccessResponse
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
    api_instance = pymeshdb.HelpersApi(api_client)
    number = 56 # int | The number to use to look up Installs and Nodes

    try:
        # Identify a number as either an NN or an install number (or both) based on MeshDB data about Installs and/or Nodes with that number
        api_response = api_instance.api_v1_disambiguate_number_retrieve(number)
        print("The response of HelpersApi->api_v1_disambiguate_number_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelpersApi->api_v1_disambiguate_number_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **int**| The number to use to look up Installs and Nodes | 

### Return type

[**DisambiguateNumberSuccessResponse**](DisambiguateNumberSuccessResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [Session ID](../README.md#Session ID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | At least one Node or Install exists corresponding to this |  -  |
**400** | Invalid request |  -  |
**404** | Requested number could not be found as either an Network or Install number |  -  |
**500** | Unexpected internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

