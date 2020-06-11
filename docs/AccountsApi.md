# dbt_cloud_client.AccountsApi

All URIs are relative to *https://cloud.getdbt.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_by_id**](AccountsApi.md#get_account_by_id) | **GET** /accounts/{accountId}/ | get account by id
[**list_accounts**](AccountsApi.md#list_accounts) | **GET** /accounts/ | search or list accounts

# **get_account_by_id**
> AccountResponse get_account_by_id(account_id)

get account by id

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.AccountsApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the account to retrieve

try:
    # get account by id
    api_response = api_instance.get_account_by_id(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the account to retrieve | 

### Return type

[**AccountResponse**](AccountResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_accounts**
> AccountsResponse list_accounts()

search or list accounts

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.AccountsApi(dbt_cloud_client.ApiClient(configuration))

try:
    # search or list accounts
    api_response = api_instance.list_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->list_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountsResponse**](AccountsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

