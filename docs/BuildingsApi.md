# pymeshdb.BuildingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_buildings_create**](BuildingsApi.md#api_v1_buildings_create) | **POST** /api/v1/buildings/ | 
[**api_v1_buildings_destroy**](BuildingsApi.md#api_v1_buildings_destroy) | **DELETE** /api/v1/buildings/{id}/ | 
[**api_v1_buildings_list**](BuildingsApi.md#api_v1_buildings_list) | **GET** /api/v1/buildings/ | 
[**api_v1_buildings_lookup_list**](BuildingsApi.md#api_v1_buildings_lookup_list) | **GET** /api/v1/buildings/lookup/ | 
[**api_v1_buildings_partial_update**](BuildingsApi.md#api_v1_buildings_partial_update) | **PATCH** /api/v1/buildings/{id}/ | 
[**api_v1_buildings_retrieve**](BuildingsApi.md#api_v1_buildings_retrieve) | **GET** /api/v1/buildings/{id}/ | 
[**api_v1_buildings_update**](BuildingsApi.md#api_v1_buildings_update) | **PUT** /api/v1/buildings/{id}/ | 


# **api_v1_buildings_create**
> Building api_v1_buildings_create(building)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.building import Building
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
    api_instance = pymeshdb.BuildingsApi(api_client)
    building = pymeshdb.Building() # Building | 

    try:
        api_response = api_instance.api_v1_buildings_create(building)
        print("The response of BuildingsApi->api_v1_buildings_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildingsApi->api_v1_buildings_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building** | [**Building**](Building.md)|  | 

### Return type

[**Building**](Building.md)

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

# **api_v1_buildings_destroy**
> api_v1_buildings_destroy(id)

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
    api_instance = pymeshdb.BuildingsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.api_v1_buildings_destroy(id)
    except Exception as e:
        print("Exception when calling BuildingsApi->api_v1_buildings_destroy: %s\n" % e)
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

# **api_v1_buildings_list**
> PaginatedBuildingList api_v1_buildings_list(page=page, page_size=page_size)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.paginated_building_list import PaginatedBuildingList
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
    api_instance = pymeshdb.BuildingsApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = api_instance.api_v1_buildings_list(page=page, page_size=page_size)
        print("The response of BuildingsApi->api_v1_buildings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildingsApi->api_v1_buildings_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedBuildingList**](PaginatedBuildingList.md)

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

# **api_v1_buildings_lookup_list**
> PaginatedBuildingList api_v1_buildings_lookup_list(bin=bin, city=city, install_number=install_number, network_number=network_number, node=node, page=page, page_size=page_size, primary_network_number=primary_network_number, primary_node=primary_node, state=state, street_address=street_address, zip_code=zip_code)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.paginated_building_list import PaginatedBuildingList
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
    api_instance = pymeshdb.BuildingsApi(api_client)
    bin = 56 # int | Filter installs by bin using strict equality (optional)
    city = 'city_example' # str | Filter installs by the city field using case-insensitve equality (optional)
    install_number = 56 # int | Filter Buildings by install_number using strict equality (optional)
    network_number = 56 # int | Filter Buildings by the network number of their associated nodes using strict equality (optional)
    node = 'node_example' # str |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    primary_network_number = 56 # int | Filter Buildings by the network number of their primary node using strict equality (optional)
    primary_node = 'primary_node_example' # str |  (optional)
    state = 'state_example' # str | Filter installs by the state field using case-insensitve equality (optional)
    street_address = 'street_address_example' # str | Filter installs by the street_address field using case-insensitve substring matching (optional)
    zip_code = 'zip_code_example' # str | Filter installs by the zip_code field using strict equality (optional)

    try:
        api_response = api_instance.api_v1_buildings_lookup_list(bin=bin, city=city, install_number=install_number, network_number=network_number, node=node, page=page, page_size=page_size, primary_network_number=primary_network_number, primary_node=primary_node, state=state, street_address=street_address, zip_code=zip_code)
        print("The response of BuildingsApi->api_v1_buildings_lookup_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildingsApi->api_v1_buildings_lookup_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bin** | **int**| Filter installs by bin using strict equality | [optional] 
 **city** | **str**| Filter installs by the city field using case-insensitve equality | [optional] 
 **install_number** | **int**| Filter Buildings by install_number using strict equality | [optional] 
 **network_number** | **int**| Filter Buildings by the network number of their associated nodes using strict equality | [optional] 
 **node** | **str**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **primary_network_number** | **int**| Filter Buildings by the network number of their primary node using strict equality | [optional] 
 **primary_node** | **str**|  | [optional] 
 **state** | **str**| Filter installs by the state field using case-insensitve equality | [optional] 
 **street_address** | **str**| Filter installs by the street_address field using case-insensitve substring matching | [optional] 
 **zip_code** | **str**| Filter installs by the zip_code field using strict equality | [optional] 

### Return type

[**PaginatedBuildingList**](PaginatedBuildingList.md)

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

# **api_v1_buildings_partial_update**
> Building api_v1_buildings_partial_update(id, patched_building=patched_building)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.building import Building
from pymeshdb.models.patched_building import PatchedBuilding
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
    api_instance = pymeshdb.BuildingsApi(api_client)
    id = 'id_example' # str | 
    patched_building = pymeshdb.PatchedBuilding() # PatchedBuilding |  (optional)

    try:
        api_response = api_instance.api_v1_buildings_partial_update(id, patched_building=patched_building)
        print("The response of BuildingsApi->api_v1_buildings_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildingsApi->api_v1_buildings_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **patched_building** | [**PatchedBuilding**](PatchedBuilding.md)|  | [optional] 

### Return type

[**Building**](Building.md)

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

# **api_v1_buildings_retrieve**
> Building api_v1_buildings_retrieve(id)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.building import Building
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
    api_instance = pymeshdb.BuildingsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.api_v1_buildings_retrieve(id)
        print("The response of BuildingsApi->api_v1_buildings_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildingsApi->api_v1_buildings_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Building**](Building.md)

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

# **api_v1_buildings_update**
> Building api_v1_buildings_update(id, building)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.building import Building
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
    api_instance = pymeshdb.BuildingsApi(api_client)
    id = 'id_example' # str | 
    building = pymeshdb.Building() # Building | 

    try:
        api_response = api_instance.api_v1_buildings_update(id, building)
        print("The response of BuildingsApi->api_v1_buildings_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildingsApi->api_v1_buildings_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **building** | [**Building**](Building.md)|  | 

### Return type

[**Building**](Building.md)

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

