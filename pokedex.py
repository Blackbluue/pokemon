import copy
import csv


class Pokedex:
    """Interface for a Pokedex"""
    ###--TO DO--###
    # make sorted views of Pokedex
    # name, type, id, classification, height, weight, cap_rate, egg cycles,
    # exp yield, exp growth rate, happiness, total stats, total evs,
    # egg groups, evolution chain, owned
    # make filter methods
    

    def __init__(self, dex_file):
        """Constructor for the Pokedex class.

        This constructor should be called with the name of the pokedex to create
        and a csv that contains the information defining the pokedex.
        """
        try:
            # assume dex_file is a string, the path to the file
            with open(dex_file, newline="") as fh:
                reader = csv.DictReader(fh)
        except TypeError:
            # dex_file is a file-like object
            reader = csv.DictReader(dex_file)
        self._dex_dict = self._parse_info(reader)

    def _parse_info(self, reader):
        """Parser to read a Pokedex File.
        
        :param reader: the DictReader that contains the info on the Pokedex.
        :type reader: class:'csv.DictReader'

        :return: A dict of id keys and :class:'pokedex.DexEntry' object values
            containing all the Pokedex info from the file.
        :rtype: dict
        """
        dex_dict = dict()
        for row in reader:
            dex_dict[row["number"]] = (DexEntry(row))
        return dex_dict

    def __len__(self):
        """The size of the Pokedex."""
        return len(self._dex_dict)
    
    def __getitem__(self, key):
        """Retrieve the Pokedex entry with the specified key.
        
        Although key must be a string, they should consist of a
        single integer value, possibly with an optional variant
        tag in the form of int:var_tag

        :param key: the id of the requested Pokedex file.
        :type key: str

        :return: The requested Pokedex entry.
        :rtype: :class:'pokedex.DexEntry'
        """
        return self._dex_dict[key]

    def __iter__(self):
        """The iterator for the Pokdex"""
        return iter(self._dex_dict)

    def __contains__(self, item):
        """True if an entry with the specified id exists; otherwise false."""
        return True if item in self._dex_dict else False

    
class DexEntry:
    """A single entry for a Pokemon in a Pokedex."""

    def __init__(self, info):
        """Constructor for a single Pokedex entry.
        
        :praram info: A dict containing all the information on this Pokdex entry.
        :type info: dict
        """
        self._dex_info = info
        # convert data to internal list
        self._dex_info["type"] = self._str_to_list(self._dex_info["type"])
        self._dex_info["abilities"] = self._str_to_list(self._dex_info["abilities"])
        self._dex_info["egg_groups"] = self._str_to_list(self._dex_info["egg_groups"])
        self._dex_info["evolve_to"] = self._str_to_list(self._dex_info["evolve_to"])
        self._dex_info["move_set_machine"] = self._str_to_list(self._dex_info["move_set_machine"])
        self._dex_info["move_set_egg"] = self._str_to_list(self._dex_info["move_set_egg"])
        self._dex_info["move_set_tutor"] = self._str_to_list(self._dex_info["move_set_tutor"])
        # convert data to internal dicts
        self._dex_info["name"] = self._str_to_dict(self._dex_info["name"])
        self._dex_info["base_stats"] = self._str_to_dict(self._dex_info["base_stats"], value_type=int)
        self._dex_info["evs"] = self._str_to_dict(self._dex_info["evs"], value_type=int)
        self._dex_info["flavor_text"] = self._str_to_dict(self._dex_info["flavor_text"])
        self._dex_info["move_set_level"] = self._str_to_dict(self._dex_info["move_set_level"], key_type=int)

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

    @property
    def dex_info(self):
        """The collected information on this pokedex entry."""
        return copy.deepcopy(self._dex_info)

    @property
    def owned(self):
        """Whether the pokemon has been is unknown, seen, or owned."""
        return self._dex_info["owned"]

    @owned.setter
    def owned(self, status):
        if status.lower() not in ["unknown", "seen", "owned"]:
            raise ValueError("Improper value for 'owned' attribute.")
        self._dex_info["owned"] = status.lower()
