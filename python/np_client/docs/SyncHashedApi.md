# np_client.SyncHashedApi

All URIs are relative to *http://host.docker.internal:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sync_hashed_query**](SyncHashedApi.md#sync_hashed_query) | **GET** /api/sync/hashed/token | Validate service token
[**sync_hashed_report_completed**](SyncHashedApi.md#sync_hashed_report_completed) | **POST** /api/sync/hashed/completed | Sync completed
[**sync_hashed_report_start**](SyncHashedApi.md#sync_hashed_report_start) | **POST** /api/sync/hashed/start | Sync started
[**sync_hashed_settings**](SyncHashedApi.md#sync_hashed_settings) | **POST** /api/sync/hashed/settings | Settings
[**sync_hashed_sync_entities**](SyncHashedApi.md#sync_hashed_sync_entities) | **POST** /api/sync/hashed/entities | Sync entities
[**sync_hashed_sync_groups**](SyncHashedApi.md#sync_hashed_sync_groups) | **POST** /api/sync/hashed/groups | Sync groups
[**sync_hashed_sync_interactions**](SyncHashedApi.md#sync_hashed_sync_interactions) | **POST** /api/sync/hashed/interactions | Sync interactions
[**sync_hashed_sync_users**](SyncHashedApi.md#sync_hashed_sync_users) | **POST** /api/sync/hashed/users | Sync users


# **sync_hashed_query**
> ServiceResult sync_hashed_query(service_token=service_token)

Validate service token

### Example

* Api Key Authentication (CookieAuth):
* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import np_client
from np_client.models.service_result import ServiceResult
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
    api_instance = np_client.SyncHashedApi(api_client)
    service_token = 'service_token_example' # str |  (optional)

    try:
        # Validate service token
        api_response = api_instance.sync_hashed_query(service_token=service_token)
        print("The response of SyncHashedApi->sync_hashed_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyncHashedApi->sync_hashed_query: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_token** | **str**|  | [optional] 

### Return type

[**ServiceResult**](ServiceResult.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Model validation error |  -  |
**429** | API calls quota exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_hashed_report_completed**
> sync_hashed_report_completed(report_sync_completed_command=report_sync_completed_command)

Sync completed

Connector should call this endpoint when synchronization has completed or failed

### Example

* Api Key Authentication (CookieAuth):
* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import np_client
from np_client.models.report_sync_completed_command import ReportSyncCompletedCommand
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
    api_instance = np_client.SyncHashedApi(api_client)
    report_sync_completed_command = np_client.ReportSyncCompletedCommand() # ReportSyncCompletedCommand |  (optional)

    try:
        # Sync completed
        api_instance.sync_hashed_report_completed(report_sync_completed_command=report_sync_completed_command)
    except Exception as e:
        print("Exception when calling SyncHashedApi->sync_hashed_report_completed: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_sync_completed_command** | [**ReportSyncCompletedCommand**](ReportSyncCompletedCommand.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[CookieAuth](../README.md#CookieAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Model validation error |  -  |
**429** | API calls quota exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_hashed_report_start**
> sync_hashed_report_start(report_sync_started_command=report_sync_started_command)

Sync started

Connector should call this endpoint when starting synchronization job

### Example

* Api Key Authentication (CookieAuth):
* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import np_client
from np_client.models.report_sync_started_command import ReportSyncStartedCommand
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
    api_instance = np_client.SyncHashedApi(api_client)
    report_sync_started_command = np_client.ReportSyncStartedCommand() # ReportSyncStartedCommand |  (optional)

    try:
        # Sync started
        api_instance.sync_hashed_report_start(report_sync_started_command=report_sync_started_command)
    except Exception as e:
        print("Exception when calling SyncHashedApi->sync_hashed_report_start: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_sync_started_command** | [**ReportSyncStartedCommand**](ReportSyncStartedCommand.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[CookieAuth](../README.md#CookieAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Model validation error |  -  |
**429** | API calls quota exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_hashed_settings**
> HashedDataSourceSettingsResult sync_hashed_settings(service_token=service_token)

Settings

Returns synchronization settings common for all connectors

### Example

* Api Key Authentication (CookieAuth):
* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import np_client
from np_client.models.hashed_data_source_settings_result import HashedDataSourceSettingsResult
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
    api_instance = np_client.SyncHashedApi(api_client)
    service_token = 'service_token_example' # str |  (optional)

    try:
        # Settings
        api_response = api_instance.sync_hashed_settings(service_token=service_token)
        print("The response of SyncHashedApi->sync_hashed_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyncHashedApi->sync_hashed_settings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_token** | **str**|  | [optional] 

### Return type

[**HashedDataSourceSettingsResult**](HashedDataSourceSettingsResult.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Model validation error |  -  |
**429** | API calls quota exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_hashed_sync_entities**
> str sync_hashed_sync_entities(sync_hashed_entites_command=sync_hashed_entites_command)

Sync entities

Sync nodes in graph.  Keys, Groups, Props should be hashed or bucketed befored sending

### Example

* Api Key Authentication (CookieAuth):
* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import np_client
from np_client.models.sync_hashed_entites_command import SyncHashedEntitesCommand
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
    api_instance = np_client.SyncHashedApi(api_client)
    sync_hashed_entites_command = np_client.SyncHashedEntitesCommand() # SyncHashedEntitesCommand |  (optional)

    try:
        # Sync entities
        api_response = api_instance.sync_hashed_sync_entities(sync_hashed_entites_command=sync_hashed_entites_command)
        print("The response of SyncHashedApi->sync_hashed_sync_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyncHashedApi->sync_hashed_sync_entities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_hashed_entites_command** | [**SyncHashedEntitesCommand**](SyncHashedEntitesCommand.md)|  | [optional] 

### Return type

**str**

### Authorization

[CookieAuth](../README.md#CookieAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Model validation error |  -  |
**429** | API calls quota exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_hashed_sync_groups**
> str sync_hashed_sync_groups(sync_hashed_group_structure_command=sync_hashed_group_structure_command)

Sync groups

Sync group names and hierarchy for reports available in user interface

### Example

* Api Key Authentication (CookieAuth):
* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import np_client
from np_client.models.sync_hashed_group_structure_command import SyncHashedGroupStructureCommand
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
    api_instance = np_client.SyncHashedApi(api_client)
    sync_hashed_group_structure_command = np_client.SyncHashedGroupStructureCommand() # SyncHashedGroupStructureCommand |  (optional)

    try:
        # Sync groups
        api_response = api_instance.sync_hashed_sync_groups(sync_hashed_group_structure_command=sync_hashed_group_structure_command)
        print("The response of SyncHashedApi->sync_hashed_sync_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyncHashedApi->sync_hashed_sync_groups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_hashed_group_structure_command** | [**SyncHashedGroupStructureCommand**](SyncHashedGroupStructureCommand.md)|  | [optional] 

### Return type

**str**

### Authorization

[CookieAuth](../README.md#CookieAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Model validation error |  -  |
**429** | API calls quota exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_hashed_sync_interactions**
> str sync_hashed_sync_interactions(sync_hashed_interactions_command=sync_hashed_interactions_command)

Sync interactions

Sync interactions between nodes in graph

### Example

* Api Key Authentication (CookieAuth):
* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import np_client
from np_client.models.sync_hashed_interactions_command import SyncHashedInteractionsCommand
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
    api_instance = np_client.SyncHashedApi(api_client)
    sync_hashed_interactions_command = np_client.SyncHashedInteractionsCommand() # SyncHashedInteractionsCommand |  (optional)

    try:
        # Sync interactions
        api_response = api_instance.sync_hashed_sync_interactions(sync_hashed_interactions_command=sync_hashed_interactions_command)
        print("The response of SyncHashedApi->sync_hashed_sync_interactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyncHashedApi->sync_hashed_sync_interactions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_hashed_interactions_command** | [**SyncHashedInteractionsCommand**](SyncHashedInteractionsCommand.md)|  | [optional] 

### Return type

**str**

### Authorization

[CookieAuth](../README.md#CookieAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Model validation error |  -  |
**429** | API calls quota exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_hashed_sync_users**
> str sync_hashed_sync_users(sync_users_command=sync_users_command)

Sync users

Syncs not hashed list of users that might have access to the application  (Permissions are to be assigned by the administrator)

### Example

* Api Key Authentication (CookieAuth):
* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import np_client
from np_client.models.sync_users_command import SyncUsersCommand
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
    api_instance = np_client.SyncHashedApi(api_client)
    sync_users_command = np_client.SyncUsersCommand() # SyncUsersCommand |  (optional)

    try:
        # Sync users
        api_response = api_instance.sync_hashed_sync_users(sync_users_command=sync_users_command)
        print("The response of SyncHashedApi->sync_hashed_sync_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyncHashedApi->sync_hashed_sync_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_users_command** | [**SyncUsersCommand**](SyncUsersCommand.md)|  | [optional] 

### Return type

**str**

### Authorization

[CookieAuth](../README.md#CookieAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Model validation error |  -  |
**429** | API calls quota exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

