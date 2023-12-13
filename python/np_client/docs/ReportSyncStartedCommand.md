# ReportSyncStartedCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_token** | **str** |  | [optional] 
**sync_period_start** | **datetime** |  | [optional] 
**sync_period_end** | **datetime** |  | [optional] 

## Example

```python
from np_client.models.report_sync_started_command import ReportSyncStartedCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ReportSyncStartedCommand from a JSON string
report_sync_started_command_instance = ReportSyncStartedCommand.from_json(json)
# print the JSON string representation of the object
print ReportSyncStartedCommand.to_json()

# convert the object into a dict
report_sync_started_command_dict = report_sync_started_command_instance.to_dict()
# create an instance of ReportSyncStartedCommand from a dict
report_sync_started_command_form_dict = report_sync_started_command.from_dict(report_sync_started_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


