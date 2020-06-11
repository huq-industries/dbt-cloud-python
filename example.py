from __future__ import print_function
import time
import dbt_cloud_client
from dbt_cloud_client.rest import ApiException
from pprint import pprint

API_KEY = ''

# create an instance of the API class
accounts_api_instance = dbt_cloud_client.AccountsApi(
    dbt_cloud_client.ApiClient(
        configuration=None,
        header_name='Authorization',
        header_value=f'Token {API_KEY}'
        )
    )

jobs_api_instance = dbt_cloud_client.JobsApi(
    dbt_cloud_client.ApiClient(
        configuration=None,
        header_name='Authorization',
        header_value=f'Token {API_KEY}'
        )
    )

account_id = 56 # int | Numeric ID of the account to retrieve

try:
    # get account by id
    api_response = accounts_api_instance.get_account_by_id(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account_by_id: %s\n" % e)

try:
    # search or list accounts
    api_response = accounts_api_instance.list_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->list_accounts: %s\n" % e)

job_id = 0
try:
    # search or list accounts
    api_response = jobs_api_instance.get_job_by_id(account_id=account_id, job_id=job_id) 
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->get_job_by_id: %s\n" % e)
