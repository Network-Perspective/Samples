# MetricRelatedExportQuery


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** |  | [optional] 
**network_id** | **str** |  | [optional] 
**aggregate** | [**AggregateEnum**](AggregateEnum.md) |  | [optional] 
**top** | **int** |  | [optional] 

## Example

```python
from np_client.models.metric_related_export_query import MetricRelatedExportQuery

# TODO update the JSON string below
json = "{}"
# create an instance of MetricRelatedExportQuery from a JSON string
metric_related_export_query_instance = MetricRelatedExportQuery.from_json(json)
# print the JSON string representation of the object
print MetricRelatedExportQuery.to_json()

# convert the object into a dict
metric_related_export_query_dict = metric_related_export_query_instance.to_dict()
# create an instance of MetricRelatedExportQuery from a dict
metric_related_export_query_form_dict = metric_related_export_query.from_dict(metric_related_export_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


