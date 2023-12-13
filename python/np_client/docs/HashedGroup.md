# HashedGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**client_group_id** | **str** | Id available in data export | [optional] 
**name** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 

## Example

```python
from np_client.models.hashed_group import HashedGroup

# TODO update the JSON string below
json = "{}"
# create an instance of HashedGroup from a JSON string
hashed_group_instance = HashedGroup.from_json(json)
# print the JSON string representation of the object
print HashedGroup.to_json()

# convert the object into a dict
hashed_group_dict = hashed_group_instance.to_dict()
# create an instance of HashedGroup from a dict
hashed_group_form_dict = hashed_group.from_dict(hashed_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


