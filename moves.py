"""Contains classes relating to a battle moves that pokemon can use."""
import csv

import battle_effects


class Move:
    """Interface for a pokemon's battle move."""

    def __init__(self, name, move_file):
        """Constructor for the Move class.

        This constructor should be called with the name of the move to create
        and a csv that contains the information defining the move.
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

    ########## Class Constants ##########

    ########## Properties ##########
    @property
    def name(self):
        """The name of the move."""
        return self._move_info["name"]

    @property
    def type(self):
        """The type of the move."""
        return self._move_info["type"]

    @property
    def category(self):
        """The category of the move.

        Valid categories include: physical, special, other.
        """
        return self._move_info["category"]

    @property
    def pp_max(self):
        """The maximum value for this move's power points."""
        return self._move_info["pp_max"]

    @property
    def pp_cur(self):
        """The current value for this move's power points."""
        return self._move_info["pp_cur"]

    @pp_cur.setter
    def pp_cur(self, value):
        if value > self._move_info["pp_max"] or value < 0:
            raise ValueError(f"Improper value for current pp: {value}")
        self._move_info["pp_cur"] = value

    @property
    def base_power(self):
        """The base power for this move.

        Moves that do not deal damage will have a base power of None.
        """
        return self._move_info["base_power"]

    @property
    def accuracy(self):
        """The accuracy for this move.

        Moves that cannot miss will have an accuracy of None.
        """
        return self._move_info["accuracy"]

    @property
    def flavor_text(self):
        """The simple description for this move."""
        return self._move_info["flavor_text"]

    @property
    def effect(self):
        """The effect that may be applied by this move.

        Moves that do not have additional effects will have an effect of None.
        """
        ###--TO DO--###
        # add code to properly set an effect to the move
        # should return a tuple of 2 items; the name of the effect and a
        # function used to apply the effect to a target
        return self._move_info["effect"]

    @property
    def effect_rate(self):
        """The chance that the additional effect will occur, if present.

        If this move has no additional effect or if the effect cannot fail,
        this property will be None
        """
        return self._move_info["effect_rate"]

    @property
    def cit_ratio(self):
        """The chance this damaging move will deal critical damage.

        Moves that cannot deal critical damage will have a critical ratio of
        sNone.
        """
        return self._move_info["cit_ratio"]

    @property
    def priority(self):
        """The speed priority for this move.

        Moves with a higher priority will always go before one with lower
        priorirty. If both moves have the same priority, the pokemon with the
        higher speed stat will act first.
        """
        return self._move_info["priority"]

    @property
    def target(self):
        """The target of this move.

        Suitable values for a target are:
        self, single_adjacent_foe, single_adjacent_any, single_adjacent_ally,
        single_any, user_or_adjacent_ally, all_adjacent_foe, all_adjacent_any,
        all_foes, field, team, special.
        """
        return self._move_info["target"]

    @property
    def contact(self):
        """Whether the move makes physical contact with its target."""
        return self._move_info["contact"]

    @property
    def sound(self):
        """Whether the move utilizes sound."""
        return self._move_info["sound"]

    @property
    def punch(self):
        """Whether the move is a punch."""
        return self._move_info["punch"]

    @property
    def biting(self):
        """Whether the move is a biting move."""
        return self._move_info["biting"]

    @property
    def snatchable(self):
        """Whether the move is snatchable."""
        return self._move_info["snatchable"]

    @property
    def gravity(self):
        """Whether the move is affected by gravity."""
        return self._move_info["gravity"]

    @property
    def defrost(self):
        """Whether the move defrosts the pokemon if it is frozen."""
        return self._move_info["defrost"]

    @property
    def reflectable(self):
        """Whether the move can be reflected by magic coat or magic bounce."""
        return self._move_info["reflectable"]

    @property
    def blockable(self):
        """Whether the move can be blocked by protect or detect."""
        return self._move_info["blockable"]

    @property
    def copyable(self):
        """Whether the move can be copied by mirror move."""
        return self._move_info["copyable"]


    ########## Class/Static Methods ##########

    ########## Instance Methods ##########
    def _parse_info(self, move_info):
        """Parse the supplied dictionary for info to initialize this move."""
        if not battle_effects.verify_move(move_info):
            raise ValueError("Error reading move information: "
                             f"{move_info["name"]}")

        self._pp_up = 0
        self._base_pp_max = move_info["pp_max"]
        move_info["pp_cur"] = move_info["pp_max"]
        self._move_info = move_info

    def execute(self, source_pokemon, target_pokemon, field):
        """Perform this move on the target.

        If a pokemon uses a move on itself, both the source and target pokemon
        should be the same object. Any effects on the field that may alter the
        move will be applied. A numerical status code will be returned to
        signify the result of the move. Code are as follows:
            0  - the move succeeded normally
            1  - the damaging move has scored a critical hit
            2  - the damaging move has scored a critical hit due to affection
            3  - the damaging move was super effective due to type match ups
            4  - the damaging move was not very effective due to type match ups
            5  - the move had no effect due to type match ups
            6  - the move has missed due to low accuracy or high evasion
            7  - the move has missed due to the target's high friendship
            8  - the move's effect cannot be applied due to the target already
                 being affected
            9  - the move failed due to the source being paralyzed
            10 - the move failed due to the source being asleep
            11 - the move failed due to the source being confused
            12 - the move failed due to the source being infatuated
            13 - the move failed due to the target blocking the move
            14 - the move failed due to the source's disobedience
            15 - the move failed due to some other factor
        """
        status_code = battle_effects.apply_move(self._move_info,
            source_pokemon, target_pokemon, field)
        return status_code

    def pp_up(self, amount):
        """Increase the max power points of this move a certain amount of times.

        amount should be an integer. Integers less than 1 are ignored, and any
        greater than 3 are treated as 3. Note that the maximum amount of times
        a move's pp can be raised is 3 times. For each time a move's max pp has
        increased, it will increase by 1/5th of its base value.
        """
        if amount > 3:
            amount = 3

        while self._pp_up < 3 and amount > 0:
            increase = self._base_pp_max / 5
            self._move_info["pp_max"] += increase
            self._pp_up += 1
            amount -= 1
