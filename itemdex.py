from copy import copy
from csv import DictReader

class Itemdex:
    """Interface for an encyclopedia of items"""
    ###--TO DO--###
    # define _search_key()

    def __init__(self, dex_file):
        """Constructor for the Itemdex class.

        This constructor should be called with the name of the itemdex to create
        and a csv that contains the information defining the itemdex.

        :param dex_file: the itemdex to create. This can be either
            a file-like object of the itemdex or path-like string
            to the file.
        """
        try:
            # assume dex_file is a string, the path to the file
            with open(dex_file, newline="") as fh:
                reader = DictReader(fh)
        except TypeError:
            # dex_file is a file-like object
            reader = DictReader(dex_file)
        self._dex_dict, self._dex_view = self._parse_info(reader)

    def _parse_info(self, reader):
        """Parser to read an Itemdex File.
        
        :param reader: the DictReader that contains the info on the Itemdex.
        :type reader: class:'csv.DictReader'

        :return: A tuple of a dict of id keys and :class:'itemdex.DexEntry'
            object values containing all the Itemdex info from the file,
            and a list containing only the id numbers of each entry.
        :rtype: tuple of (dict, list)
        """
        # information on all items in itemdex
        dex_dict = dict()
        # list view for filtering and sorting
        dex_view = list()
        for row in reader:
            dex_dict[row["number"]] = DexEntry(row)
            dex_view.append(row["number"])
        return dex_dict, dex_view

        def __len__(self):
        """The size of the Pokedex."""
        return len(self._dex_dict)
    
    def __getitem__(self, key):
        """Retrieve the Itemdex entry with the specified key.

        :param key: the id of the requested Itemdex file.
        :type key: str

        :return: The requested Itemdex entry.
        :rtype: :class:'itemdex.DexEntry'
        """
        return self._dex_dict[key]

    def __iter__(self):
        """The iterator for the Itemdex"""
        return iter(self._dex_dict)

    def __contains__(self, item):
        """True if an entry with the specified id exists; otherwise false."""
        return True if item in self._dex_dict else False

    def _search_key(self, field):
        """Internal method for building a sort/filter key.
        :param field: Flag signifiying which field to use for data look up.

        :return: A single argument function that takes in one
            :class:'itemdex.DexEntry' object and returns the data in the field
            specified by ``field``
        """
        pass

    def sort(self, key, reverse=False):
        """Sort the entries of this Itemdex based on the given sort key.
        After sorting, the results can be retrieved with
        ``itemdex.Itemdex.results()``.

        :param key: Specifies on what criteria to sort the Itemdex.
            Identity values are supplied as constants in this class, and can
            be found in the documentation.
        :param reverse: A boolean value. If set to True, then the
            elements are sorted in reverse order.
        :type reverse: bool, optional
        """
        sort_key = self._search_key(key)
        self.dex_view.sort(key=sort_key,  reverse=reverse)

    def filter(self, field, criteria):
        """Filter the Itemdex based on the given set of rules.

        :param field: The field to check for filtering.
        :param criteria: The data that is compared against the Itemdex
            for filtering.
        """
        extractor = self._search_key(field)
        for index, entry_number in enumerate(self._dex_view):
                entry = self._dex_dict[entry_number]
                try:
                    # check if field is iterable
                    if criteria not in extractor(entry):
                        del self._dex_view[index]
                except TypeError:
                    # field is not iterable, assume primative type
                    if criteria != extractor(entry):
                        del self._dex_view[index]

    def results(self):
        """Return the current state of this Itemdex, with sorting and filtering.

        :return: The current state of this Itemdex. Changes to it do not reflect 
            to the internal sorting/filtering of the Itemdex, and vice-versa.
        :rtype: list
        """
        return [self._dex_dict[number] for number in self._dex_view]

    def reset(self):
        """Reset any sorting and filtering done on this Itemdex."""
        self._dex_view.clear()
        self._dex_view.extend(sorted(self._dex_dict.keys()))

class DexEntry:
    """A single entry for an item in a Itemdex."""

    def __init__(self, info):
        """Constructor for a single Itemdex entry.
        
        :praram info: A dict containing all the information on this Itemdex entry.
        :type info: dict
        """
        self._dex_info = info
        # convert data to internal list
        # convert data to internal dicts
        
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
