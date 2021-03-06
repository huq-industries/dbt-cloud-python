# coding: utf-8

"""
    dbt Cloud API v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0a1
    Contact: support@getdbt.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import dbt_cloud_client
from api.runs_api import RunsApi  # noqa: E501
from dbt_cloud_client.rest import ApiException


class TestRunsApi(unittest.TestCase):
    """RunsApi unit test stubs"""

    def setUp(self):
        self.api = api.runs_api.RunsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_run_by_id(self):
        """Test case for cancel_run_by_id

        cancel specific run on account  # noqa: E501
        """
        pass

    def test_get_run_by_id(self):
        """Test case for get_run_by_id

        get specific run on account  # noqa: E501
        """
        pass

    def test_list_runs_for_account(self):
        """Test case for list_runs_for_account

        search or list runs for an account  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
