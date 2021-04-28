from copy import copy

class DexEntry:
    """A single entry for an item in a Dex-like collection."""

    def __init__(self, info):
        """Constructor for a single Itemdex entry.
        
        :param info: A dict containing all the information on this Itemdex entry.
        :type info: dict
        """
        self._dex_info = info
        # convert data to internal list in subclasses
        # convert data to internal dicts in subclasses
        
    @staticmethod
    def _str_to_dict(string, key_type=None, value_type=None):
        """Convert a string to a dictionary.

        :param string: The string to convert.
        :type string: str
        :param key_type: a single argument function used to extract the
            desired type for the keys of the dict.
        :type key_type: function, optional
        :param value_type: a single argument function used to extract the
            desired type for the values of the dict.
        :type value_type: function, optional

        :return: The converted dict object.
        :rtype: dict
        """
        string = string.strip("[]").split(",")
        temp_list = [item.split(":") for item in string]
        results = dict()
        for key, value in temp_list:
            if key_type:
                key = key_type(key)
            if value_type:
                value = value_type(value)
            results[key] = value
        return results

    @staticmethod
    def _str_to_list(string, value_type=None):
        """Convert a string to a list.
        
        :param string: The string to convert.
        :type string: str
        :param value_type: a single argument function used to extract the
            desired type for the values of the list.
        :type value_type: function, optional

        :return: The converted list object.
        :rtype: list
        """
        if value_type:
            return [value_type(item) for item in string.strip("[]").split(",")]
        else:
            return string.strip("[]").split(",")

    def __getitem__(self, key):
        """Return a single property from this DexEntry.
        
        :param key: The name of the property.
        :type key: str

        :return: The requested property value. Type is dependent on the property.
        """
        return copy(self._dex_info[key])