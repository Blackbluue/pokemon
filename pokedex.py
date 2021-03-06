from csv import DictReader
from operator import itemgetter

from chunks import timsort
from dex_entry import DexEntry


class Pokedex:
    """Interface for a Pokedex"""
    ###--TO DO--###
    # fix sorting on exp growth rate
    
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
    ABILITIES_FIRST = 29
    ABILITIES_SECOND = 30
    ABILITIES_HIDDEN = 31

    # Filtering keys
    # all sort keys also function as filter keys

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
        self._dex_dict, self._dex_view = self._parse_info(reader)

    def _parse_info(self, reader):
        """Parser to read a Pokedex File.
        
        :param reader: the DictReader that contains the info on the Pokedex.
        :type reader: class:'csv.DictReader'

        :return: A tuple of a dict of id keys and :class:'pokedex.DexEntry'
            object values containing all the Pokedex info from the file,
            and a list containing only the id numbers of each entry.
        :rtype: tuple of (dict, list)
        """
        # information on all pokemon in pokedex
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
        return item in self._dex_dict
   
    def _search_key(self, field):
        """Internal method for building a sort/filter key.
        :param field: Flag signifiying which field to use for data look up.

        :return: A single argument function that takes in one
            :class:'dex_entry.DexEntry' object and returns the data in the field
            specified by ``field``
        """
        if field == self.NAME:
            # only checking enlgish name, may update in future
            return lambda entry: entry["name"]["English"]
        elif field == self.TYPE:
            return lambda entry: entry["type"]
        elif field == self.NUMBER:
            return lambda entry: entry["number"]
        elif field == self.CLASSIFICATION:
            return lambda entry: entry["classification"]
        elif field == self.HEIGHT:
            return lambda entry: entry["height"]
        elif field == self.WEIGHT:
            return lambda entry: entry["weight"]
        elif field == self.CAPTURE_RATE:
            return lambda entry: entry["capture_rate"]
        elif field == self.EGG_CYCLES:
            return lambda entry: entry["base_egg_cycles"]
        elif field == self.ABILITIES:  # checks all 3 abilities
            return lambda entry: entry["abilities"]
        elif field == self.ABILITIES_FIRST:
            return lambda entry: entry["abilities"][0]
        elif field == self.ABILITIES_SECOND:
            return lambda entry: entry["abilities"][1]
        elif field == self.ABILITIES_HIDDEN:
            return lambda entry: entry["abilities"][2]
        elif field == self.EXP_YIELD:
            return lambda entry: entry["exp_yield"]
        elif field == self.EXP_GROWTH_RATE:
            return lambda entry: entry["experience_growth"]
        elif field == self.HAPPINESS:
            return lambda entry: entry["happiness"]
        elif field == self.STATS_TOTAL:
            return lambda entry: sum(entry["base_stats"].values())
        elif field == self.STATS_HP:
            return lambda entry: entry["base_stats"]["hp"]
        elif field == self.STATS_ATK:
            return lambda entry: entry["base_stats"]["attack"]
        elif field == self.STATS_DEF:
            return lambda entry: entry["base_stats"]["defense"]
        elif field == self.STATS_SP_ATK:
            return lambda entry: entry["base_stats"]["sp_attack"]
        elif field == self.STATS_SP_DEF:
            return lambda entry: entry["base_stats"]["sp_defense"]
        elif field == self.STATS_SPD:
            return lambda entry: entry["base_stats"]["speed"]
        elif field == self.EV_TOTAL:
            return lambda entry: sum(entry["evs"].values())
        elif field == self.EV_HP:
            return lambda entry: entry["evs"]["hp"]
        elif field == self.EV_ATK:
            return lambda entry: entry["evs"]["attack"]
        elif field == self.EV_DEF:
            return lambda entry: entry["evs"]["defense"]
        elif field == self.EV_SP_ATK:
            return lambda entry: entry["evs"]["sp_attack"]
        elif field == self.EV_SP_DEF:
            return lambda entry: entry["evs"]["sp_defense"]
        elif field == self.EV_SPD:
            return lambda entry: entry["evs"]["speed"]
        elif field == self.EGG_GROUPS:
            return lambda entry: entry["egg_groups"]
        elif field == self.EVOLUTION:
            return lambda entry: entry["evolve_to"]
        elif field == self.OWNED:
            return lambda entry: entry["owned"]
        else:  # default sort order
            return lambda entry: entry["number"]

    def sort(self, key, reverse=False):
        """Sort the entries of this Pokedex based on the given sort key.
        After sorting, the results can be retrieved with
        ``pokedex.Pokedex.results()``.

        :param key: Specifies on what criteria to sort the Pokedex.
            Identity values are supplied as constants in this class, and can
            be found in the documentation.
        :param reverse: A boolean value. If set to True, then the
            elements are sorted in reverse order.
        :type reverse: bool, optional
        """
        if key == EVOLUTION:
            def comp_key(elem1, elem2):
                if elem1["evolve_to"]:  # check if has evolution
                    return elem2["number"] in elem1["evolve_to"]
                else:
                    return elem1["number"] > elem2["number"]
            timsort(self.dex_view, comp_key=comp_key)
        else:
            sort_key = self._search_key(key)
            self.dex_view.sort(key=sort_key,  reverse=reverse)

    def filter(self, field, criteria):
        """Filter the Pokedex based on the given set of rules.

        :param field: The field to check for filtering.
        :param criteria: The data that i compared against the Pokedex
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
        """Return the current state of this Pokedex, with sorting and filtering.

        :return: The current state of this Pokedex. Changes to it do not reflect 
            to the internal sorting/filtering of the Pokdex, and vice-versa.
        :rtype: list
        """
        return [self._dex_dict[number] for number in self._dex_view]

    def reset(self):
        """Reset any sorting and filtering done on this Pokedex."""
        self._dex_view.clear()
        self._dex_view.extend(sorted(self._dex_dict.keys()))

class PokeEntry(DexEntry):
    """A single entry for a Pokemon in a Pokedex."""

    def __init__(self, info):
        """Constructor for a single Pokedex entry.
        
        :praram info: A dict containing all the information on this Pokdex entry.
        :type info: dict
        """
        super().__init__(info)
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
        # convert data to primative types

    @property
    def owned(self):
        """Whether the pokemon has been is unknown, seen, or owned."""
        return self._dex_info["owned"]

    @owned.setter
    def owned(self, status):
        if status.lower() not in ["unknown", "seen", "owned"]:
            raise ValueError("Improper value for 'owned' attribute.")
        self._dex_info["owned"] = status.lower()
