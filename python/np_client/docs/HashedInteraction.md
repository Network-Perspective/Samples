# HashedInteraction



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interaction_id** | **str** |  | [optional] 
**when** | **datetime** |  | [optional] 
**source_ids** | **Dict[str, str]** |  | [optional] 
**target_ids** | **Dict[str, str]** |  | [optional] 
**event_id** | **str** |  | [optional] 
**parent_event_id** | **str** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**duration_minutes** | **int** |  | [optional] 
**label** | [**List[HashedInteractionLabel]**](HashedInteractionLabel.md) |  | [optional] 

## Example

```python
from np_client.models.hashed_interaction import HashedInteraction

# TODO update the JSON string below
json = "{}"
# create an instance of HashedInteraction from a JSON string
hashed_interaction_instance = HashedInteraction.from_json(json)
# print the JSON string representation of the object
print HashedInteraction.to_json()

# convert the object into a dict
hashed_interaction_dict = hashed_interaction_instance.to_dict()
# create an instance of HashedInteraction from a dict
hashed_interaction_form_dict = hashed_interaction.from_dict(hashed_interaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


