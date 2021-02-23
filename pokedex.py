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
        self._parse_info(reader)
        dex_entries = dict()


class DexEntry:
    """A single entry for a Pokemon in a Pokedex."""

    def __init__(self, info):
        """Constructor for a single Pokedex entry."""
        self._name = info["name"]

    @property
    def name(self):
        """The name of this species of pokemon."""
        return self._name
