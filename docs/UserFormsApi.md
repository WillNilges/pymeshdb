# pymeshdb.UserFormsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_join_create**](UserFormsApi.md#api_v1_join_create) | **POST** /api/v1/join/ | Register a new request for a potential mesh Install. Used by the join form posted on the nycmesh.net website
[**api_v1_nn_assign_create**](UserFormsApi.md#api_v1_nn_assign_create) | **POST** /api/v1/nn-assign/ | Assign a network number to a given Install object. Used by the NN Assignment form


# **api_v1_join_create**
> JoinFormSuccessResponse api_v1_join_create(join_form_request)

Register a new request for a potential mesh Install. Used by the join form posted on the nycmesh.net website

### Example


```python
import pymeshdb
from pymeshdb.models.join_form_request import JoinFormRequest
from pymeshdb.models.join_form_success_response import JoinFormSuccessResponse
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
    api_instance = pymeshdb.UserFormsApi(api_client)
    join_form_request = pymeshdb.JoinFormRequest() # JoinFormRequest | 

    try:
        # Register a new request for a potential mesh Install. Used by the join form posted on the nycmesh.net website
        api_response = api_instance.api_v1_join_create(join_form_request)
        print("The response of UserFormsApi->api_v1_join_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFormsApi->api_v1_join_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **join_form_request** | [**JoinFormRequest**](JoinFormRequest.md)|  | 

### Return type

[**JoinFormSuccessResponse**](JoinFormSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Request received, an install has been created (along with member and building objects if necessary). |  -  |
**400** | Invalid request body JSON or missing required fields |  -  |
**500** | Unexpected internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_nn_assign_create**
> NNFormSuccessResponse api_v1_nn_assign_create(network_number_assignment_request)

Assign a network number to a given Install object. Used by the NN Assignment form

Takes an install number, and assigns the install a network number,
deduping using the other buildings in our database.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.nn_form_success_response import NNFormSuccessResponse
from pymeshdb.models.network_number_assignment_request import NetworkNumberAssignmentRequest
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
    api_instance = pymeshdb.UserFormsApi(api_client)
    network_number_assignment_request = pymeshdb.NetworkNumberAssignmentRequest() # NetworkNumberAssignmentRequest | 

    try:
        # Assign a network number to a given Install object. Used by the NN Assignment form
        api_response = api_instance.api_v1_nn_assign_create(network_number_assignment_request)
        print("The response of UserFormsApi->api_v1_nn_assign_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFormsApi->api_v1_nn_assign_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_number_assignment_request** | [**NetworkNumberAssignmentRequest**](NetworkNumberAssignmentRequest.md)|  | 

### Return type

[**NNFormSuccessResponse**](NNFormSuccessResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [Session ID](../README.md#Session ID)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This install already has an NN, no action has been perfomed in the DB |  -  |
**201** | This install did not already have an NN. One has been found (either from the backlog of unused installs or already existing on the Building) and assigned to this install. |  -  |
**400** | Invalid request body JSON or missing required fields |  -  |
**403** | Incorrect or missing password |  -  |
**404** | Requested install number could not be found |  -  |
**500** | Unexpected internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

