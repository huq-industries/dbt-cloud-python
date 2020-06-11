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


class Body4(object):
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
        'remote_url': 'str',
        'github_installation_id': 'int'
    }

    attribute_map = {
        'remote_url': 'remote_url',
        'github_installation_id': 'github_installation_id'
    }

    def __init__(self, remote_url=None, github_installation_id=None):  # noqa: E501
        """Body4 - a model defined in Swagger"""  # noqa: E501
        self._remote_url = None
        self._github_installation_id = None
        self.discriminator = None
        if remote_url is not None:
            self.remote_url = remote_url
        if github_installation_id is not None:
            self.github_installation_id = github_installation_id

    @property
    def remote_url(self):
        """Gets the remote_url of this Body4.  # noqa: E501

        The git URL of the repository.  # noqa: E501

        :return: The remote_url of this Body4.  # noqa: E501
        :rtype: str
        """
        return self._remote_url

    @remote_url.setter
    def remote_url(self, remote_url):
        """Sets the remote_url of this Body4.

        The git URL of the repository.  # noqa: E501

        :param remote_url: The remote_url of this Body4.  # noqa: E501
        :type: str
        """

        self._remote_url = remote_url

    @property
    def github_installation_id(self):
        """Gets the github_installation_id of this Body4.  # noqa: E501

        If using a github integration, provide the id of the installation. If not, send `null`.  # noqa: E501

        :return: The github_installation_id of this Body4.  # noqa: E501
        :rtype: int
        """
        return self._github_installation_id

    @github_installation_id.setter
    def github_installation_id(self, github_installation_id):
        """Sets the github_installation_id of this Body4.

        If using a github integration, provide the id of the installation. If not, send `null`.  # noqa: E501

        :param github_installation_id: The github_installation_id of this Body4.  # noqa: E501
        :type: int
        """

        self._github_installation_id = github_installation_id

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
        if issubclass(Body4, dict):
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
        if not isinstance(other, Body4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
