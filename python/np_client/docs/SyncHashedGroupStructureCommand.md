# SyncHashedGroupStructureCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_token** | **str** |  | [optional] 
**groups** | [**List[HashedGroup]**](HashedGroup.md) |  | [optional] 

## Example

```python
from np_client.models.sync_hashed_group_structure_command import SyncHashedGroupStructureCommand

# TODO update the JSON string below
json = "{}"
# create an instance of SyncHashedGroupStructureCommand from a JSON string
sync_hashed_group_structure_command_instance = SyncHashedGroupStructureCommand.from_json(json)
# print the JSON string representation of the object
print SyncHashedGroupStructureCommand.to_json()

# convert the object into a dict
sync_hashed_group_structure_command_dict = sync_hashed_group_structure_command_instance.to_dict()
# create an instance of SyncHashedGroupStructureCommand from a dict
sync_hashed_group_structure_command_form_dict = sync_hashed_group_structure_command.from_dict(sync_hashed_group_structure_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


