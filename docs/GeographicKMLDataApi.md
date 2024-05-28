# pymeshdb.GeographicKMLDataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_geography_whole_mesh_kml_retrieve**](GeographicKMLDataApi.md#api_v1_geography_whole_mesh_kml_retrieve) | **GET** /api/v1/geography/whole-mesh.kml | Generate a KML file which contains all nodes and links on the mesh


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

