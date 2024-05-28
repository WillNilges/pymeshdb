# pymeshdb
Programmatic access to mesh core data, detailing our installs, members, etc. 

To use an authorization token, use the \"Authorize\" button, and under \"tokenAuth\" enter `Token ` before the content of your token, like this: `Token xxxyyyyyzzz`

If you have username/password credentials (like those used on the admin UI) you can login via the admin UI or [DRF login page](/auth/login/?next=/api-docs/swagger/)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.7.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/willnilges/pymeshdb.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/willnilges/pymeshdb.git`)

Then import the package:
```python
import pymeshdb
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pymeshdb
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    except ApiException as e:
        print("Exception when calling APIStatusApi->api_v1_retrieve: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*APIStatusApi* | [**api_v1_retrieve**](docs/APIStatusApi.md#api_v1_retrieve) | **GET** /api/v1/ | Check API status
*BuildingsApi* | [**api_v1_buildings_create**](docs/BuildingsApi.md#api_v1_buildings_create) | **POST** /api/v1/buildings/ | 
*BuildingsApi* | [**api_v1_buildings_destroy**](docs/BuildingsApi.md#api_v1_buildings_destroy) | **DELETE** /api/v1/buildings/{id}/ | 
*BuildingsApi* | [**api_v1_buildings_list**](docs/BuildingsApi.md#api_v1_buildings_list) | **GET** /api/v1/buildings/ | 
*BuildingsApi* | [**api_v1_buildings_lookup_list**](docs/BuildingsApi.md#api_v1_buildings_lookup_list) | **GET** /api/v1/buildings/lookup/ | 
*BuildingsApi* | [**api_v1_buildings_partial_update**](docs/BuildingsApi.md#api_v1_buildings_partial_update) | **PATCH** /api/v1/buildings/{id}/ | 
*BuildingsApi* | [**api_v1_buildings_retrieve**](docs/BuildingsApi.md#api_v1_buildings_retrieve) | **GET** /api/v1/buildings/{id}/ | 
*BuildingsApi* | [**api_v1_buildings_update**](docs/BuildingsApi.md#api_v1_buildings_update) | **PUT** /api/v1/buildings/{id}/ | 
*DevicesApi* | [**api_v1_devices_create**](docs/DevicesApi.md#api_v1_devices_create) | **POST** /api/v1/devices/ | 
*DevicesApi* | [**api_v1_devices_destroy**](docs/DevicesApi.md#api_v1_devices_destroy) | **DELETE** /api/v1/devices/{id}/ | 
*DevicesApi* | [**api_v1_devices_list**](docs/DevicesApi.md#api_v1_devices_list) | **GET** /api/v1/devices/ | 
*DevicesApi* | [**api_v1_devices_lookup_list**](docs/DevicesApi.md#api_v1_devices_lookup_list) | **GET** /api/v1/devices/lookup/ | 
*DevicesApi* | [**api_v1_devices_partial_update**](docs/DevicesApi.md#api_v1_devices_partial_update) | **PATCH** /api/v1/devices/{id}/ | 
*DevicesApi* | [**api_v1_devices_retrieve**](docs/DevicesApi.md#api_v1_devices_retrieve) | **GET** /api/v1/devices/{id}/ | 
*DevicesApi* | [**api_v1_devices_update**](docs/DevicesApi.md#api_v1_devices_update) | **PUT** /api/v1/devices/{id}/ | 
*GeographicKMLDataApi* | [**api_v1_geography_whole_mesh_kml_retrieve**](docs/GeographicKMLDataApi.md#api_v1_geography_whole_mesh_kml_retrieve) | **GET** /api/v1/geography/whole-mesh.kml | Generate a KML file which contains all nodes and links on the mesh
*InstallsApi* | [**api_v1_installs_create**](docs/InstallsApi.md#api_v1_installs_create) | **POST** /api/v1/installs/ | 
*InstallsApi* | [**api_v1_installs_destroy**](docs/InstallsApi.md#api_v1_installs_destroy) | **DELETE** /api/v1/installs/{install_number}/ | 
*InstallsApi* | [**api_v1_installs_list**](docs/InstallsApi.md#api_v1_installs_list) | **GET** /api/v1/installs/ | 
*InstallsApi* | [**api_v1_installs_lookup_list**](docs/InstallsApi.md#api_v1_installs_lookup_list) | **GET** /api/v1/installs/lookup/ | 
*InstallsApi* | [**api_v1_installs_partial_update**](docs/InstallsApi.md#api_v1_installs_partial_update) | **PATCH** /api/v1/installs/{install_number}/ | 
*InstallsApi* | [**api_v1_installs_retrieve**](docs/InstallsApi.md#api_v1_installs_retrieve) | **GET** /api/v1/installs/{install_number}/ | 
*InstallsApi* | [**api_v1_installs_update**](docs/InstallsApi.md#api_v1_installs_update) | **PUT** /api/v1/installs/{install_number}/ | 
*LegacyQueryFormApi* | [**api_v1_query_buildings_list**](docs/LegacyQueryFormApi.md#api_v1_query_buildings_list) | **GET** /api/v1/query/buildings/ | Query &amp; filter based on Building attributes. Results are returned as flattened spreadsheet row style output
*LegacyQueryFormApi* | [**api_v1_query_installs_list**](docs/LegacyQueryFormApi.md#api_v1_query_installs_list) | **GET** /api/v1/query/installs/ | Query &amp; filter based on Install attributes. Results are returned as flattened spreadsheet row style output
*LegacyQueryFormApi* | [**api_v1_query_members_list**](docs/LegacyQueryFormApi.md#api_v1_query_members_list) | **GET** /api/v1/query/members/ | Query &amp; filter based on Member attributes. Results are returned as flattened spreadsheet row style output
*LinksApi* | [**api_v1_links_create**](docs/LinksApi.md#api_v1_links_create) | **POST** /api/v1/links/ | 
*LinksApi* | [**api_v1_links_destroy**](docs/LinksApi.md#api_v1_links_destroy) | **DELETE** /api/v1/links/{id}/ | 
*LinksApi* | [**api_v1_links_list**](docs/LinksApi.md#api_v1_links_list) | **GET** /api/v1/links/ | 
*LinksApi* | [**api_v1_links_lookup_list**](docs/LinksApi.md#api_v1_links_lookup_list) | **GET** /api/v1/links/lookup/ | 
*LinksApi* | [**api_v1_links_partial_update**](docs/LinksApi.md#api_v1_links_partial_update) | **PATCH** /api/v1/links/{id}/ | 
*LinksApi* | [**api_v1_links_retrieve**](docs/LinksApi.md#api_v1_links_retrieve) | **GET** /api/v1/links/{id}/ | 
*LinksApi* | [**api_v1_links_update**](docs/LinksApi.md#api_v1_links_update) | **PUT** /api/v1/links/{id}/ | 
*MembersApi* | [**api_v1_members_create**](docs/MembersApi.md#api_v1_members_create) | **POST** /api/v1/members/ | 
*MembersApi* | [**api_v1_members_destroy**](docs/MembersApi.md#api_v1_members_destroy) | **DELETE** /api/v1/members/{id}/ | 
*MembersApi* | [**api_v1_members_list**](docs/MembersApi.md#api_v1_members_list) | **GET** /api/v1/members/ | 
*MembersApi* | [**api_v1_members_lookup_list**](docs/MembersApi.md#api_v1_members_lookup_list) | **GET** /api/v1/members/lookup/ | 
*MembersApi* | [**api_v1_members_partial_update**](docs/MembersApi.md#api_v1_members_partial_update) | **PATCH** /api/v1/members/{id}/ | 
*MembersApi* | [**api_v1_members_retrieve**](docs/MembersApi.md#api_v1_members_retrieve) | **GET** /api/v1/members/{id}/ | 
*MembersApi* | [**api_v1_members_update**](docs/MembersApi.md#api_v1_members_update) | **PUT** /api/v1/members/{id}/ | 
*NodesApi* | [**api_v1_nodes_create**](docs/NodesApi.md#api_v1_nodes_create) | **POST** /api/v1/nodes/ | 
*NodesApi* | [**api_v1_nodes_destroy**](docs/NodesApi.md#api_v1_nodes_destroy) | **DELETE** /api/v1/nodes/{network_number}/ | 
*NodesApi* | [**api_v1_nodes_list**](docs/NodesApi.md#api_v1_nodes_list) | **GET** /api/v1/nodes/ | 
*NodesApi* | [**api_v1_nodes_lookup_list**](docs/NodesApi.md#api_v1_nodes_lookup_list) | **GET** /api/v1/nodes/lookup/ | 
*NodesApi* | [**api_v1_nodes_partial_update**](docs/NodesApi.md#api_v1_nodes_partial_update) | **PATCH** /api/v1/nodes/{network_number}/ | 
*NodesApi* | [**api_v1_nodes_retrieve**](docs/NodesApi.md#api_v1_nodes_retrieve) | **GET** /api/v1/nodes/{network_number}/ | 
*NodesApi* | [**api_v1_nodes_update**](docs/NodesApi.md#api_v1_nodes_update) | **PUT** /api/v1/nodes/{network_number}/ | 
*SectorsApi* | [**api_v1_sectors_create**](docs/SectorsApi.md#api_v1_sectors_create) | **POST** /api/v1/sectors/ | 
*SectorsApi* | [**api_v1_sectors_destroy**](docs/SectorsApi.md#api_v1_sectors_destroy) | **DELETE** /api/v1/sectors/{id}/ | 
*SectorsApi* | [**api_v1_sectors_list**](docs/SectorsApi.md#api_v1_sectors_list) | **GET** /api/v1/sectors/ | 
*SectorsApi* | [**api_v1_sectors_lookup_list**](docs/SectorsApi.md#api_v1_sectors_lookup_list) | **GET** /api/v1/sectors/lookup/ | 
*SectorsApi* | [**api_v1_sectors_partial_update**](docs/SectorsApi.md#api_v1_sectors_partial_update) | **PATCH** /api/v1/sectors/{id}/ | 
*SectorsApi* | [**api_v1_sectors_retrieve**](docs/SectorsApi.md#api_v1_sectors_retrieve) | **GET** /api/v1/sectors/{id}/ | 
*SectorsApi* | [**api_v1_sectors_update**](docs/SectorsApi.md#api_v1_sectors_update) | **PUT** /api/v1/sectors/{id}/ | 
*UserFormsApi* | [**api_v1_join_create**](docs/UserFormsApi.md#api_v1_join_create) | **POST** /api/v1/join/ | Register a new request for a potential mesh Install. Used by the join form posted on the nycmesh.net website
*UserFormsApi* | [**api_v1_nn_assign_create**](docs/UserFormsApi.md#api_v1_nn_assign_create) | **POST** /api/v1/nn-assign/ | Assign a network number to a given Install object. Used by the NN Assignment form
*WebsiteMapDataApi* | [**api_v1_mapdata_links_list**](docs/WebsiteMapDataApi.md#api_v1_mapdata_links_list) | **GET** /api/v1/mapdata/links/ | Complete list of all Links, unpaginated, in the format expected by the website map. (Warning: This endpoint is a legacy format and may be deprecated/removed in the future)
*WebsiteMapDataApi* | [**api_v1_mapdata_nodes_list**](docs/WebsiteMapDataApi.md#api_v1_mapdata_nodes_list) | **GET** /api/v1/mapdata/nodes/ | Complete list of all \&quot;Nodes\&quot; (mostly Installs with some fake installs generated to solve NN re-use), unpaginated, in the format expected by the website map. (Warning: This endpoint is a legacy format and may be deprecated/removed in the future)
*WebsiteMapDataApi* | [**api_v1_mapdata_sectors_list**](docs/WebsiteMapDataApi.md#api_v1_mapdata_sectors_list) | **GET** /api/v1/mapdata/sectors/ | Complete list of all Sectors, unpaginated, in the format expected by the website map. (Warning: This endpoint is a legacy format and may be deprecated/removed in the future)
*ApiApi* | [**api_v1_update_panoramas_create**](docs/ApiApi.md#api_v1_update_panoramas_create) | **POST** /api/v1/update-panoramas/ | 


## Documentation For Models

 - [AddressTruthSourcesEnum](docs/AddressTruthSourcesEnum.md)
 - [BlankEnum](docs/BlankEnum.md)
 - [Building](docs/Building.md)
 - [Device](docs/Device.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [Install](docs/Install.md)
 - [JoinFormRequest](docs/JoinFormRequest.md)
 - [JoinFormSuccessResponse](docs/JoinFormSuccessResponse.md)
 - [Link](docs/Link.md)
 - [LinkStatusEnum](docs/LinkStatusEnum.md)
 - [LinkType](docs/LinkType.md)
 - [LinkTypeEnum](docs/LinkTypeEnum.md)
 - [MapDataInstall](docs/MapDataInstall.md)
 - [MapDataLink](docs/MapDataLink.md)
 - [MapDataSector](docs/MapDataSector.md)
 - [Member](docs/Member.md)
 - [NNFormSuccessResponse](docs/NNFormSuccessResponse.md)
 - [NetworkNumberAssignmentRequest](docs/NetworkNumberAssignmentRequest.md)
 - [Node](docs/Node.md)
 - [NodeStatusEnum](docs/NodeStatusEnum.md)
 - [NodeTypeEnum](docs/NodeTypeEnum.md)
 - [NullEnum](docs/NullEnum.md)
 - [PaginatedBuildingList](docs/PaginatedBuildingList.md)
 - [PaginatedDeviceList](docs/PaginatedDeviceList.md)
 - [PaginatedInstallList](docs/PaginatedInstallList.md)
 - [PaginatedLinkList](docs/PaginatedLinkList.md)
 - [PaginatedMemberList](docs/PaginatedMemberList.md)
 - [PaginatedNodeList](docs/PaginatedNodeList.md)
 - [PaginatedQueryFormList](docs/PaginatedQueryFormList.md)
 - [PaginatedSectorList](docs/PaginatedSectorList.md)
 - [PatchedBuilding](docs/PatchedBuilding.md)
 - [PatchedDevice](docs/PatchedDevice.md)
 - [PatchedInstall](docs/PatchedInstall.md)
 - [PatchedLink](docs/PatchedLink.md)
 - [PatchedMember](docs/PatchedMember.md)
 - [PatchedNode](docs/PatchedNode.md)
 - [PatchedSector](docs/PatchedSector.md)
 - [QueryForm](docs/QueryForm.md)
 - [Sector](docs/Sector.md)
 - [Status195Enum](docs/Status195Enum.md)
 - [Status432Enum](docs/Status432Enum.md)
 - [Type75bEnum](docs/Type75bEnum.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Session ID"></a>
### Session ID

- **Type**: API key
- **API key parameter name**: sessionid
- **Location**: 

<a id="tokenAuth"></a>
### tokenAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




