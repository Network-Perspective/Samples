# ReportSyncCompletedCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_token** | **str** |  | [optional] 
**sync_period_start** | **datetime** |  | [optional] 
**sync_period_end** | **datetime** |  | [optional] 
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from np_client.models.report_sync_completed_command import ReportSyncCompletedCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ReportSyncCompletedCommand from a JSON string
report_sync_completed_command_instance = ReportSyncCompletedCommand.from_json(json)
# print the JSON string representation of the object
print ReportSyncCompletedCommand.to_json()

# convert the object into a dict
report_sync_completed_command_dict = report_sync_completed_command_instance.to_dict()
# create an instance of ReportSyncCompletedCommand from a dict
report_sync_completed_command_form_dict = report_sync_completed_command.from_dict(report_sync_completed_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


