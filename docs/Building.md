# Building

A  ModelSerializer MixIn which sets `NestedKeyObjectRelatedField` as the default field class to use for the foreign key fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**installs** | [**List[BuildingInstallsInner]**](BuildingInstallsInner.md) |  | [readonly] 
**bin** | **int** | NYC DOB Identifier for the structure containing this building | [optional] 
**street_address** | **str** | Line 1 only of the address of this building: i.e. &lt;house num&gt; &lt;street&gt; | [optional] 
**city** | **str** | The name of the borough this building is in for buildings within NYC, \&quot;New York\&quot; for Manhattan to match street addresses. The actual city name for anything outside NYC | [optional] 
**state** | **str** | The 2 letter abreviation of the US State this building is contained within, e.g. \&quot;NY\&quot; or \&quot;NJ\&quot; | [optional] 
**zip_code** | **str** | The five digit ZIP code this building is contained within | [optional] 
**address_truth_sources** | [**List[AddressTruthSourcesEnum]**](AddressTruthSourcesEnum.md) | A list of strings that answers the question: How was the content of the street address, city, state, and ZIP fields determined? This is useful in understanding the level of validation applied to spreadsheet imported data. Possible values are: OSMNominatim, OSMNominatimZIPOnly, NYCPlanningLabs, PeliasStringParsing, ReverseGeocodeFromCoordinates, HumanEntry. Check the import script for details | 
**latitude** | **float** | Building latitude in decimal degrees | 
**longitude** | **float** | Building longitude in decimal degrees | 
**altitude** | **float** | Building rooftop altitude in \&quot;absolute\&quot; meters above mean sea level | [optional] 
**notes** | **str** | A free-form text description of this building, to track any additional information. For Buidings imported from the spreadsheet, this starts with a formatted block of information about the import process and original spreadsheet data. However this structure can be changed by admins at any time and should not be relied on by automated systems.  | [optional] 
**panoramas** | **List[str]** | Panoramas taken from the roof of this Building | [optional] 
**primary_node** | [**BuildingPrimaryNode**](BuildingPrimaryNode.md) |  | [optional] 
**nodes** | [**List[BuildingNodesInner]**](BuildingNodesInner.md) | All nodes located on the same structure (i.e. a discrete man-made place identified by the same BIN) that this Building is located within. | [optional] 

## Example

```python
from pymeshdb.models.building import Building

# TODO update the JSON string below
json = "{}"
# create an instance of Building from a JSON string
building_instance = Building.from_json(json)
# print the JSON string representation of the object
print(Building.to_json())

# convert the object into a dict
building_dict = building_instance.to_dict()
# create an instance of Building from a dict
building_from_dict = Building.from_dict(building_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


