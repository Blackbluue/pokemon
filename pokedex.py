from copy import copy
from csv import DictReader
from operator import itemgetter


class Pokedex:
    """Interface for a Pokedex"""
    ###--TO DO--###
    # make sorted views of Pokedex
    # height, weight, cap_rate, egg cycles,
    # exp yield, exp growth rate, happiness, total stats, total evs,
    # egg groups, evolution chain, owned
    # make filter methods
    
    # Sorting keys
    NAME = 0
    TYPE = 1
    NUMBER = 2
    CLASSIFICATION = 3
    HEIGHT = 4
    WEIGHT = 5
    CAPTURE_RATE = 6
    EGG_CYCLES = 7
    ABILITIES = 8
    EXP_YIELD = 9
    EXP_GROWTH_RATE = 10
    HAPPINESS = 11
    STATS_TOTAL = 12
    STATS_HP = 13
    STATS_ATK = 14
    STATS_DEF = 15
    STATS_SP_ATK = 16
    STATS_SP_DEF = 17
    STATS_SPD = 18
    EV_TOTAL = 19
    EV_HP = 20
    EV_ATK = 21
    EV_DEF = 22
    EV_SP_ATK = 23
    EV_SP_DEF = 24
    EV_SPD = 25
    EGG_GROUPS = 26
    EVOLUTION = 27
    OWNED = 28

    # Filtering keys
    # all sort keys also function as filter keys
    ABILITIES_SECOND = 29
    ABILITIES_HIDDEN = 30

    def __init__(self, dex_file):
        """Constructor for the Pokedex class.

        This constructor should be called with the name of the pokedex to create
        and a csv that contains the information defining the pokedex.
        """
        try:
            # assume dex_file is a string, the path to the file
            with open(dex_file, newline="") as fh:
                reader = DictReader(fh)
        except TypeError:
            # dex_file is a file-like object
            reader = DictReader(dex_file)
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
            dex_dict[row["number"]] = DexEntry(row)
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
   
    def sort_weight(self, reverse=False):
        """Return an iterator containing DexEntry ids from this Pokdex,
        sorted by the weight of each pokemon.

        :param reverse: A boolean value. If set to True, then the
            elements are sorted reverse order.
        :type reverse: bool, optional
        
        :return: An iterator of this DexEntry ids.
        :rtype: iter
        """
        entries = sorted(self._dex_dict.values(), key=itemgetter("weight"), reverse=reverse)
        return iter([entry["number"] for entry in entries])

    def sort_capture_rate(self, reverse=False):
        """Return an iterator containing DexEntry ids from this Pokdex,
        sorted by the capture_rate of each pokemon.

        :param reverse: A boolean value. If set to True, then the
            elements are sorted reverse order.
        :type reverse: bool, optional
        
        :return: An iterator of this DexEntry ids.
        :rtype: iter
        """
        entries = sorted(self._dex_dict.values(), key=itemgetter("capture_rate"), reverse=reverse)
        return iter([entry["number"] for entry in entries])

    def sorted(self, key, reverse=False):
        """Return an iterator containing id number/DexEntry pairs for entries
        in this Pokedex.
        :param key: Specifies on what criteria to sort the Pokedex.
            Identity values are supplied as constants in this class, and can
            be found in the documentation.
        :param reverse: A boolean value. If set to True, then the
            elements are sorted in reverse order.
        :type reverse: bool, optional

        :return: An iterator of this Pokdex's items.
        :rtype: iter
        """
        if key == self.NAME:
            return self._sort_simple(lambda entry: entry["name"]["English"], reverse)
        elif key == self.TYPE:
            return self._sort_simple(itemgetter("type"), reverse)
        elif key == self.NUMBER:  # default sort order
            return self._sort_simple(itemgetter("number"), reverse)
        elif key == self.CLASSIFICATION:
            return self._sort_simple(itemgetter("classification"), reverse)
        elif key == self.HEIGHT:
            return self._sort_simple(itemgetter("height"), reverse)
        elif key == self.WEIGHT:
            return self._sort_simple(itemgetter("weight"), reverse)
        elif key == self.CAPTURE_RATE:
            return self._sort_simple(itemgetter("capture_rate"), reverse)
        elif key == self.EGG_CYCLES:
            return self._sort_simple(itemgetter("base_egg_cycles"), reverse)
        elif key == self.ABILITIES:
            return self._sort_simple(itemgetter("abilities"), reverse)
        elif key == self.EXP_YIELD:
            return self._sort_simple(itemgetter("exp_yield"), reverse)
        elif key == self.EXP_GROWTH_RATE:
            return self._sort_simple(itemgetter("experience_growth"), reverse)
        elif key == self.HAPPINESS:
            return self._sort_simple(itemgetter("happiness"), reverse)
        elif key == self.STATS_TOTAL:
            sort_key = lambda entry: sum(entry["base_stats"].values())
            return self._sort_simple(sort_key, reverse)
        elif key == self.STATS_HP:
            return self._sort_simple(itemgetter("stats_hp"), reverse)
        elif key == self.STATS_ATK:
            return self._sort_simple(itemgetter("stats_atk"), reverse)
        elif key == self.STATS_DEF:
            return self._sort_simple(itemgetter("stats_def"), reverse)
        elif key == self.STATS_SP_ATK:
            return self._sort_simple(itemgetter("stats_sp_atk"), reverse)
        elif key == self.STATS_SP_DEF:
            return self._sort_simple(itemgetter("stats_sp_def"), reverse)
        elif key == self.STATS_SPD:
            return self._sort_simple(itemgetter("stats_spd"), reverse)
        elif key == self.EV_TOTAL:
            sort_key = lambda entry: sum(entry["evs"].values())
            return self._sort_simple(sort_key, reverse)
        elif key == self.EV_HP:
            return self._sort_simple(itemgetter("ev_hp"), reverse)
        elif key == self.EV_ATK:
            return self._sort_simple(itemgetter("ev_atk"), reverse)
        elif key == self.EV_DEF:
            return self._sort_simple(itemgetter("ev_def"), reverse)
        elif key == self.EV_SP_ATK:
            return self._sort_simple(itemgetter("ev_sp_atk"), reverse)
        elif key == self.EV_SP_DEF:
            return self._sort_simple(itemgetter("ev_sp_def"), reverse)
        elif key == self.EV_SPD:
            return self._sort_simple(itemgetter("ev_spd"), reverse)

    def _sort_simple(key, reverse=False):
        """Internal method for sorting Pokedex on text based fields. Supply
        a function key to specify which field to sort on.
        
        :param key: Single argument function that when supplied a
            :class:'pokedex.DexEntry' will return a value used for sorting.
        :param reverse: A boolean value. If set to True, then the
            elements are sorted in reverse order.
        :type reverse: bool, optional
        """
        entries = sorted(self._dex_dict.values(), key=key,  reverse=reverse)
        return iter([(value["number"], value) for value in entries])

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

    @property
    def owned(self):
        """Whether the pokemon has been is unknown, seen, or owned."""
        return self._dex_info["owned"]

    @owned.setter
    def owned(self, status):
        if status.lower() not in ["unknown", "seen", "owned"]:
            raise ValueError("Improper value for 'owned' attribute.")
        self._dex_info["owned"] = status.lower()

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
