from collections import UserDict

class Pokemon():
    """Class to define a pokemon."""

    def __init__(self, natl_id, region, name, types, stats, moves, level=1):
        """Initialize a single Pokemon.

        Keyword arguments:
        natl_id  -- the national pokedex id of the pokemon
        region   -- a tuple containining the region name and regional pokedex
                    id of the pokemon
        name     -- the name of the pokemon, or nickname if it has one
        types    -- an iterable of the type(s) of the pokemon. Can be at most
                    2 types, but must still be an iterable even if only 1 type
                    is given
        stats    -- a dictionary containing the current stats of the pokemon.
                    The key for these stats must be exact, and include:
                        max_HP       -- the maximum health value of the pokemon
                        cur_HP       -- the current health value of the pokemon.
                                        Cannot be greater than max_HP
                        attack       -- the physical attack of the pokemon
                        defense      -- the pyhsical defense of the pokemon
                        sp_attack    -- the special attack of the pokemon
                        sp_defense   -- the special defense of the pokemon
                        speed        -- the speed of the pokemon
                    All stats must be at least 1, with the exception of cur_HP
                    which can be 0
        moves    -- an iterable of the usable moves for this pokemon.
                    Can be 1 to 4 moves
        level    -- the current level of the pokemon. Must be between 1 and 100
                    (default 1)
        """

        self._natl_id = id
        self._region, self._region_id = *region
        self.name = name
        self.level = level
        for poke_type in types:
            if poke_type not in self.VALID_TYPES:
                raise ValueError(f"{poke_type} is not a valid type.")
        self._types = types
        self._initialize_stats(stats)
        if self._cur_HP != 0:
            self._fainted = False
        else:
            self._fainted = True
        self._moves = moves  # need to add validation/initialization methods

    ########## Class Constants ##########
    # Valid types for pokemon
    VALID_TYPES = ("Bug", "Dark", "Dragon", "Electric", "Fighting", "Fighting",
                   "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice",
                   "Normal", "Poison", "Psychic", "Rock", "Steel", "Water")

    ########## Properties ##########
    @property
    def natl_id(self):
        """The national pokedex id of the pokemon."""
        return self._natl_id

    @property
    def region(self):
        """The region the pokemon was originally encountered."""
        return self._region

    @property
    def region_id(self):
        """The regional pokedex id of the pokemon."""
        return self._region_id

    @property
    def name(self):
        """The name of the pokemon, or nickname if it has one."""
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def level(self):
        """The current level of the pokemon. Must be between 1 and 100 inclusive."""
        return self._level

    @level.setter
    def level(self, level):
        if level > 100 or < 1:
            raise ValueError("Pokemon's level must be between 1 and 100.")
        else:
            self._level = level

    @property
    def types(self):
        """The type(s) of the pokemon."""
        return self._types

    @property
    def stats(self):
        """A dictionary containing the current stats of the pokemon.

        The key for these stats must be exact, and include:
            max_HP       -- the maximum health value of the pokemon
            cur_HP       -- the current health value of the pokemon.
                            Cannot be greater than max_HP
            attack       -- the physical attack of the pokemon
            defense      -- the pyhsical defense of the pokemon
            sp_attack    -- the special attack of the pokemon
            sp_defense   -- the special defense of the pokemon
            speed        -- the speed of the pokemon
        All stats must be at least 1, with the exception of cur_HP which can
        be 0. Each stat also has its own instance property. The stats property
        returns a copy of the stats mappings; it cannot be used to modify the
        pokemon's stats directly. Use the individual stat properties to modify
        values.
        """
        return self._stats.copy()

    @property
    def max_HP(self):
        """The maximum health value of the pokemon."""
        return self._stats["max_HP"]

    @max_HP.setter
    def max_HP(self, max_HP):
        if max_HP <= 0:
            raise ValueError("Max HP cannot be less than 1.")
        self._stats["max_HP"] = max_HP

    @property
    def cur_HP(self):
        """The current health value of the pokemon. Must be less than max_HP."""
        return self._stats["cur_HP"]

    @cur_HP.setter
    def cur_HP(self, cur_HP):
        if cur_HP < 0 or cur_HP > self.max_HP:
            raise ValueError("Improper value for current HP.")
        self._stats["cur_HP"] = cur_HP

    @property
    def attack(self):
        """The attack value of the pokemon."""
        return self._stats["attack"]

    @attack.setter
    def attack(self, attack):
        if attack <= 0:
            raise ValueError("Attack cannot be less than 1.")
        self._stats["attack"] = attack

    @property
    def defense(self):
        """The defense value of the pokemon."""
        return self._stats["defense"]

    @defense.setter
    def defense(self, defense):
        if defense <= 0:
            raise ValueError("Defense cannot be less than 1.")
        self._stats["defense"] = defense

    @property
    def sp_attack(self):
        """The special attack value of the pokemon."""
        return self._stats["sp_attack"]

    @sp_attack.setter
    def sp_attack(self, sp_attack):
        if sp_attack <= 0:
            raise ValueError("Special attack cannot be less than 1.")
        self._stats["sp_attack"] = sp_attack

    @property
    def sp_defense(self):
        """The special defense value of the pokemon."""
        return self._stats["sp_defense"]

    @sp_defense.setter
    def sp_defense(self, sp_defense):
        if sp_defense <= 0:
            raise ValueError("Special defense cannot be less than 1.")
        self._stats["sp_defense"] = sp_defense

    @property
    def speed(self):
        """The speed value of the pokemon."""
        return self._stats["speed"]

    @speed.setter
    def speed(self, speed):
        if speed <= 0:
            raise ValueError("Speed cannot be less than 1.")
        self._stats["speed"] = speed

    ########## Class Methods ##########

    ########## Instance Methods ##########
    def _initialize_stats(self, stats):
        """Initialize the pokemon's stats with a set of given stats.

        This method can also be used when the pokemon levels up. In either
        case, a key-value pair must be supplied for every stat.
        """
        self.max_HP = stats["max_HP"]
        self.cur_HP = stats["cur_HP"]
        self.attack = stats["attack"]
        self.defense = stats["defense"]
        self.sp_attack = stats["sp_attack"]
        self.sp_defense = stats["sp_defense"]
        self.speed = stats["speed"]

    def _check_fainted(self):
        previous_state = self._fainted
        if self._cur_HP == 0:
            self._fainted = True
            if self._fainted != previous_state:
                print(f"{self._name} has fainted.")
        else:
            self._fainted = False
            if self._fainted != previous_state:
                print(f"{self._name} has been revived.")

    def lose_health(self, damage):
        if damage >= self._cur_HP:
            self._cur_HP = 0
        else:
            self._cur_HP -= damage
        print(f"{self._name} has taken {damage} points of damage. "
              f"Current HP is {self._cur_HP}")
        self._check_fainted()

    def gain_health(health):
        if health + self._cur_HP >= self._max_HP:
            self._cur_HP = self._max_HP
        else:
            self._cur_HP += health
        self._check_fainted()
        print(f"{self._name} has been restored {health} points of health. "
              f"Current HP is {self._cur_HP}")

    def attack(self, other_pokemon):
        pass
