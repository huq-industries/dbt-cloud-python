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
from api.jobs_api import JobsApi  # noqa: E501
from dbt_cloud_client.rest import ApiException


class TestJobsApi(unittest.TestCase):
    """JobsApi unit test stubs"""

    def setUp(self):
        self.api = api.jobs_api.JobsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_job(self):
        """Test case for create_job

        create job on account  # noqa: E501
        """
        pass

    def test_delete_job_by_id(self):
        """Test case for delete_job_by_id

        delete job on account  # noqa: E501
        """
        pass

    def test_get_job_by_id(self):
        """Test case for get_job_by_id

        get specific job on account  # noqa: E501
        """
        pass

    def test_list_jobs_for_account(self):
        """Test case for list_jobs_for_account

        search or list jobs on an account  # noqa: E501
        """
        pass

    def test_trigger_run(self):
        """Test case for trigger_run

        trigger run for job  # noqa: E501
        """
        pass

    def test_update_job_by_id(self):
        """Test case for update_job_by_id

        update job on account  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
