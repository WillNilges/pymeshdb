# pymeshdb.GeographicKMLDataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_geography_nyc_geocode_v2_search_retrieve**](GeographicKMLDataApi.md#api_v1_geography_nyc_geocode_v2_search_retrieve) | **GET** /api/v1/geography/nyc-geocode/v2/search | Use the NYC geocoding APIs to look up an address, and return the lat/lon/alt corresponding to it or 404 if the address cannot be found within NYC
[**api_v1_geography_whole_mesh_kml_retrieve**](GeographicKMLDataApi.md#api_v1_geography_whole_mesh_kml_retrieve) | **GET** /api/v1/geography/whole-mesh.kml | Generate a KML file which contains all nodes and links on the mesh


# **api_v1_geography_nyc_geocode_v2_search_retrieve**
> GeocodeSuccessResponse api_v1_geography_nyc_geocode_v2_search_retrieve(city, state, street_address, zip)

Use the NYC geocoding APIs to look up an address, and return the lat/lon/alt corresponding to it or 404 if the address cannot be found within NYC

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (Session ID):

```python
import pymeshdb
from pymeshdb.models.geocode_success_response import GeocodeSuccessResponse
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
    api_instance = pymeshdb.GeographicKMLDataApi(api_client)
    city = 'city_example' # str | 
    state = 'state_example' # str | 
    street_address = 'street_address_example' # str | 
    zip = 'zip_example' # str | 

    try:
        # Use the NYC geocoding APIs to look up an address, and return the lat/lon/alt corresponding to it or 404 if the address cannot be found within NYC
        api_response = api_instance.api_v1_geography_nyc_geocode_v2_search_retrieve(city, state, street_address, zip)
        print("The response of GeographicKMLDataApi->api_v1_geography_nyc_geocode_v2_search_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeographicKMLDataApi->api_v1_geography_nyc_geocode_v2_search_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **city** | **str**|  | 
 **state** | **str**|  | 
 **street_address** | **str**|  | 
 **zip** | **str**|  | 

### Return type

[**GeocodeSuccessResponse**](GeocodeSuccessResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [Session ID](../README.md#Session ID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Request received, an install has been created (along with member and building objects if necessary). |  -  |
**400** | Invalid request body JSON or missing required fields |  -  |
**404** | Invalid address, or not found within NYC |  -  |
**500** | Could not geocode address due to internal failure. Try again? |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_geography_whole_mesh_kml_retrieve**
> bytearray api_v1_geography_whole_mesh_kml_retrieve()

Generate a KML file which contains all nodes and links on the mesh

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
    api_instance = pymeshdb.GeographicKMLDataApi(api_client)

    try:
        # Generate a KML file which contains all nodes and links on the mesh
        api_response = api_instance.api_v1_geography_whole_mesh_kml_retrieve()
        print("The response of GeographicKMLDataApi->api_v1_geography_whole_mesh_kml_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeographicKMLDataApi->api_v1_geography_whole_mesh_kml_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.google-earth.kml+xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesfully generated KML file. Returns XML Data conforming to the KML specification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

