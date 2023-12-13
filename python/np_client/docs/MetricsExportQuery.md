# MetricsExportQuery


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_id** | **str** |  | [optional] 
**aggregate** | [**AggregateEnum**](AggregateEnum.md) |  | [optional] 
**periods** | **List[str]** |  | [optional] 
**metrics** | **List[str]** |  | [optional] 

## Example

```python
from np_client.models.metrics_export_query import MetricsExportQuery

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsExportQuery from a JSON string
metrics_export_query_instance = MetricsExportQuery.from_json(json)
# print the JSON string representation of the object
print MetricsExportQuery.to_json()

# convert the object into a dict
metrics_export_query_dict = metrics_export_query_instance.to_dict()
# create an instance of MetricsExportQuery from a dict
metrics_export_query_form_dict = metrics_export_query.from_dict(metrics_export_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


