# pymeshdb.LegacyQueryFormApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_query_buildings_list**](LegacyQueryFormApi.md#api_v1_query_buildings_list) | **GET** /api/v1/query/buildings/ | Query &amp; filter based on Building attributes. Results are returned as flattened spreadsheet row style output
[**api_v1_query_installs_list**](LegacyQueryFormApi.md#api_v1_query_installs_list) | **GET** /api/v1/query/installs/ | Query &amp; filter based on Install attributes. Results are returned as flattened spreadsheet row style output
[**api_v1_query_members_list**](LegacyQueryFormApi.md#api_v1_query_members_list) | **GET** /api/v1/query/members/ | Query &amp; filter based on Member attributes. Results are returned as flattened spreadsheet row style output


# **api_v1_query_buildings_list**
> PaginatedQueryFormList api_v1_query_buildings_list(password, bin=bin, city=city, page=page, page_size=page_size, state=state, street_address=street_address, zip_code=zip_code)

Query & filter based on Building attributes. Results are returned as flattened spreadsheet row style output

### Example


```python
import pymeshdb
from pymeshdb.models.paginated_query_form_list import PaginatedQueryFormList
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
    api_instance = pymeshdb.LegacyQueryFormApi(api_client)
    password = 'password_example' # str | The password for the legacy query form
    bin = 'bin_example' # str |  (optional)
    city = 'city_example' # str |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    state = 'state_example' # str |  (optional)
    street_address = 'street_address_example' # str |  (optional)
    zip_code = 'zip_code_example' # str |  (optional)

    try:
        # Query & filter based on Building attributes. Results are returned as flattened spreadsheet row style output
        api_response = api_instance.api_v1_query_buildings_list(password, bin=bin, city=city, page=page, page_size=page_size, state=state, street_address=street_address, zip_code=zip_code)
        print("The response of LegacyQueryFormApi->api_v1_query_buildings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacyQueryFormApi->api_v1_query_buildings_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | **str**| The password for the legacy query form | 
 **bin** | **str**|  | [optional] 
 **city** | **str**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **state** | **str**|  | [optional] 
 **street_address** | **str**|  | [optional] 
 **zip_code** | **str**|  | [optional] 

### Return type

[**PaginatedQueryFormList**](PaginatedQueryFormList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_query_installs_list**
> PaginatedQueryFormList api_v1_query_installs_list(password, building=building, install_number=install_number, member=member, network_number=network_number, page=page, page_size=page_size, status=status)

Query & filter based on Install attributes. Results are returned as flattened spreadsheet row style output

### Example


```python
import pymeshdb
from pymeshdb.models.paginated_query_form_list import PaginatedQueryFormList
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
    api_instance = pymeshdb.LegacyQueryFormApi(api_client)
    password = 'password_example' # str | The password for the legacy query form
    building = 'building_example' # str |  (optional)
    install_number = 56 # int |  (optional)
    member = 'member_example' # str |  (optional)
    network_number = 56 # int |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    status = 'status_example' # str | The current status of this install  * `Request Received` - Request Received * `Pending` - Pending * `Blocked` - Blocked * `Active` - Active * `Inactive` - Inactive * `Closed` - Closed * `NN Reassigned` - NN Reassigned (optional)

    try:
        # Query & filter based on Install attributes. Results are returned as flattened spreadsheet row style output
        api_response = api_instance.api_v1_query_installs_list(password, building=building, install_number=install_number, member=member, network_number=network_number, page=page, page_size=page_size, status=status)
        print("The response of LegacyQueryFormApi->api_v1_query_installs_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacyQueryFormApi->api_v1_query_installs_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | **str**| The password for the legacy query form | 
 **building** | **str**|  | [optional] 
 **install_number** | **int**|  | [optional] 
 **member** | **str**|  | [optional] 
 **network_number** | **int**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **status** | **str**| The current status of this install  * &#x60;Request Received&#x60; - Request Received * &#x60;Pending&#x60; - Pending * &#x60;Blocked&#x60; - Blocked * &#x60;Active&#x60; - Active * &#x60;Inactive&#x60; - Inactive * &#x60;Closed&#x60; - Closed * &#x60;NN Reassigned&#x60; - NN Reassigned | [optional] 

### Return type

[**PaginatedQueryFormList**](PaginatedQueryFormList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_query_members_list**
> PaginatedQueryFormList api_v1_query_members_list(password, email_address=email_address, name=name, page=page, page_size=page_size, phone_number=phone_number)

Query & filter based on Member attributes. Results are returned as flattened spreadsheet row style output

### Example


```python
import pymeshdb
from pymeshdb.models.paginated_query_form_list import PaginatedQueryFormList
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
    api_instance = pymeshdb.LegacyQueryFormApi(api_client)
    password = 'password_example' # str | The password for the legacy query form
    email_address = 'email_address_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    phone_number = 'phone_number_example' # str |  (optional)

    try:
        # Query & filter based on Member attributes. Results are returned as flattened spreadsheet row style output
        api_response = api_instance.api_v1_query_members_list(password, email_address=email_address, name=name, page=page, page_size=page_size, phone_number=phone_number)
        print("The response of LegacyQueryFormApi->api_v1_query_members_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacyQueryFormApi->api_v1_query_members_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | **str**| The password for the legacy query form | 
 **email_address** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **phone_number** | **str**|  | [optional] 

### Return type

[**PaginatedQueryFormList**](PaginatedQueryFormList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

