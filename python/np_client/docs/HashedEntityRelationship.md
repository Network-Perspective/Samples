# HashedEntityRelationship


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relationship_name** | **str** |  | [optional] 
**target_ids** | **Dict[str, str]** |  | [optional] 

## Example

```python
from np_client.models.hashed_entity_relationship import HashedEntityRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of HashedEntityRelationship from a JSON string
hashed_entity_relationship_instance = HashedEntityRelationship.from_json(json)
# print the JSON string representation of the object
print HashedEntityRelationship.to_json()

# convert the object into a dict
hashed_entity_relationship_dict = hashed_entity_relationship_instance.to_dict()
# create an instance of HashedEntityRelationship from a dict
hashed_entity_relationship_form_dict = hashed_entity_relationship.from_dict(hashed_entity_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


