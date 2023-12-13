# MetricsExportParamsResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**periods** | **List[str]** |  | [optional] 
**metrics** | **List[str]** |  | [optional] 
**related_metrics** | **List[str]** |  | [optional] 
**categories** | **List[str]** |  | [optional] 

## Example

```python
from np_client.models.metrics_export_params_result import MetricsExportParamsResult

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsExportParamsResult from a JSON string
metrics_export_params_result_instance = MetricsExportParamsResult.from_json(json)
# print the JSON string representation of the object
print MetricsExportParamsResult.to_json()

# convert the object into a dict
metrics_export_params_result_dict = metrics_export_params_result_instance.to_dict()
# create an instance of MetricsExportParamsResult from a dict
metrics_export_params_result_form_dict = metrics_export_params_result.from_dict(metrics_export_params_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


