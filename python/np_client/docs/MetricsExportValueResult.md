# MetricsExportValueResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** |  | [optional] 
**period** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**group_id** | **str** |  | [optional] 
**client_group_id** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 
**category** | **str** |  | [optional] 

## Example

```python
from np_client.models.metrics_export_value_result import MetricsExportValueResult

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsExportValueResult from a JSON string
metrics_export_value_result_instance = MetricsExportValueResult.from_json(json)
# print the JSON string representation of the object
print MetricsExportValueResult.to_json()

# convert the object into a dict
metrics_export_value_result_dict = metrics_export_value_result_instance.to_dict()
# create an instance of MetricsExportValueResult from a dict
metrics_export_value_result_form_dict = metrics_export_value_result.from_dict(metrics_export_value_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


