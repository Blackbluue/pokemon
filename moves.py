"""Contains classes relating to a battle moves that pokemon can use."""
import csv

class Move:
    """Interface for a pokemon's battle move."""
    def __init__(self, name, move_file):
        """Constructor for the Move class.

        This constructor should be called with the name of the move to create
        and a csv that contains the information defining the move.
        Required kwargs:
            name                   -- the name of the move
            type                   -- the type of the move
            category               -- whether the move is physical or special
            pp                     -- the maximum power point value for the move
                                      damage, or a status move
            base_power             -- the base power of the move
            accuracy               -- the accuracy of the move
            flavor_text            -- flavor text for the move, a brief
                                      description of what it does
            effect                 -- the additional effect that the move may
                                      cause
            effect_rate            -- the chance the additoinal effect will
                                      occur
            cit_ratio              -- the base chance the damaging move will
                                      cause critical damage
            priority               -- the speed priority of the move
            target                 -- the target of the move in battle
            contact                -- whether the pokemon using the move makes
                                      physical contact with its target
            sound                  -- whether the move is sound based
            punch                  -- whether the move is a punching move
            biting                 -- whether the move is a biting move
            snatchable             -- whether the move can be snatched
            gravity                -- whether the move is affected by gravity
            defrost                -- whether the move defrosts the pokemon if
                                      it is frozen
            reflectable            -- whether the move can be reflected by
                                      magic coat/magic bounce
            blockable              -- whether the move can be blocked by
                                      protect/detect
            copyable               -- whether the move can be copied by mirror
                                      move
            unique_effect          -- additional notes on irregular effects. Is
                                      ignored by the base Move class
        """
        try:
            # assume move_file is a string, the path to the file
            with open(move_file, newline="") as fh:
                reader = csv.DictReader(fh)
                filtered = (info for info in reader if info["name"] == name)
        except TypeError:
            # move_file is a file-like object
            reader = csv.DictReader(move_file)
            filtered = (info for info in reader if info["name"] == name)
        move_info = next(filtered)
        self._parse_info(move_info)

        self._name = move_info["name"]
        self._type = move_info["type"]
        self._category = move_info["category"]
        self._pp_max = move_info["pp"]
        self._pp_cur = self._pp_max
        self._base_power = move_info["base_power"]
        self._accuracy = move_info["accuracy"]
        self._flavor_text = move_info["flavor_text"]
        ###--TO DO--###
        # add code to properly set an effect to the move
        self._set_effect(move_info["effect"], move_info["effect_rate"])
        self._cit_ratio = move_info["cit_ratio"]
        self._priority = move_info["priority"]
        self._target = move_info["target"]
        self._contact = move_info["contact"]
        self._sound = move_info["sound"]
        self._punch = move_info["punch"]
        self._biting = move_info["biting"]
        self._snatchable = move_info["snatchable"]
        self._gravity = move_info["gravity"]
        self._defrost = move_info["defrost"]
        self._reflectable = move_info["reflectable"]
        self._blockable = move_info["blockable"]

    ########## Class Constants ##########

    ########## Properties ##########
    @property
    def name(self):
        """The name of the move."""
        return self._name

    @property
    def type(self):
        """The type of the move."""
        return self._type

    @property
    def category(self):
        """The category of the move.

        Valid categories include: physical, special, other.
        """
        return self._category

    @property
    def pp_max(self):
        """The maximum value for this move's power points."""
        return self._pp_max

    @property
    def pp_cur(self):
        """The current value for this move's power points."""
        return self._pp_cur

    @pp_cur.setter
    def pp_cur(self, value):
        if value > self._pp_max or value < 0:
            raise ValueError(f"Improper value for current pp: {value}")
        self._pp_cur = value

    @property
    def base_power(self):
        """The base power for this move."""
        return self._base_power

    @property
    def accuracy(self):
        """The accuracy for this move."""
        return self._accuracy

    @property
    def flavor_text(self):
        """The simple description for this move."""
        return self._flavor_text

    @property
    def effect(self):
        """The effect that may be applied by this move."""
        ###--TO DO--###
        # add code to properly set an effect to the move
        # should return a tuple of 2 items; the name of the effect and a
        # function used to apply the effect to a target
        return self._effect

    @property
    def effect_rate(self):
        """The chance that the additional effect will occur, if present.

        If this move has no additional effect, this property will be None
        """
        return self._effect_rate

    @property
    def cit_ratio(self):
        """The chance this damaging move will deal critical damage.

        Moves that do not deal damage will have a critical ratio of 0.
        """
        return self._cit_ratio

    @property
    def priority(self):
        """The speed priority for this move.

        Moves with a higher priority will always go before one with lower
        priorirty. If both moves have the same priority, the pokemon with the
        higher speed stat will act first.
        """
        return self._priority

    @property
    def target(self):
        """The target of this move.

        Suitable values for a target are:
        self, single_adjacent_foe, single_adjacent_any, single_adjacent_ally,
        single_any, user_or_adjacent_ally, all_adjacent_foe, all_adjacent_any,
        all_foes, field, team, special.
        """
        return self._target

    @property
    def contact(self):
        """Whether the move makes physical contact with its target."""
        return self._contact

    @property
    def sound(self):
        """Whether the move utilizes sound."""
        return self._sound

    @property
    def punch(self):
        """Whether the move is a punch."""
        return self._punch

    @property
    def biting(self):
        """Whether the move is a biting move."""
        return self._biting

    @property
    def snatchable(self):
        """Whether the move is snatchable."""
        return self._snatchable

    @property
    def gravity(self):
        """Whether the move is affected by gravity."""
        return self._gravity

    @property
    def defrost(self):
        """Whether the move defrosts the pokemon if it is frozen."""
        return self._defrost

    @property
    def reflectable(self):
        """Whether the move can be reflected by magic coat or magic bounce."""
        return self._reflectable

    @property
    def blockable(self):
        """Whether the move can be blocked by protect or detect."""
        return self._blockable

    @property
    def copyable(self):
        """Whether the move can be copied by mirror move."""
        return self._copyable


    ########## Class/Static Methods ##########
    @staticmethod
    def _get_move_info(name, reader):
        """Pull the required information from the csv for the specified move."""
        ###--TO DO--###
        # add code to read the csv and get the necessary info
        try:
            # assume move_file is a string, the path to the file
            with open(move_file, newline="") as fh:
                reader = csv.DictReader(fh)
                filtered = (info for info in reader if info["name"] == name)
                self._move_info = next(filtered)
        except TypeError:
            # move_file is a file-like object
            reader = csv.DictReader(move_file)
            filtered = (info for info in reader if info["name"] == name)
            self._move_info = next(filtered)

    ########## Instance Methods ##########
    def _parse_info(move_info):
        """Parse the supplied dictionary for info to initialize this move."""
        pass

    def _set_effect(self, effect, effect_rate):
        """Set the effect for this move."""
        ###--TO DO--###
        # add code to properly set an effect to the move
        pass
