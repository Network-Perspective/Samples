# SyncHashedInteractionsCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_token** | **str** |  | [optional] 
**interactions** | [**List[HashedInteraction]**](HashedInteraction.md) |  | [optional] 

## Example

```python
from np_client.models.sync_hashed_interactions_command import SyncHashedInteractionsCommand

# TODO update the JSON string below
json = "{}"
# create an instance of SyncHashedInteractionsCommand from a JSON string
sync_hashed_interactions_command_instance = SyncHashedInteractionsCommand.from_json(json)
# print the JSON string representation of the object
print SyncHashedInteractionsCommand.to_json()

# convert the object into a dict
sync_hashed_interactions_command_dict = sync_hashed_interactions_command_instance.to_dict()
# create an instance of SyncHashedInteractionsCommand from a dict
sync_hashed_interactions_command_form_dict = sync_hashed_interactions_command.from_dict(sync_hashed_interactions_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


