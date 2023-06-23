import pprint
import re  # noqa: F401
import six

from pyunifi.models.site import Site


class Siteslist(object):
    unifi_types = {
        'results': 'list[Site]',
        'total_count': 'int'
    }

    attribute_map = {
        'results': 'results',
        'total_count': 'totalCount'
    }

    def __init__(self, results=None, total_count=None):
        self._results = None
        self._total_count = None
        self.discriminator = None

        if results is not None:
            self.results = results
        if total_count is not None:
            self.total_count = total_count

    @property
    def results(self):
        return self._results

    @results.setter
    def results(self, results):
        self._results = results

    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        self._total_count = total_count

    def to_dict(self):
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
        if issubclass(Systemslist, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Systemslist):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
