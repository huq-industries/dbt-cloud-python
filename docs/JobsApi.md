# dbt_cloud_client.JobsApi

All URIs are relative to *https://cloud.getdbt.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_job**](JobsApi.md#create_job) | **POST** /accounts/{accountId}/jobs/ | create job on account
[**delete_job_by_id**](JobsApi.md#delete_job_by_id) | **DELETE** /accounts/{accountId}/jobs/{jobId}/ | delete job on account
[**get_job_by_id**](JobsApi.md#get_job_by_id) | **GET** /accounts/{accountId}/jobs/{jobId}/ | get specific job on account
[**list_jobs_for_account**](JobsApi.md#list_jobs_for_account) | **GET** /accounts/{accountId}/jobs/ | search or list jobs on an account
[**trigger_run**](JobsApi.md#trigger_run) | **POST** /accounts/{accountId}/jobs/{jobId}/run/ | trigger run for job
[**update_job_by_id**](JobsApi.md#update_job_by_id) | **POST** /accounts/{accountId}/jobs/{jobId}/ | update job on account

# **create_job**
> JobResponse create_job(account_id, body=body)

create job on account

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.JobsApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the account to create the new Job in
body = dbt_cloud_client.Job() # Job |  (optional)

try:
    # create job on account
    api_response = api_instance.create_job(account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->create_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the account to create the new Job in | 
 **body** | [**Job**](Job.md)|  | [optional] 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_by_id**
> JobResponse delete_job_by_id(account_id, job_id)

delete job on account

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.JobsApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the Account that the Job belongs to
job_id = 56 # int | Numeric ID of the Job to delete

try:
    # delete job on account
    api_response = api_instance.delete_job_by_id(account_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->delete_job_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the Account that the Job belongs to | 
 **job_id** | **int**| Numeric ID of the Job to delete | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_by_id**
> JobResponse get_job_by_id(account_id, job_id, order_by=order_by)

get specific job on account

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.JobsApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the account to retrieve
job_id = 56 # int | Numeric ID of the run to retrieve
order_by = 'order_by_example' # str | Field to order the result by. Use `-` to indicate reverse order.  (optional)

try:
    # get specific job on account
    api_response = api_instance.get_job_by_id(account_id, job_id, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->get_job_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the account to retrieve | 
 **job_id** | **int**| Numeric ID of the run to retrieve | 
 **order_by** | **str**| Field to order the result by. Use &#x60;-&#x60; to indicate reverse order.  | [optional] 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jobs_for_account**
> JobsResponse list_jobs_for_account(account_id, order_by=order_by)

search or list jobs on an account

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.JobsApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the account to retrieve
order_by = 'order_by_example' # str | Field to order the result by. Use `-` to indicate reverse order.  (optional)

try:
    # search or list jobs on an account
    api_response = api_instance.list_jobs_for_account(account_id, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->list_jobs_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the account to retrieve | 
 **order_by** | **str**| Field to order the result by. Use &#x60;-&#x60; to indicate reverse order.  | [optional] 

### Return type

[**JobsResponse**](JobsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_run**
> RunResponse trigger_run(account_id, job_id, body=body)

trigger run for job

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.JobsApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the Account that the Job belongs to
job_id = 56 # int | Numeric ID of the Job for which to trigger a run
body = dbt_cloud_client.Body3() # Body3 |  (optional)

try:
    # trigger run for job
    api_response = api_instance.trigger_run(account_id, job_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->trigger_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the Account that the Job belongs to | 
 **job_id** | **int**| Numeric ID of the Job for which to trigger a run | 
 **body** | [**Body3**](Body3.md)|  | [optional] 

### Return type

[**RunResponse**](RunResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job_by_id**
> JobResponse update_job_by_id(account_id, job_id, body=body)

update job on account

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.JobsApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the Account that the Job belongs to
job_id = 56 # int | Numeric ID of the Job to update
body = dbt_cloud_client.Job() # Job |  (optional)

try:
    # update job on account
    api_response = api_instance.update_job_by_id(account_id, job_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->update_job_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the Account that the Job belongs to | 
 **job_id** | **int**| Numeric ID of the Job to update | 
 **body** | [**Job**](Job.md)|  | [optional] 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

