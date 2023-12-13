# MetricRelatedExportValueResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**group_id** | **str** |  | [optional] 
**client_group_id** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 
**related_group_id** | **str** |  | [optional] 
**related_client_group_id** | **str** |  | [optional] 
**related_group_name** | **str** |  | [optional] 
**category** | **str** |  | [optional] 

## Example

```python
from np_client.models.metric_related_export_value_result import MetricRelatedExportValueResult

# TODO update the JSON string below
json = "{}"
# create an instance of MetricRelatedExportValueResult from a JSON string
metric_related_export_value_result_instance = MetricRelatedExportValueResult.from_json(json)
# print the JSON string representation of the object
print MetricRelatedExportValueResult.to_json()

# convert the object into a dict
metric_related_export_value_result_dict = metric_related_export_value_result_instance.to_dict()
# create an instance of MetricRelatedExportValueResult from a dict
metric_related_export_value_result_form_dict = metric_related_export_value_result.from_dict(metric_related_export_value_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


