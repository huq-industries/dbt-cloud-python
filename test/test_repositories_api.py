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
from api.repositories_api import RepositoriesApi  # noqa: E501
from dbt_cloud_client.rest import ApiException


class TestRepositoriesApi(unittest.TestCase):
    """RepositoriesApi unit test stubs"""

    def setUp(self):
        self.api = api.repositories_api.RepositoriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_repository(self):
        """Test case for create_repository

        create repository on account  # noqa: E501
        """
        pass

    def test_get_repository_by_id(self):
        """Test case for get_repository_by_id

        get specific repository on account  # noqa: E501
        """
        pass

    def test_list_repositories_for_account(self):
        """Test case for list_repositories_for_account

        search or list repositories on an account  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
