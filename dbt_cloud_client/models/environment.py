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


class Environment(object):
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
        'account_id': 'int',
        'connection_id': 'int',
        'deploy_key_id': 'int',
        'created_by_id': 'int',
        'repository_id': 'int',
        'name': 'str',
        'notification_email': 'int',
        'dbt_version': 'str',
        'use_custom_branch': 'bool',
        'custom_branch': 'str',
        'supports_docs': 'bool',
        'state': 'int'
    }

    attribute_map = {
        'id': 'id',
        'account_id': 'account_id',
        'connection_id': 'connection_id',
        'deploy_key_id': 'deploy_key_id',
        'created_by_id': 'created_by_id',
        'repository_id': 'repository_id',
        'name': 'name',
        'notification_email': 'notification_email',
        'dbt_version': 'dbt_version',
        'use_custom_branch': 'use_custom_branch',
        'custom_branch': 'custom_branch',
        'supports_docs': 'supports_docs',
        'state': 'state'
    }

    def __init__(self, id=None, account_id=None, connection_id=None, deploy_key_id=None, created_by_id=None, repository_id=None, name=None, notification_email=None, dbt_version=None, use_custom_branch=None, custom_branch=None, supports_docs=None, state=None):  # noqa: E501
        """Environment - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._account_id = None
        self._connection_id = None
        self._deploy_key_id = None
        self._created_by_id = None
        self._repository_id = None
        self._name = None
        self._notification_email = None
        self._dbt_version = None
        self._use_custom_branch = None
        self._custom_branch = None
        self._supports_docs = None
        self._state = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if account_id is not None:
            self.account_id = account_id
        if connection_id is not None:
            self.connection_id = connection_id
        if deploy_key_id is not None:
            self.deploy_key_id = deploy_key_id
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if repository_id is not None:
            self.repository_id = repository_id
        if name is not None:
            self.name = name
        if notification_email is not None:
            self.notification_email = notification_email
        if dbt_version is not None:
            self.dbt_version = dbt_version
        if use_custom_branch is not None:
            self.use_custom_branch = use_custom_branch
        if custom_branch is not None:
            self.custom_branch = custom_branch
        if supports_docs is not None:
            self.supports_docs = supports_docs
        if state is not None:
            self.state = state

    @property
    def id(self):
        """Gets the id of this Environment.  # noqa: E501


        :return: The id of this Environment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Environment.


        :param id: The id of this Environment.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def account_id(self):
        """Gets the account_id of this Environment.  # noqa: E501


        :return: The account_id of this Environment.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Environment.


        :param account_id: The account_id of this Environment.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def connection_id(self):
        """Gets the connection_id of this Environment.  # noqa: E501


        :return: The connection_id of this Environment.  # noqa: E501
        :rtype: int
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this Environment.


        :param connection_id: The connection_id of this Environment.  # noqa: E501
        :type: int
        """

        self._connection_id = connection_id

    @property
    def deploy_key_id(self):
        """Gets the deploy_key_id of this Environment.  # noqa: E501


        :return: The deploy_key_id of this Environment.  # noqa: E501
        :rtype: int
        """
        return self._deploy_key_id

    @deploy_key_id.setter
    def deploy_key_id(self, deploy_key_id):
        """Sets the deploy_key_id of this Environment.


        :param deploy_key_id: The deploy_key_id of this Environment.  # noqa: E501
        :type: int
        """

        self._deploy_key_id = deploy_key_id

    @property
    def created_by_id(self):
        """Gets the created_by_id of this Environment.  # noqa: E501


        :return: The created_by_id of this Environment.  # noqa: E501
        :rtype: int
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this Environment.


        :param created_by_id: The created_by_id of this Environment.  # noqa: E501
        :type: int
        """

        self._created_by_id = created_by_id

    @property
    def repository_id(self):
        """Gets the repository_id of this Environment.  # noqa: E501


        :return: The repository_id of this Environment.  # noqa: E501
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """Sets the repository_id of this Environment.


        :param repository_id: The repository_id of this Environment.  # noqa: E501
        :type: int
        """

        self._repository_id = repository_id

    @property
    def name(self):
        """Gets the name of this Environment.  # noqa: E501


        :return: The name of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Environment.


        :param name: The name of this Environment.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notification_email(self):
        """Gets the notification_email of this Environment.  # noqa: E501


        :return: The notification_email of this Environment.  # noqa: E501
        :rtype: int
        """
        return self._notification_email

    @notification_email.setter
    def notification_email(self, notification_email):
        """Sets the notification_email of this Environment.


        :param notification_email: The notification_email of this Environment.  # noqa: E501
        :type: int
        """

        self._notification_email = notification_email

    @property
    def dbt_version(self):
        """Gets the dbt_version of this Environment.  # noqa: E501


        :return: The dbt_version of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._dbt_version

    @dbt_version.setter
    def dbt_version(self, dbt_version):
        """Sets the dbt_version of this Environment.


        :param dbt_version: The dbt_version of this Environment.  # noqa: E501
        :type: str
        """

        self._dbt_version = dbt_version

    @property
    def use_custom_branch(self):
        """Gets the use_custom_branch of this Environment.  # noqa: E501


        :return: The use_custom_branch of this Environment.  # noqa: E501
        :rtype: bool
        """
        return self._use_custom_branch

    @use_custom_branch.setter
    def use_custom_branch(self, use_custom_branch):
        """Sets the use_custom_branch of this Environment.


        :param use_custom_branch: The use_custom_branch of this Environment.  # noqa: E501
        :type: bool
        """

        self._use_custom_branch = use_custom_branch

    @property
    def custom_branch(self):
        """Gets the custom_branch of this Environment.  # noqa: E501


        :return: The custom_branch of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._custom_branch

    @custom_branch.setter
    def custom_branch(self, custom_branch):
        """Sets the custom_branch of this Environment.


        :param custom_branch: The custom_branch of this Environment.  # noqa: E501
        :type: str
        """

        self._custom_branch = custom_branch

    @property
    def supports_docs(self):
        """Gets the supports_docs of this Environment.  # noqa: E501


        :return: The supports_docs of this Environment.  # noqa: E501
        :rtype: bool
        """
        return self._supports_docs

    @supports_docs.setter
    def supports_docs(self, supports_docs):
        """Sets the supports_docs of this Environment.


        :param supports_docs: The supports_docs of this Environment.  # noqa: E501
        :type: bool
        """

        self._supports_docs = supports_docs

    @property
    def state(self):
        """Gets the state of this Environment.  # noqa: E501


        :return: The state of this Environment.  # noqa: E501
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Environment.


        :param state: The state of this Environment.  # noqa: E501
        :type: int
        """

        self._state = state

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
        if issubclass(Environment, dict):
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
        if not isinstance(other, Environment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other