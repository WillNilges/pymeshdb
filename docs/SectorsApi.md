# pymeshdb.SectorsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_sectors_create**](SectorsApi.md#api_v1_sectors_create) | **POST** /api/v1/sectors/ | 
[**api_v1_sectors_destroy**](SectorsApi.md#api_v1_sectors_destroy) | **DELETE** /api/v1/sectors/{id}/ | 
[**api_v1_sectors_list**](SectorsApi.md#api_v1_sectors_list) | **GET** /api/v1/sectors/ | 
[**api_v1_sectors_lookup_list**](SectorsApi.md#api_v1_sectors_lookup_list) | **GET** /api/v1/sectors/lookup/ | 
[**api_v1_sectors_partial_update**](SectorsApi.md#api_v1_sectors_partial_update) | **PATCH** /api/v1/sectors/{id}/ | 
[**api_v1_sectors_retrieve**](SectorsApi.md#api_v1_sectors_retrieve) | **GET** /api/v1/sectors/{id}/ | 
[**api_v1_sectors_update**](SectorsApi.md#api_v1_sectors_update) | **PUT** /api/v1/sectors/{id}/ | 


# **api_v1_sectors_create**
> Sector api_v1_sectors_create(sector)



### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.sector import Sector
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
    api_instance = pymeshdb.SectorsApi(api_client)
    sector = pymeshdb.Sector() # Sector | 

    try:
        api_response = api_instance.api_v1_sectors_create(sector)
        print("The response of SectorsApi->api_v1_sectors_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SectorsApi->api_v1_sectors_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sector** | [**Sector**](Sector.md)|  | 

### Return type

[**Sector**](Sector.md)

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

# **api_v1_sectors_destroy**
> api_v1_sectors_destroy(id)



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
    api_instance = pymeshdb.SectorsApi(api_client)
    id = 56 # int | 

    try:
        api_instance.api_v1_sectors_destroy(id)
    except Exception as e:
        print("Exception when calling SectorsApi->api_v1_sectors_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

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

# **api_v1_sectors_list**
> PaginatedSectorList api_v1_sectors_list(page=page)



### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.paginated_sector_list import PaginatedSectorList
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
    api_instance = pymeshdb.SectorsApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.api_v1_sectors_list(page=page)
        print("The response of SectorsApi->api_v1_sectors_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SectorsApi->api_v1_sectors_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedSectorList**](PaginatedSectorList.md)

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

# **api_v1_sectors_lookup_list**
> PaginatedSectorList api_v1_sectors_lookup_list(model=model, name=name, network_number=network_number, page=page, ssid=ssid, status=status, type=type, uisp_id=uisp_id)



### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.paginated_sector_list import PaginatedSectorList
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
    api_instance = pymeshdb.SectorsApi(api_client)
    model = 'model_example' # str | Filter sectors by the model name field using strict equality (optional)
    name = 'name_example' # str | Filter sectors by the name field using case-insensitve substring matching (optional)
    network_number = 56 # int | Filter sectors by network_number using strict equality (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    ssid = 'ssid_example' # str | Filter sectors by the ssid field using strict equality (optional)
    status = 'status_example' # str | Filter sectors by the status field using strict equality (optional)
    type = 'type_example' # str | Filter sectors by the type field using strict equality (optional)
    uisp_id = 'uisp_id_example' # str | Filter sectors by the uisp_id field using strict equality (optional)

    try:
        api_response = api_instance.api_v1_sectors_lookup_list(model=model, name=name, network_number=network_number, page=page, ssid=ssid, status=status, type=type, uisp_id=uisp_id)
        print("The response of SectorsApi->api_v1_sectors_lookup_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SectorsApi->api_v1_sectors_lookup_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| Filter sectors by the model name field using strict equality | [optional] 
 **name** | **str**| Filter sectors by the name field using case-insensitve substring matching | [optional] 
 **network_number** | **int**| Filter sectors by network_number using strict equality | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **ssid** | **str**| Filter sectors by the ssid field using strict equality | [optional] 
 **status** | **str**| Filter sectors by the status field using strict equality | [optional] 
 **type** | **str**| Filter sectors by the type field using strict equality | [optional] 
 **uisp_id** | **str**| Filter sectors by the uisp_id field using strict equality | [optional] 

### Return type

[**PaginatedSectorList**](PaginatedSectorList.md)

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

# **api_v1_sectors_partial_update**
> Sector api_v1_sectors_partial_update(id, patched_sector=patched_sector)



### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.patched_sector import PatchedSector
from pymeshdb.models.sector import Sector
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
    api_instance = pymeshdb.SectorsApi(api_client)
    id = 56 # int | 
    patched_sector = pymeshdb.PatchedSector() # PatchedSector |  (optional)

    try:
        api_response = api_instance.api_v1_sectors_partial_update(id, patched_sector=patched_sector)
        print("The response of SectorsApi->api_v1_sectors_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SectorsApi->api_v1_sectors_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **patched_sector** | [**PatchedSector**](PatchedSector.md)|  | [optional] 

### Return type

[**Sector**](Sector.md)

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

# **api_v1_sectors_retrieve**
> Sector api_v1_sectors_retrieve(id)



### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.sector import Sector
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
    api_instance = pymeshdb.SectorsApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.api_v1_sectors_retrieve(id)
        print("The response of SectorsApi->api_v1_sectors_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SectorsApi->api_v1_sectors_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Sector**](Sector.md)

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

# **api_v1_sectors_update**
> Sector api_v1_sectors_update(id, sector)



### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.sector import Sector
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
    api_instance = pymeshdb.SectorsApi(api_client)
    id = 56 # int | 
    sector = pymeshdb.Sector() # Sector | 

    try:
        api_response = api_instance.api_v1_sectors_update(id, sector)
        print("The response of SectorsApi->api_v1_sectors_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SectorsApi->api_v1_sectors_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **sector** | [**Sector**](Sector.md)|  | 

### Return type

[**Sector**](Sector.md)

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

