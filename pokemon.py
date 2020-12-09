class Pokemon():
    """Class to define a pokemon."""
    # Valid types for pokemon
    valid_types = ["Bug", "Dark", "Dragon", "Electric", "Fighting", "Fighting",
                   "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice",
                   "Normal", "Poison", "Psychic", "Rock", "Steel", "Water"]

    def __init__(self, id, region, name, poke_type, max_HP, cur_HP, moves, level=1):
        """Initialize a single Pokemon.

        Keyword arguments:
        id        -- the national pokedex id of the pokemon
        region    -- a tuple containining the region name and regional pokedex
                     id of the pokemon
        name      -- the name of the pokemon, or nickname if it has one
        poke_type -- an iterable of the type(s) of the pokemon. Can be at most
                     2 types, but must still be an iterable even if only 1 type
                     is given
        max_HP    -- the maximum health value of the pokemon. Must be at least 1
        cur_HP    -- the current health value of the pokemon. Cannot be greater
                     than max_HP
        moves     --
        level
        """
        self._natl_id = id
        self._region , self._region_id = region
        self._name = name
        if level > 100 or < 1:
            raise ValueError("Pokemon's level must be between 1 and 100.")
        else:
            self._level = level
        if poke_type not in Pokemon.valid_types:
            raise ValueError(f"{poke_type} is not a valid type.")
        else:
            self._poke_type = poke_type
        if max_HP <= 0:
            raise ValueError("Max HP must be greater than 0.")
        else:
            self._max_HP = max_HP
        if cur_HP < 0 or cur_HP > self._max_HP:
            raise ValueError("Not a valid value for current HP.")
        else:
            self._cur_HP = cur_HP
        if self._cur_HP != 0:
            self._fainted = False
        else:
            self._fainted = True
        self._moves = moves

    def check_fainted(self):
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
        self.check_fainted()

    def gain_health(health):
        if health + self._cur_HP >= self._max_HP:
            self._cur_HP = self._max_HP
        else:
            self._cur_HP += health
        self.check_fainted()
        print(f"{self._name} has been restored {health} points of health. "
              f"Current HP is {self._cur_HP}")

    def attack(self, other_pokemon):
        pass
