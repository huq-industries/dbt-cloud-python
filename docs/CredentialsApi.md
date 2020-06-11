# dbt_cloud_client.CredentialsApi

All URIs are relative to *https://cloud.getdbt.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_credentials**](CredentialsApi.md#create_credentials) | **POST** /accounts/{accountId}/credentials/ | create credentials on account
[**list_credentials_for_account**](CredentialsApi.md#list_credentials_for_account) | **GET** /accounts/{accountId}/credentials/ | search or list credentials on an account

# **create_credentials**
> CredentialsResponse create_credentials(account_id, body=body)

create credentials on account

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.CredentialsApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the account to create the new Credentials in
body = dbt_cloud_client.Body() # Body |  (optional)

try:
    # create credentials on account
    api_response = api_instance.create_credentials(account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->create_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the account to create the new Credentials in | 
 **body** | [**Body**](Body.md)|  | [optional] 

### Return type

[**CredentialsResponse**](CredentialsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_credentials_for_account**
> CredentialsResponse list_credentials_for_account(account_id)

search or list credentials on an account

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.CredentialsApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the account to retrieve

try:
    # search or list credentials on an account
    api_response = api_instance.list_credentials_for_account(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->list_credentials_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the account to retrieve | 

### Return type

[**CredentialsResponse**](CredentialsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

