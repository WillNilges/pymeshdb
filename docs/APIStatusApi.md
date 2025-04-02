# pymeshdb.APIStatusApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_retrieve**](APIStatusApi.md#api_v1_retrieve) | **GET** /api/v1/ | Check API status


# **api_v1_retrieve**
> str api_v1_retrieve()

Check API status

This endpoint can be used by clients to determine the health status of this API. This API always
returns 200 status codes, accepts no input, and has no side effects. It always returns the
string "We're meshin'."

### Example


```python
import pymeshdb
from pymeshdb.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pymeshdb.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pymeshdb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pymeshdb.APIStatusApi(api_client)

    try:
        # Check API status
        api_response = api_instance.api_v1_retrieve()
        print("The response of APIStatusApi->api_v1_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIStatusApi->api_v1_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API is up and serving traffic |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

