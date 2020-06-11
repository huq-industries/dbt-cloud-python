# dbt_cloud_client.RepositoriesApi

All URIs are relative to *https://cloud.getdbt.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_repository**](RepositoriesApi.md#create_repository) | **POST** /accounts/{accountId}/repositories/ | create repository on account
[**get_repository_by_id**](RepositoriesApi.md#get_repository_by_id) | **GET** /accounts/{accountId}/repositories/{repositoryId}/ | get specific repository on account
[**list_repositories_for_account**](RepositoriesApi.md#list_repositories_for_account) | **GET** /accounts/{accountId}/repositories/ | search or list repositories on an account

# **create_repository**
> RepositoryResponse create_repository(account_id, body=body)

create repository on account

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.RepositoriesApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the account to create the new Connection in
body = dbt_cloud_client.Body4() # Body4 |  (optional)

try:
    # create repository on account
    api_response = api_instance.create_repository(account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->create_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the account to create the new Connection in | 
 **body** | [**Body4**](Body4.md)|  | [optional] 

### Return type

[**RepositoryResponse**](RepositoryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository_by_id**
> RepositoryResponse get_repository_by_id(account_id, repository_id)

get specific repository on account

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.RepositoriesApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the account to retrieve
repository_id = 56 # int | Numeric ID of the repository to retrieve

try:
    # get specific repository on account
    api_response = api_instance.get_repository_by_id(account_id, repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_repository_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the account to retrieve | 
 **repository_id** | **int**| Numeric ID of the repository to retrieve | 

### Return type

[**RepositoryResponse**](RepositoryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_repositories_for_account**
> RepositoriesResponse list_repositories_for_account(account_id)

search or list repositories on an account

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.RepositoriesApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the account to retrieve

try:
    # search or list repositories on an account
    api_response = api_instance.list_repositories_for_account(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->list_repositories_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the account to retrieve | 

### Return type

[**RepositoriesResponse**](RepositoriesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

