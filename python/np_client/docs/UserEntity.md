# UserEntity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**ids** | **Dict[str, str]** |  | [optional] 
**props** | **Dict[str, object]** |  | [optional] 
**group_access** | **List[str]** |  | [optional] 

## Example

```python
from np_client.models.user_entity import UserEntity

# TODO update the JSON string below
json = "{}"
# create an instance of UserEntity from a JSON string
user_entity_instance = UserEntity.from_json(json)
# print the JSON string representation of the object
print UserEntity.to_json()

# convert the object into a dict
user_entity_dict = user_entity_instance.to_dict()
# create an instance of UserEntity from a dict
user_entity_form_dict = user_entity.from_dict(user_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


