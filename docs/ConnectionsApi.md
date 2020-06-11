# dbt_cloud_client.ConnectionsApi

All URIs are relative to *https://cloud.getdbt.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connection**](ConnectionsApi.md#create_connection) | **POST** /accounts/{accountId}/connections/ | create connection on account
[**delete_connection_by_id**](ConnectionsApi.md#delete_connection_by_id) | **DELETE** /accounts/{accountId}/connections/{connectionId}/ | delete connection on account
[**get_connection_by_id**](ConnectionsApi.md#get_connection_by_id) | **GET** /accounts/{accountId}/connections/{connectionId}/ | get specific connection on account
[**list_connections_for_account**](ConnectionsApi.md#list_connections_for_account) | **GET** /accounts/{accountId}/connections/ | search or list connections on an account
[**update_connection_by_id**](ConnectionsApi.md#update_connection_by_id) | **POST** /accounts/{accountId}/connections/{connectionId}/ | update connection on account

# **create_connection**
> ConnectionResponse create_connection(account_id, body=body)

create connection on account

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.ConnectionsApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the account to create the new Connection in
body = dbt_cloud_client.Body1() # Body1 |  (optional)

try:
    # create connection on account
    api_response = api_instance.create_connection(account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->create_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the account to create the new Connection in | 
 **body** | [**Body1**](Body1.md)|  | [optional] 

### Return type

[**ConnectionResponse**](ConnectionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection_by_id**
> ConnectionResponse delete_connection_by_id(account_id, connection_id)

delete connection on account

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.ConnectionsApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the Account that the Connection belongs to
connection_id = 56 # int | Numeric ID of the Connection to delete

try:
    # delete connection on account
    api_response = api_instance.delete_connection_by_id(account_id, connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->delete_connection_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the Account that the Connection belongs to | 
 **connection_id** | **int**| Numeric ID of the Connection to delete | 

### Return type

[**ConnectionResponse**](ConnectionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_by_id**
> ConnectionResponse get_connection_by_id(account_id, connection_id)

get specific connection on account

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.ConnectionsApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the account to retrieve
connection_id = 56 # int | Numeric ID of the connection to retrieve

try:
    # get specific connection on account
    api_response = api_instance.get_connection_by_id(account_id, connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->get_connection_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the account to retrieve | 
 **connection_id** | **int**| Numeric ID of the connection to retrieve | 

### Return type

[**ConnectionResponse**](ConnectionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connections_for_account**
> ConnectionsResponse list_connections_for_account(account_id, order_by=order_by)

search or list connections on an account

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.ConnectionsApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the account to retrieve
order_by = 'order_by_example' # str | Field to order the result by. Use `-` to indicate reverse order.  (optional)

try:
    # search or list connections on an account
    api_response = api_instance.list_connections_for_account(account_id, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->list_connections_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the account to retrieve | 
 **order_by** | **str**| Field to order the result by. Use &#x60;-&#x60; to indicate reverse order.  | [optional] 

### Return type

[**ConnectionsResponse**](ConnectionsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connection_by_id**
> ConnectionResponse update_connection_by_id(account_id, connection_id, body=body)

update connection on account

### Example
```python
from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = dbt_cloud_client.ConnectionsApi(dbt_cloud_client.ApiClient(configuration))
account_id = 56 # int | Numeric ID of the Account that the Job belongs to
connection_id = 56 # int | Numeric ID of the Job to update
body = dbt_cloud_client.Body2() # Body2 |  (optional)

try:
    # update connection on account
    api_response = api_instance.update_connection_by_id(account_id, connection_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->update_connection_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Numeric ID of the Account that the Job belongs to | 
 **connection_id** | **int**| Numeric ID of the Job to update | 
 **body** | [**Body2**](Body2.md)|  | [optional] 

### Return type

[**ConnectionResponse**](ConnectionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

