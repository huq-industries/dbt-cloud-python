# dbt_cloud_client.EnvironmentsApi

All URIs are relative to *https://cloud.getdbt.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_environment**](EnvironmentsApi.md#create_environment) | **POST** /accounts/{accountId}/environments/ | create environment on account
[**delete_environment_by_id**](EnvironmentsApi.md#delete_environment_by_id) | **DELETE** /accounts/{accountId}/environments/{environmentId}/ | delete environment on account
[**get_environment_by_id**](EnvironmentsApi.md#get_environment_by_id) | **GET** /accounts/{accountId}/environments/{environmentId}/ | get specific environment on account
[**list_environments_for_account**](EnvironmentsApi.md#list_environments_for_account) | **GET** /accounts/{accountId}/environments/ | search or list environments on an account
[**update_environment_by_id**](EnvironmentsApi.md#update_environment_by_id) | **POST** /accounts/{accountId}/environments/{environmentId}/ | update environment on account

# **create_environment**
> EnvironmentResponse create_environment(account_id, body=body)

create environment on account

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.EnvironmentsApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the Account to create the new Environment in
body = dbt_cloud_client.Environment() # Environment |  (optional)

try:
    # create environment on account
    api_response = api_instance.create_environment(account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->create_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the Account to create the new Environment in | 
 **body** | [**Environment**](Environment.md)|  | [optional] 

### Return type

[**EnvironmentResponse**](EnvironmentResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_environment_by_id**
> EnvironmentResponse delete_environment_by_id(account_id, environment_id)

delete environment on account

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.EnvironmentsApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the Account that the Environment belongs to
environment_id = 56 # int | Numeric ID of the Environment to delete

try:
    # delete environment on account
    api_response = api_instance.delete_environment_by_id(account_id, environment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->delete_environment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the Account that the Environment belongs to | 
 **environment_id** | **int**| Numeric ID of the Environment to delete | 

### Return type

[**EnvironmentResponse**](EnvironmentResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_by_id**
> JobResponse get_environment_by_id(account_id, environment_id)

get specific environment on account

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.EnvironmentsApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the account to retrieve
environment_id = 56 # int | Numeric ID of the run to retrieve

try:
    # get specific environment on account
    api_response = api_instance.get_environment_by_id(account_id, environment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->get_environment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the account to retrieve | 
 **environment_id** | **int**| Numeric ID of the run to retrieve | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_environments_for_account**
> EnvironmentsResponse list_environments_for_account(account_id, order_by=order_by)

search or list environments on an account

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.EnvironmentsApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the account to retrieve
order_by = 'order_by_example' # str | Field to order the result by. Use `-` to indicate reverse order.  (optional)

try:
    # search or list environments on an account
    api_response = api_instance.list_environments_for_account(account_id, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->list_environments_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the account to retrieve | 
 **order_by** | **str**| Field to order the result by. Use &#x60;-&#x60; to indicate reverse order.  | [optional] 

### Return type

[**EnvironmentsResponse**](EnvironmentsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_environment_by_id**
> EnvironmentResponse update_environment_by_id(account_id, environment_id, body=body)

update environment on account

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.EnvironmentsApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the Account that the Environment belongs to
environment_id = 56 # int | Numeric ID of the Environment to update
body = dbt_cloud_client.Environment() # Environment |  (optional)

try:
    # update environment on account
    api_response = api_instance.update_environment_by_id(account_id, environment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->update_environment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the Account that the Environment belongs to | 
 **environment_id** | **int**| Numeric ID of the Environment to update | 
 **body** | [**Environment**](Environment.md)|  | [optional] 

### Return type

[**EnvironmentResponse**](EnvironmentResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

