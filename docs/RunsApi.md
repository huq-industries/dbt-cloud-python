# dbt_cloud_client.RunsApi

All URIs are relative to *https://cloud.getdbt.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_run_by_id**](RunsApi.md#cancel_run_by_id) | **POST** /accounts/{accountId}/runs/{runId}/cancel/ | cancel specific run on account
[**get_run_by_id**](RunsApi.md#get_run_by_id) | **GET** /accounts/{accountId}/runs/{runId}/ | get specific run on account
[**list_runs_for_account**](RunsApi.md#list_runs_for_account) | **GET** /accounts/{accountId}/runs/ | search or list runs for an account

# **cancel_run_by_id**
> RunResponse cancel_run_by_id(account_id, run_id)

cancel specific run on account

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.RunsApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the account for this run
run_id = 56 # int | Numeric ID of the run to cancel

try:
    # cancel specific run on account
    api_response = api_instance.cancel_run_by_id(account_id, run_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunsApi->cancel_run_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the account for this run | 
 **run_id** | **int**| Numeric ID of the run to cancel | 

### Return type

[**RunResponse**](RunResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_by_id**
> RunResponse get_run_by_id(account_id, run_id, include_related=include_related)

get specific run on account

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.RunsApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the account to retrieve
run_id = 56 # int | Numeric ID of the run to retrieve
include_related = 'include_related_example' # str | List of related fields to pull with the run. Valid values are  \"trigger\" and \"job\".  (optional)

try:
    # get specific run on account
    api_response = api_instance.get_run_by_id(account_id, run_id, include_related=include_related)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunsApi->get_run_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the account to retrieve | 
 **run_id** | **int**| Numeric ID of the run to retrieve | 
 **include_related** | **str**| List of related fields to pull with the run. Valid values are  \&quot;trigger\&quot; and \&quot;job\&quot;.  | [optional] 

### Return type

[**RunResponse**](RunResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_runs_for_account**
> RunsResponse list_runs_for_account(account_id, include_related, order_by=order_by)

search or list runs for an account

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.RunsApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the account to retrieve
include_related = 'include_related_example' # str | List of related fields to pull with the run. Valid values are  \"trigger\" and \"job\". 
order_by = 'order_by_example' # str | Field to order the result by. Use `-` to indicate reverse order.  (optional)

try:
    # search or list runs for an account
    api_response = api_instance.list_runs_for_account(account_id, include_related, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunsApi->list_runs_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the account to retrieve | 
 **include_related** | **str**| List of related fields to pull with the run. Valid values are  \&quot;trigger\&quot; and \&quot;job\&quot;.  | 
 **order_by** | **str**| Field to order the result by. Use &#x60;-&#x60; to indicate reverse order.  | [optional] 

### Return type

[**RunsResponse**](RunsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

