# pymeshdb.InstallsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_installs_create**](InstallsApi.md#api_v1_installs_create) | **POST** /api/v1/installs/ | 
[**api_v1_installs_destroy**](InstallsApi.md#api_v1_installs_destroy) | **DELETE** /api/v1/installs/{install_number}/ | 
[**api_v1_installs_list**](InstallsApi.md#api_v1_installs_list) | **GET** /api/v1/installs/ | 
[**api_v1_installs_lookup_list**](InstallsApi.md#api_v1_installs_lookup_list) | **GET** /api/v1/installs/lookup/ | 
[**api_v1_installs_partial_update**](InstallsApi.md#api_v1_installs_partial_update) | **PATCH** /api/v1/installs/{install_number}/ | 
[**api_v1_installs_retrieve**](InstallsApi.md#api_v1_installs_retrieve) | **GET** /api/v1/installs/{install_number}/ | 
[**api_v1_installs_update**](InstallsApi.md#api_v1_installs_update) | **PUT** /api/v1/installs/{install_number}/ | 


# **api_v1_installs_create**
> Install api_v1_installs_create(install)



### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.install import Install
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
    api_instance = pymeshdb.InstallsApi(api_client)
    install = pymeshdb.Install() # Install | 

    try:
        api_response = api_instance.api_v1_installs_create(install)
        print("The response of InstallsApi->api_v1_installs_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->api_v1_installs_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install** | [**Install**](Install.md)|  | 

### Return type

[**Install**](Install.md)

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

# **api_v1_installs_destroy**
> api_v1_installs_destroy(install_number)



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
    api_instance = pymeshdb.InstallsApi(api_client)
    install_number = 56 # int | A unique integer value identifying this install.

    try:
        api_instance.api_v1_installs_destroy(install_number)
    except Exception as e:
        print("Exception when calling InstallsApi->api_v1_installs_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_number** | **int**| A unique integer value identifying this install. | 

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

# **api_v1_installs_list**
> PaginatedInstallList api_v1_installs_list(page=page)



### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.paginated_install_list import PaginatedInstallList
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
    api_instance = pymeshdb.InstallsApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.api_v1_installs_list(page=page)
        print("The response of InstallsApi->api_v1_installs_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->api_v1_installs_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedInstallList**](PaginatedInstallList.md)

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

# **api_v1_installs_lookup_list**
> PaginatedInstallList api_v1_installs_lookup_list(building=building, member=member, network_number=network_number, page=page, status=status)



### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.paginated_install_list import PaginatedInstallList
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
    api_instance = pymeshdb.InstallsApi(api_client)
    building = 56 # int | Filter installs by the Building id foreign key field using strict equality (optional)
    member = 56 # int | Filter installs by the Member id foreign key field using strict equality (optional)
    network_number = 56 # int | Filter installs by network_number using strict equality (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    status = 'status_example' # str | Filter installs by the status field using strict equality (optional)

    try:
        api_response = api_instance.api_v1_installs_lookup_list(building=building, member=member, network_number=network_number, page=page, status=status)
        print("The response of InstallsApi->api_v1_installs_lookup_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->api_v1_installs_lookup_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building** | **int**| Filter installs by the Building id foreign key field using strict equality | [optional] 
 **member** | **int**| Filter installs by the Member id foreign key field using strict equality | [optional] 
 **network_number** | **int**| Filter installs by network_number using strict equality | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **status** | **str**| Filter installs by the status field using strict equality | [optional] 

### Return type

[**PaginatedInstallList**](PaginatedInstallList.md)

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

# **api_v1_installs_partial_update**
> Install api_v1_installs_partial_update(install_number, patched_install=patched_install)



### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.install import Install
from pymeshdb.models.patched_install import PatchedInstall
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
    api_instance = pymeshdb.InstallsApi(api_client)
    install_number = 56 # int | A unique integer value identifying this install.
    patched_install = pymeshdb.PatchedInstall() # PatchedInstall |  (optional)

    try:
        api_response = api_instance.api_v1_installs_partial_update(install_number, patched_install=patched_install)
        print("The response of InstallsApi->api_v1_installs_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->api_v1_installs_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_number** | **int**| A unique integer value identifying this install. | 
 **patched_install** | [**PatchedInstall**](PatchedInstall.md)|  | [optional] 

### Return type

[**Install**](Install.md)

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

# **api_v1_installs_retrieve**
> Install api_v1_installs_retrieve(install_number)



### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.install import Install
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
    api_instance = pymeshdb.InstallsApi(api_client)
    install_number = 56 # int | A unique integer value identifying this install.

    try:
        api_response = api_instance.api_v1_installs_retrieve(install_number)
        print("The response of InstallsApi->api_v1_installs_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->api_v1_installs_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_number** | **int**| A unique integer value identifying this install. | 

### Return type

[**Install**](Install.md)

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

# **api_v1_installs_update**
> Install api_v1_installs_update(install_number, install)



### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.install import Install
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
    api_instance = pymeshdb.InstallsApi(api_client)
    install_number = 56 # int | A unique integer value identifying this install.
    install = pymeshdb.Install() # Install | 

    try:
        api_response = api_instance.api_v1_installs_update(install_number, install)
        print("The response of InstallsApi->api_v1_installs_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallsApi->api_v1_installs_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_number** | **int**| A unique integer value identifying this install. | 
 **install** | [**Install**](Install.md)|  | 

### Return type

[**Install**](Install.md)

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

