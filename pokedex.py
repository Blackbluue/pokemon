import copy
import csv


class Pokedex:
    """Interface for a Pokedex"""
    ###--TO DO--###
    # make Pokedex class act like a dict object
    

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



class DexEntry:
    """A single entry for a Pokemon in a Pokedex."""

    def __init__(self, info):
        """Constructor for a single Pokedex entry."""
        self._dex_info = info

    @property
    def dex_info(self):
        """The collected information on this pokedex entry."""
        return copy.deepcopy(self._dex_info)

    @property
    def owned(self):
        """Whether the pokemon has been seen, caught, or is unknown."""
        return self._dex_info["owned"]

    @owned.setter
    def owned(self, status):
        if status.lower() not in ["unknown", "seen", "owned"]:
            raise ValueError("Improper value for 'owned' attribute.")
        self._dex_info["owned"] = status.lower()
