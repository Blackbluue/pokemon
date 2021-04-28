from csv import DictReader

from dex_entry import DexEntry
class Itemdex:
    """Interface for an encyclopedia of items"""
    ###--TO DO--###

    # Sorting keys
    NAME = 0
    TYPE = 1
    ID = 2
    BUY = 3
    SELL = 4
    EFFECT = 5
    FLAVOR_TEXT = 6

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
            dex_dict[row["id"]] = DexEntry(row)
            dex_view.append(row["id"])
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
        return item in self._dex_dict

    def _search_key(self, field):
        """Internal method for building a sort/filter key.
        :param field: Flag signifiying which field to use for data look up.

        :return: A single argument function that takes in one
            :class:'dex_entry.DexEntry' object and returns the data in the field
            specified by ``field``
        """
        if field == self.NAME:
            return lambda entry: entry["name"]
        elif field == self.TYPE:
            return lambda entry: entry["type"]
        elif field == self.ID:
            return lambda entry: entry["id"]
        elif field == self.BUY:
            return lambda entry: entry["purchase_price"]
        elif field == self.SELL:
            return lambda entry: entry["sale_price"]
        elif field == self.EFFECT:
            return lambda entry: entry["effect"]
        elif field == self.FLAVOR_TEXT:
            return lambda entry: entry["flavor_text"]
        else:  # specific/unknown field name
            try:  # check name
                return lambda entry: entry[field.lower()]
            except:  # default sort order
                return lambda entry: entry["name"]

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
        self._dex_view.sort(key=sort_key,  reverse=reverse)

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
        return [self._dex_dict[item_id] for item_id in self._dex_view]

    def reset(self):
        """Reset any sorting and filtering done on this Itemdex."""
        self._dex_view.clear()
        self._dex_view.extend(sorted(self._dex_dict.keys()))

class ItemEntry(DexEntry):
    """A single entry for an item in a Itemdex."""

    def __init__(self, info):
        """Constructor for a single Itemdex entry.
        
        :param info: A dict containing all the information on this Itemdex entry.
        :type info: dict
        """
        super().__init__(info)
        # convert data to internal list
        # convert data to internal dicts
        # convert data to primative types
