# HashedDataSourceCustomAttributesSettingsResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **List[str]** |  | [optional] 
**prop** | **List[str]** |  | [optional] 
**relationship** | [**List[HashedDataSourceCustomRelationshipSettingsResult]**](HashedDataSourceCustomRelationshipSettingsResult.md) |  | [optional] 

## Example

```python
from np_client.models.hashed_data_source_custom_attributes_settings_result import HashedDataSourceCustomAttributesSettingsResult

# TODO update the JSON string below
json = "{}"
# create an instance of HashedDataSourceCustomAttributesSettingsResult from a JSON string
hashed_data_source_custom_attributes_settings_result_instance = HashedDataSourceCustomAttributesSettingsResult.from_json(json)
# print the JSON string representation of the object
print HashedDataSourceCustomAttributesSettingsResult.to_json()

# convert the object into a dict
hashed_data_source_custom_attributes_settings_result_dict = hashed_data_source_custom_attributes_settings_result_instance.to_dict()
# create an instance of HashedDataSourceCustomAttributesSettingsResult from a dict
hashed_data_source_custom_attributes_settings_result_form_dict = hashed_data_source_custom_attributes_settings_result.from_dict(hashed_data_source_custom_attributes_settings_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


