# Sector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**network_number** | **int** |  | 
**links_from** | **List[int]** |  | [readonly] 
**links_to** | **List[int]** |  | [readonly] 
**name** | **str** | The colloquial name of this node used among mesh volunteers, if applicable | [optional] 
**model** | **str** | The manufacturer model name of this device, e.g. OmniTik or LBEGen2 | 
**type** | [**Type75bEnum**](Type75bEnum.md) | The general type of device that this is, the role it fills on the mesh. e.g. ap, ptp, station, etc. This lines up with the UISP &#39;role&#39; property  * &#x60;ap&#x60; - Ap * &#x60;gateway&#x60; - Gateway * &#x60;gpon&#x60; - Gpon * &#x60;convertor&#x60; - Convertor * &#x60;other&#x60; - Other * &#x60;ptp&#x60; - Ptp * &#x60;router&#x60; - Router * &#x60;server&#x60; - Server * &#x60;station&#x60; - Station * &#x60;switch&#x60; - Switch * &#x60;ups&#x60; - Ups * &#x60;wireless&#x60; - Wireless * &#x60;homeWiFi&#x60; - Homewifi * &#x60;wirelessDevice&#x60; - Wirelessdevice | 
**status** | [**Status432Enum**](Status432Enum.md) | The current status of this device  * &#x60;Inactive&#x60; - Inactive * &#x60;Active&#x60; - Active * &#x60;Potential&#x60; - Potential | 
**latitude** | **float** | Approximate Device latitude in decimal degrees (this will match the attached Node object in most cases, but has been manually moved around in some cases to more accurately reflect the device location) | 
**longitude** | **float** | Approximate Device longitude in decimal degrees (this will match the attached Node object in most cases, but has been manually moved around in some cases to more accurately reflect the device location) | 
**altitude** | **float** | Approximate Device altitude in \&quot;absolute\&quot; meters above mean sea level (this will match the attached Node object in most cases, but has been manually moved around in some cases to more accurately reflect the device location) | [optional] 
**install_date** | **date** | The date this device first became active on the mesh | [optional] 
**abandon_date** | **date** | The this device was abandoned, unplugged, or removed from service | [optional] 
**notes** | **str** | A free-form text description of this Device, to track any additional information. For imported Devices, this starts with a formatted block of information about the import processand original data. However this structure can be changed by admins at any time and should not be relied onby automated systems.  | [optional] 
**uisp_id** | **str** | The UUID used to indentify this device in UISP (if applicable) | [optional] 
**ssid** | **str** | The SSID being broadcast by this device | [optional] 
**ip_address** | **str** | The IP address of this device within the 10.x network | [optional] 
**radius** | **float** | The radius to display this sector on the map (in km) | 
**azimuth** | **int** | The compass heading that this sector is pointed towards | 
**width** | **int** | The approximate width of the beam this sector produces | 

## Example

```python
from pymeshdb.models.sector import Sector

# TODO update the JSON string below
json = "{}"
# create an instance of Sector from a JSON string
sector_instance = Sector.from_json(json)
# print the JSON string representation of the object
print(Sector.to_json())

# convert the object into a dict
sector_dict = sector_instance.to_dict()
# create an instance of Sector from a dict
sector_from_dict = Sector.from_dict(sector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


