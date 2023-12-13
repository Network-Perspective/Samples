# HashedDataSourceSettingsResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**whitelist** | **List[str]** |  | [optional] 
**blacklist** | **List[str]** |  | [optional] 
**custom_attributes** | [**HashedDataSourceCustomAttributesSettingsResult**](HashedDataSourceCustomAttributesSettingsResult.md) |  | [optional] 

## Example

```python
from np_client.models.hashed_data_source_settings_result import HashedDataSourceSettingsResult

# TODO update the JSON string below
json = "{}"
# create an instance of HashedDataSourceSettingsResult from a JSON string
hashed_data_source_settings_result_instance = HashedDataSourceSettingsResult.from_json(json)
# print the JSON string representation of the object
print HashedDataSourceSettingsResult.to_json()

# convert the object into a dict
hashed_data_source_settings_result_dict = hashed_data_source_settings_result_instance.to_dict()
# create an instance of HashedDataSourceSettingsResult from a dict
hashed_data_source_settings_result_form_dict = hashed_data_source_settings_result.from_dict(hashed_data_source_settings_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


