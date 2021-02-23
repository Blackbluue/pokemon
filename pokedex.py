import copy
import csv


class Pokedex:
    """Interface for a Pokedex"""

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
        self._dex_list = self._parse_info(reader)
        dex_entries = dict()

    def _parse_info(self, reader):
        """Parser to read a Pokedex File.
        
        :param reader: the DictReader that contains the info on the Pokedex.
        :type reader: class:'csv.DictReader'

        :return: A list of :class:'pokedex.DexEntry' objects containing all
            the Pokedex info from the file.
        :rtype: list
        """
        pass


class DexEntry:
    """A single entry for a Pokemon in a Pokedex."""

    def __init__(self, info):
        """Constructor for a single Pokedex entry."""
        self._dex_info = info

    @property
    def dex_info(self):
        """The collected information on this pokedex entry."""
        return copy.deepcopy(self._dex_info)
