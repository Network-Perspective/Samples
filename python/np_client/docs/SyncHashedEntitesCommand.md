# SyncHashedEntitesCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_token** | **str** |  | [optional] 
**entites** | [**List[HashedEntity]**](HashedEntity.md) |  | [optional] 

## Example

```python
from np_client.models.sync_hashed_entites_command import SyncHashedEntitesCommand

# TODO update the JSON string below
json = "{}"
# create an instance of SyncHashedEntitesCommand from a JSON string
sync_hashed_entites_command_instance = SyncHashedEntitesCommand.from_json(json)
# print the JSON string representation of the object
print SyncHashedEntitesCommand.to_json()

# convert the object into a dict
sync_hashed_entites_command_dict = sync_hashed_entites_command_instance.to_dict()
# create an instance of SyncHashedEntitesCommand from a dict
sync_hashed_entites_command_form_dict = sync_hashed_entites_command.from_dict(sync_hashed_entites_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


