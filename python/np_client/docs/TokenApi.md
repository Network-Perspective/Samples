# np_client.TokenApi

All URIs are relative to *http://host.docker.internal:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**token_get_token**](TokenApi.md#token_get_token) | **POST** /token | Issue an access token


# **token_get_token**
> TokenResponseModel token_get_token(username=username, password=password, refresh_token=refresh_token, grant_type=grant_type, client_id=client_id)

Issue an access token

### Example

* Api Key Authentication (CookieAuth):
* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import np_client
from np_client.models.token_response_model import TokenResponseModel
from np_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://host.docker.internal:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = np_client.Configuration(
    host = "http://host.docker.internal:5000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: CookieAuth
configuration.api_key['CookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CookieAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = np_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with np_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = np_client.TokenApi(api_client)
    username = 'username_example' # str |  (optional)
    password = 'password_example' # str |  (optional)
    refresh_token = 'refresh_token_example' # str |  (optional)
    grant_type = 'grant_type_example' # str |  (optional)
    client_id = 'client_id_example' # str |  (optional)

    try:
        # Issue an access token
        api_response = api_instance.token_get_token(username=username, password=password, refresh_token=refresh_token, grant_type=grant_type, client_id=client_id)
        print("The response of TokenApi->token_get_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenApi->token_get_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] 
 **password** | **str**|  | [optional] 
 **refresh_token** | **str**|  | [optional] 
 **grant_type** | **str**|  | [optional] 
 **client_id** | **str**|  | [optional] 

### Return type

[**TokenResponseModel**](TokenResponseModel.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Logged in |  -  |
**400** | Invalid credentials |  -  |
**429** | API calls quota exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

