# pymeshdb.WebsiteMapDataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_mapdata_kiosks_retrieve**](WebsiteMapDataApi.md#api_v1_mapdata_kiosks_retrieve) | **GET** /api/v1/mapdata/kiosks/ | Proxy for the city of new york LinkNYC kisok location dataset. Output in a JSON format that is compatible with the website map. (Warning: This endpoint is a legacy format and may be deprecated/removed in the future)
[**api_v1_mapdata_links_list**](WebsiteMapDataApi.md#api_v1_mapdata_links_list) | **GET** /api/v1/mapdata/links/ | Complete list of all Links, unpaginated, in the format expected by the website map. (Warning: This endpoint is a legacy format and may be deprecated/removed in the future)
[**api_v1_mapdata_nodes_list**](WebsiteMapDataApi.md#api_v1_mapdata_nodes_list) | **GET** /api/v1/mapdata/nodes/ | Complete list of all \&quot;Nodes\&quot; (mostly Installs with some fake installs generated to solve NN re-use), unpaginated, in the format expected by the website map. (Warning: This endpoint is a legacy format and may be deprecated/removed in the future)
[**api_v1_mapdata_sectors_list**](WebsiteMapDataApi.md#api_v1_mapdata_sectors_list) | **GET** /api/v1/mapdata/sectors/ | Complete list of all Sectors, unpaginated, in the format expected by the website map. (Warning: This endpoint is a legacy format and may be deprecated/removed in the future)


# **api_v1_mapdata_kiosks_retrieve**
> List[KioskData] api_v1_mapdata_kiosks_retrieve()

Proxy for the city of new york LinkNYC kisok location dataset. Output in a JSON format that is compatible with the website map. (Warning: This endpoint is a legacy format and may be deprecated/removed in the future)

### Example


```python
import pymeshdb
from pymeshdb.models.kiosk_data import KioskData
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
    api_instance = pymeshdb.WebsiteMapDataApi(api_client)

    try:
        # Proxy for the city of new york LinkNYC kisok location dataset. Output in a JSON format that is compatible with the website map. (Warning: This endpoint is a legacy format and may be deprecated/removed in the future)
        api_response = api_instance.api_v1_mapdata_kiosks_retrieve()
        print("The response of WebsiteMapDataApi->api_v1_mapdata_kiosks_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteMapDataApi->api_v1_mapdata_kiosks_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[KioskData]**](KioskData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully fetched a list of all linkNYC kiosks in the city |  -  |
**502** | Missing or invalid response received from NYC dataset |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_mapdata_links_list**
> List[MapDataLink] api_v1_mapdata_links_list()

Complete list of all Links, unpaginated, in the format expected by the website map. (Warning: This endpoint is a legacy format and may be deprecated/removed in the future)

### Example


```python
import pymeshdb
from pymeshdb.models.map_data_link import MapDataLink
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
    api_instance = pymeshdb.WebsiteMapDataApi(api_client)

    try:
        # Complete list of all Links, unpaginated, in the format expected by the website map. (Warning: This endpoint is a legacy format and may be deprecated/removed in the future)
        api_response = api_instance.api_v1_mapdata_links_list()
        print("The response of WebsiteMapDataApi->api_v1_mapdata_links_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteMapDataApi->api_v1_mapdata_links_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MapDataLink]**](MapDataLink.md)

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

# **api_v1_mapdata_nodes_list**
> List[MapDataInstall] api_v1_mapdata_nodes_list()

Complete list of all \"Nodes\" (mostly Installs with some fake installs generated to solve NN re-use), unpaginated, in the format expected by the website map. (Warning: This endpoint is a legacy format and may be deprecated/removed in the future)

### Example


```python
import pymeshdb
from pymeshdb.models.map_data_install import MapDataInstall
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
    api_instance = pymeshdb.WebsiteMapDataApi(api_client)

    try:
        # Complete list of all \"Nodes\" (mostly Installs with some fake installs generated to solve NN re-use), unpaginated, in the format expected by the website map. (Warning: This endpoint is a legacy format and may be deprecated/removed in the future)
        api_response = api_instance.api_v1_mapdata_nodes_list()
        print("The response of WebsiteMapDataApi->api_v1_mapdata_nodes_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteMapDataApi->api_v1_mapdata_nodes_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MapDataInstall]**](MapDataInstall.md)

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

# **api_v1_mapdata_sectors_list**
> List[MapDataSector] api_v1_mapdata_sectors_list()

Complete list of all Sectors, unpaginated, in the format expected by the website map. (Warning: This endpoint is a legacy format and may be deprecated/removed in the future)

### Example


```python
import pymeshdb
from pymeshdb.models.map_data_sector import MapDataSector
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
    api_instance = pymeshdb.WebsiteMapDataApi(api_client)

    try:
        # Complete list of all Sectors, unpaginated, in the format expected by the website map. (Warning: This endpoint is a legacy format and may be deprecated/removed in the future)
        api_response = api_instance.api_v1_mapdata_sectors_list()
        print("The response of WebsiteMapDataApi->api_v1_mapdata_sectors_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteMapDataApi->api_v1_mapdata_sectors_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MapDataSector]**](MapDataSector.md)

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

