# coding: utf-8

"""
    dbt Cloud API v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0a1
    Contact: support@getdbt.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Trigger(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'cause': 'str',
        'job_definition_id': 'int',
        'git_branch': 'str',
        'git_sha': 'str',
        'github_pull_request_id': 'int',
        'schema_override': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'cause': 'cause',
        'job_definition_id': 'job_definition_id',
        'git_branch': 'git_branch',
        'git_sha': 'git_sha',
        'github_pull_request_id': 'github_pull_request_id',
        'schema_override': 'schema_override',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, cause=None, job_definition_id=None, git_branch=None, git_sha=None, github_pull_request_id=None, schema_override=None, created_at=None):  # noqa: E501
        """Trigger - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._cause = None
        self._job_definition_id = None
        self._git_branch = None
        self._git_sha = None
        self._github_pull_request_id = None
        self._schema_override = None
        self._created_at = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if cause is not None:
            self.cause = cause
        if job_definition_id is not None:
            self.job_definition_id = job_definition_id
        if git_branch is not None:
            self.git_branch = git_branch
        if git_sha is not None:
            self.git_sha = git_sha
        if github_pull_request_id is not None:
            self.github_pull_request_id = github_pull_request_id
        if schema_override is not None:
            self.schema_override = schema_override
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this Trigger.  # noqa: E501


        :return: The id of this Trigger.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Trigger.


        :param id: The id of this Trigger.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def cause(self):
        """Gets the cause of this Trigger.  # noqa: E501


        :return: The cause of this Trigger.  # noqa: E501
        :rtype: str
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """Sets the cause of this Trigger.


        :param cause: The cause of this Trigger.  # noqa: E501
        :type: str
        """

        self._cause = cause

    @property
    def job_definition_id(self):
        """Gets the job_definition_id of this Trigger.  # noqa: E501


        :return: The job_definition_id of this Trigger.  # noqa: E501
        :rtype: int
        """
        return self._job_definition_id

    @job_definition_id.setter
    def job_definition_id(self, job_definition_id):
        """Sets the job_definition_id of this Trigger.


        :param job_definition_id: The job_definition_id of this Trigger.  # noqa: E501
        :type: int
        """

        self._job_definition_id = job_definition_id

    @property
    def git_branch(self):
        """Gets the git_branch of this Trigger.  # noqa: E501


        :return: The git_branch of this Trigger.  # noqa: E501
        :rtype: str
        """
        return self._git_branch

    @git_branch.setter
    def git_branch(self, git_branch):
        """Sets the git_branch of this Trigger.


        :param git_branch: The git_branch of this Trigger.  # noqa: E501
        :type: str
        """

        self._git_branch = git_branch

    @property
    def git_sha(self):
        """Gets the git_sha of this Trigger.  # noqa: E501


        :return: The git_sha of this Trigger.  # noqa: E501
        :rtype: str
        """
        return self._git_sha

    @git_sha.setter
    def git_sha(self, git_sha):
        """Sets the git_sha of this Trigger.


        :param git_sha: The git_sha of this Trigger.  # noqa: E501
        :type: str
        """

        self._git_sha = git_sha

    @property
    def github_pull_request_id(self):
        """Gets the github_pull_request_id of this Trigger.  # noqa: E501


        :return: The github_pull_request_id of this Trigger.  # noqa: E501
        :rtype: int
        """
        return self._github_pull_request_id

    @github_pull_request_id.setter
    def github_pull_request_id(self, github_pull_request_id):
        """Sets the github_pull_request_id of this Trigger.


        :param github_pull_request_id: The github_pull_request_id of this Trigger.  # noqa: E501
        :type: int
        """

        self._github_pull_request_id = github_pull_request_id

    @property
    def schema_override(self):
        """Gets the schema_override of this Trigger.  # noqa: E501


        :return: The schema_override of this Trigger.  # noqa: E501
        :rtype: str
        """
        return self._schema_override

    @schema_override.setter
    def schema_override(self, schema_override):
        """Sets the schema_override of this Trigger.


        :param schema_override: The schema_override of this Trigger.  # noqa: E501
        :type: str
        """

        self._schema_override = schema_override

    @property
    def created_at(self):
        """Gets the created_at of this Trigger.  # noqa: E501


        :return: The created_at of this Trigger.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Trigger.


        :param created_at: The created_at of this Trigger.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Trigger, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Trigger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other