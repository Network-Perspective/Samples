# HashedEntity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_date** | **datetime** |  | [optional] 
**ids** | **Dict[str, str]** |  | [optional] 
**groups** | **List[str]** |  | [optional] 
**props** | **Dict[str, object]** |  | [optional] 
**relationships** | [**List[HashedEntityRelationship]**](HashedEntityRelationship.md) |  | [optional] 

## Example

```python
from np_client.models.hashed_entity import HashedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of HashedEntity from a JSON string
hashed_entity_instance = HashedEntity.from_json(json)
# print the JSON string representation of the object
print HashedEntity.to_json()

# convert the object into a dict
hashed_entity_dict = hashed_entity_instance.to_dict()
# create an instance of HashedEntity from a dict
hashed_entity_form_dict = hashed_entity.from_dict(hashed_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


