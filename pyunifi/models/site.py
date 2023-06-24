#{
#    'anonymous_id': 'e3fbcb3f-8536-4c32-acff-585732dccaa4',
#    'name': '25zs4qy4',
#    '_id': '5d41b5c6a685b4035d12f2e7',
#    'desc': 'ABA (DGT)',
#    'role': 'admin',
#    'device_count': 4
#}
# This is modeled off Swagger code generator. 

import pprint
import re  # noqa: F401
import six

class Site(object):
    unifi_types = {
        'anonymous_id': 'str',
        'name': 'str',
        'id': 'str',
        'desc': 'str',
        'role': 'str',
        'device_count': 'str'
    }
    
    attribute_map = {
        'anonymous_id': 'anonymous_id',
        'name': 'name',
        'id': '_id',
        'desc': 'desc',
        'role': 'role',
        'device_count': 'device_count'
    }

    def __init__(self, anonymous_id=None, name=None, id=None, desc=None, role=None, device_count=None):
        self._anonymous_id = None
        self._name = None
        self._id = None
        self._desc = None
        self._role = None
        self._device_count = None
        
        if anonymous_id is not None:
            self.anonymous_id = anonymous_id
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if desc is not None:
            self.desc = desc
        if role is not None:
            self.role = role
        if device_count is not None:
            self.device_count = device_count
            
    @property
    def anonymous_id(self):
        return self._anonymous_id

    @anonymous_id.setter
    def anonymous_id(self, anonymous_id):
        self._anonymous_id = anonymous_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id
        
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, desc):
        self._desc = desc

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role

    @property
    def device_count(self):
        return self._device_count

    @device_count.setter
    def device_count(self, device_count):
        self._device_count = device_count
# {
#    'anonymous_id': 'e3fbcb3f-8536-4c32-acff-585732dccaa4',
#    'name': '25zs4qy4',
#    '_id': '5d41b5c6a685b4035d12f2e7',
#    'desc': 'ABA (DGT)',
#    'role': 'admin',
#    'device_count': 4
# }
    @classmethod
    def from_api_return(cls, data):
        return cls(
            anonymous_id=data['anonymous_id'],
            name=data['name'],
            id=data['_id'],
            desc=data['desc'],
            role=data['role'],
            device_count=data['device_count']
        )


    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.unifi_types):
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
        if issubclass(Site, dict):
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
        if not isinstance(other, Site):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
