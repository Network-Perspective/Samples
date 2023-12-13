# MetricsExportParamsQuery


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_id** | **str** |  | [optional] 
**aggregate** | [**AggregateEnum**](AggregateEnum.md) |  | [optional] 

## Example

```python
from np_client.models.metrics_export_params_query import MetricsExportParamsQuery

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsExportParamsQuery from a JSON string
metrics_export_params_query_instance = MetricsExportParamsQuery.from_json(json)
# print the JSON string representation of the object
print MetricsExportParamsQuery.to_json()

# convert the object into a dict
metrics_export_params_query_dict = metrics_export_params_query_instance.to_dict()
# create an instance of MetricsExportParamsQuery from a dict
metrics_export_params_query_form_dict = metrics_export_params_query.from_dict(metrics_export_params_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


