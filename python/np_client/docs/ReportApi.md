# np_client.ReportApi

All URIs are relative to *http://host.docker.internal:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**report_export_metric_params**](ReportApi.md#report_export_metric_params) | **POST** /api/report/export/params | Export metric params
[**report_export_metric_related_values**](ReportApi.md#report_export_metric_related_values) | **POST** /api/report/export/related | Export related metrics
[**report_export_metric_values**](ReportApi.md#report_export_metric_values) | **POST** /api/report/export/values | Export direct metrics


# **report_export_metric_params**
> MetricsExportParamsResult report_export_metric_params(metrics_export_params_query=metrics_export_params_query)

Export metric params

### Example

* Api Key Authentication (CookieAuth):
* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import np_client
from np_client.models.metrics_export_params_query import MetricsExportParamsQuery
from np_client.models.metrics_export_params_result import MetricsExportParamsResult
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
    api_instance = np_client.ReportApi(api_client)
    metrics_export_params_query = np_client.MetricsExportParamsQuery() # MetricsExportParamsQuery |  (optional)

    try:
        # Export metric params
        api_response = api_instance.report_export_metric_params(metrics_export_params_query=metrics_export_params_query)
        print("The response of ReportApi->report_export_metric_params:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->report_export_metric_params: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metrics_export_params_query** | [**MetricsExportParamsQuery**](MetricsExportParamsQuery.md)|  | [optional] 

### Return type

[**MetricsExportParamsResult**](MetricsExportParamsResult.md)

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

# **report_export_metric_related_values**
> List[MetricRelatedExportValueResult] report_export_metric_related_values(metric_related_export_query=metric_related_export_query)

Export related metrics

### Example

* Api Key Authentication (CookieAuth):
* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import np_client
from np_client.models.metric_related_export_query import MetricRelatedExportQuery
from np_client.models.metric_related_export_value_result import MetricRelatedExportValueResult
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
    api_instance = np_client.ReportApi(api_client)
    metric_related_export_query = np_client.MetricRelatedExportQuery() # MetricRelatedExportQuery |  (optional)

    try:
        # Export related metrics
        api_response = api_instance.report_export_metric_related_values(metric_related_export_query=metric_related_export_query)
        print("The response of ReportApi->report_export_metric_related_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->report_export_metric_related_values: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_related_export_query** | [**MetricRelatedExportQuery**](MetricRelatedExportQuery.md)|  | [optional] 

### Return type

[**List[MetricRelatedExportValueResult]**](MetricRelatedExportValueResult.md)

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

# **report_export_metric_values**
> List[MetricsExportValueResult] report_export_metric_values(metrics_export_query=metrics_export_query)

Export direct metrics

### Example

* Api Key Authentication (CookieAuth):
* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import np_client
from np_client.models.metrics_export_query import MetricsExportQuery
from np_client.models.metrics_export_value_result import MetricsExportValueResult
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
    api_instance = np_client.ReportApi(api_client)
    metrics_export_query = np_client.MetricsExportQuery() # MetricsExportQuery |  (optional)

    try:
        # Export direct metrics
        api_response = api_instance.report_export_metric_values(metrics_export_query=metrics_export_query)
        print("The response of ReportApi->report_export_metric_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->report_export_metric_values: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metrics_export_query** | [**MetricsExportQuery**](MetricsExportQuery.md)|  | [optional] 

### Return type

[**List[MetricsExportValueResult]**](MetricsExportValueResult.md)

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

