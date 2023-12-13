# SyncUsersCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_token** | **str** |  | [optional] 
**users** | [**List[UserEntity]**](UserEntity.md) |  | [optional] 
**instant** | **bool** |  | [optional] 

## Example

```python
from np_client.models.sync_users_command import SyncUsersCommand

# TODO update the JSON string below
json = "{}"
# create an instance of SyncUsersCommand from a JSON string
sync_users_command_instance = SyncUsersCommand.from_json(json)
# print the JSON string representation of the object
print SyncUsersCommand.to_json()

# convert the object into a dict
sync_users_command_dict = sync_users_command_instance.to_dict()
# create an instance of SyncUsersCommand from a dict
sync_users_command_form_dict = sync_users_command.from_dict(sync_users_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


