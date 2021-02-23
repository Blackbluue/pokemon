"""Pokemon module. Contains classes relating to a single instance of a pokemon.
"""

class Pokemon:
    """Class to define a single pokemon."""

    def __init__(self, natl_id, location, name, types, stats, moves, ability,
                 happiness=0, ivs=None, shiny=None, level=1, ot=None,
                 ot_id=None, nicknamed=False):
        """Initialize a single Pokemon.

        Keyword arguments:
        natl_id   -- the national pokedex id of the pokemon
        location  -- the location code where the pokemon was first encountered
                     by its original trainer
        name      -- the name of the pokemon, or nickname if it has one
        types     -- an iterable of the type(s) of the pokemon. Can be at most
                     2 types, but must still be an iterable even if only 1 type
                     is given
        stats     -- a dictionary containing the current stats of the pokemon.
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
        moves     -- an iterable of the usable moves for this pokemon.
                     Can be 1 to 4 moves
        happiness -- any adjustment to the initial happiness value of the
                     pokemon. This should not include the base happiness of the
                     pokemon species (default 0)
        ivs       -- individual vaules for each stat. These - along with the base
                     stats for the species and the level - determine the stats
                     for the pokemon. If None is given, or if any value in the
                     given dictionary is None, ivs will be generated randomly.
                     (default None)
        level     -- the current level of the pokemon. Must be between 1 and 100
                     (default 1)
        shiny     -- determine if the pokemon is shiny. If None, shiny state
                     will be determined randomly (default None)
        ot        -- the name of the trainer who originally caught the pokemon.
                     Should be left None for wild pokemon (default None)
        ot_id     -- the id number of the original trainer (default None)
        """

        self._natl_id = id
        self._location = location
        ###--TO DO--###
        # make a trainer class
        self._original_trainer = ot
        self._original_trainer_id = ot_id
        self._name = name
        self._level = level
        ###--TO DO--###
        # types should be pulled from pokedex entry for consistency
        for poke_type in types:
            if poke_type not in self.VALID_TYPES:
                raise ValueError(f"{poke_type} is not a valid type.")
        self._types = types
        ###--TO DO--###
        # neet to rework to incorporate base stats and IVs. clients should not
        # be able to directly set the stats for a pokemon
        self._initialize_stats(stats, ivs)
        if self._cur_HP != 0:
            self._fainted = False
        else:
            self._fainted = True
        ###--TO DO--###
        # need to add validation/initialization methods for moves
        self._moves = moves
        ###--TO DO--###
        # add base happiness value from pokemon species
        self._happiness = happiness
        ###--TO DO--###
        # add way to randomly set a pokemon to shiny if initial value not given
        if shiny == None:
            self._shiny = False
        else:
            self._shiny = shiny
        self.status = None
        self.hidden_status = None
        self._pokerus = None

    ########## Class Constants ##########

    ###--TO DO--###
    # as types will soon be retrieved from pokedex entries, this list will be
    # removed
    # Valid types for pokemon
    VALID_TYPES = ("Bug", "Dark", "Dragon", "Electric", "Fighting", "Fighting",
                   "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice",
                   "Normal", "Poison", "Psychic", "Rock", "Steel", "Water")

    ########## Properties ##########
    @property
    def natl_id(self):
        """The national pokedex id of the pokemon.

        The national pokedex id of a pokemon is a defining unique number for
        that pokemon, and is not tied to a specific region; no two different
        pokemon species may have the same national id regardless of where it was
        encountered
        """
        return self._natl_id

    @property
    def region_id(self):
        """The regional pokedex id of the pokemon.

        The regional pokedex id is similar to the national id, except that the
        same pokemon species may have different regional ids depending on which
        regional pokedex is being searched. The regional id returned from this
        property is dependent on where the trainer that currently owns this
        pokemon is in the pokemon world.
        """
        return self._region_id

    @property
    def original_trainer(self):
        """The name of the trainer who originally caught the pokemon.

        Should be left None for wild pokemon. Once set, it cannot be changed.
        """
        ###--TO DO--###
        # currently returns a string. Need to make a trainer class
        return self._original_trainer

    @property
    def original_trainer_id(self):
        """The id number of the trainer who originally caught the pokemon.

        Should be left None for wild pokemon. Once set, it cannot be changed.
        """
        ###--TO DO--###
        # currently returns a string. Need to make a trainer class
        return self._original_trainer_id

    @property
    def location(self):
        """Where the pokemon was first encountered by its original trainer.

        This is a location code that defines a specific locale within the
        pokemon world where this pokemon was first encountered by its original
        trainer. This code may not be human readable; the human readable name
        can be obtained by using this code with the PokeEarth interface.

        This locale is in refernce to the original trainer of this pokemon, not
        the currently owning trainer. Should be left None for wild pokemon.
        """
        return self._location

    @property
    def name(self):
        """The name of the pokemon, or nickname if it has one."""
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def level(self):
        """The current level of the pokemon.

        The level of a pokemon is a rough estimation of the overal power of
        that pokemon. The level must be between 1 and 100 inclusive.
        """
        return self._level

    @level.setter
    def level(self, level):
        if level > 100 or < 1:
            raise ValueError("Pokemon's level must be between 1 and 100.")
        else:
            self._level = level

    @property
    def status(self):
        """The current status condition of the pokemon.

        A pokemon can only have a single status condition at a time.
        """
        return self._status

    @status.setter
    def status(self, status):
        ###--TO DO--###
        # flesh out status system
        self._status = status

    @status.deleter
    def status(self):
        self._status = None

    @property
    def hidden_status(self):
        """The hidden status condition of the pokemon.

        A pokemon can only have a single hidden status condition at a time.
        A pokemon can have a hidden status and normal status condition
        simultaneously.
        """
        return self._hidden_status

    @hidden_status.setter
    def hidden_status(self, hidden_status):
        ###--TO DO--###
        # flesh out status system
        self._hidden_status = hidden_status

    @hidden_status.deleter
    def hidden_status(self):
        self._hidden_status = None

    @property
    def pokerus(self):
        """A rare condition that increases the evs obtained by a pokemon.

        Once contracted, the virus will spread to other pokemon in the party.
        The pokemon will eventually recover from the infection, stopping the
        spread while retaining all positive effects. Once cured, the pokemon
        is immune and cannot be infected by the virus again. A True value means
        the pokemon is infected and can spread the virus. A False value means
        the pokemon has been cured of the virus and is immune to further
        infection. A None value means the pokemon has never encountered the
        virus before and can be infected.
        """
        ###--TO DO--###
        # flesh out pokerus status
        return self._pokerus

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
        self._check_fainted()

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

    @property
    def ivs(self):
        """A dictionary containing the individual values of the pokemon.

        The key for these stats must be exact, and include:
            iv_max_HP       -- the maximum health iv of the pokemon
            iv_attack       -- the physical attack iv of the pokemon
            iv_defense      -- the pyhsical defense iv of the pokemon
            iv_sp_attack    -- the special attack iv of the pokemon
            iv_sp_defense   -- the special defense iv of the pokemon
            iv_speed        -- the speed iv of the pokemon
        All ivs must be at least 1, maxed out at 31. The ivs property returns a
        copy of the ivs dictionary; it cannot be used to modify the pokemon's
        ivs directly.
        """
        return self._ivs.copy()

    @property
    def evs(self):
        """A dictionary containing the effort values of the pokemon.

        The key for these stats must be exact, and include:
            ev_max_HP       -- the maximum health ev of the pokemon
            ev_attack       -- the physical attack ev of the pokemon
            ev_defense      -- the pyhsical defense ev of the pokemon
            ev_sp_attack    -- the special attack ev of the pokemon
            ev_sp_defense   -- the special defense ev of the pokemon
            ev_speed        -- the speed ev of the pokemon
        All evs are initially set to 0, maxed out at 255. The evs property
        returns a copy of the evs dictionary; it cannot be used to modify the
        pokemon's evs directly. Use the dedicated instance method to modify
        evs.
        """
        return self._evs.copy()

    @property
    def shiny(self):
        """Determine if the pokemon is shiny.

        Shiny pokemon have unique colorations and/or appearances; all other
        stats should be identical to their non-shiny counterparts. Shiny status
        is determined at pokemon birth and cannot change."""
        return self._shiny

    ########## Class/Static Methods ##########
    @staticmethod
    def _iv_checker(iv):
        return True if (iv >= 1 and iv <= 31) else False

    ########## Instance Methods ##########
    def _initialize_stats(self, stats, ivs):
        """Initialize the pokemon's stats with a set of given stats and ivs."""
        self._ivs = {}
        if ivs == None:
            ###--TO DO--###
            # create a process to randomly generate ivs if not given
            self._ivs = {"iv_max_HP": 15, "iv_attack": 15,
                         "iv_defense": 15, "iv_sp_attack": 15,
                         "iv_sp_defense": 15, "iv_speed": 15}
        else:
            iv_names = ["iv_max_HP", "iv_attack", "iv_defense",
                        "iv_sp_attack", "iv_sp_defense", "iv_speed"]
            for iv_name in iv_names:
                if iv_name not in ivs:
                    raise ValueError(f"iv {iv_name} not found")
                elif ivs[iv_name] == None:
                    ###--TO DO--###
                    # create a process to randomly generate ivs if not given
                    self._ivs[iv_name] = 15
                elif not Pokemon._iv_checker(ivs[iv_name]):
                    raise ValueError(f"Inappropriate value for ivs; "
                    f"{iv_name}: {ivs[iv_name]}")
                else:
                    self._ivs[iv_name] = ivs[iv_name]

        # each initialization also checks proper values in property setters
        ###--TO DO--###
        # make initial stats based on base stats of pokemon species and set ivs
        self._stats = {}
        self.max_HP = stats["max_HP"]
        self.cur_HP = stats["cur_HP"]
        self.attack = stats["attack"]
        self.defense = stats["defense"]
        self.sp_attack = stats["sp_attack"]
        self.sp_defense = stats["sp_defense"]
        self.speed = stats["speed"]

        self._evs = {}
        self._evs["ev_max_HP"] = 0
        self._evs["ev_attack"] = 0
        self._evs["ev_defense"] = 0
        self._evs["ev_sp_attack"] = 0
        self._evs["ev_sp_defense"] = 0
        self._evs["ev_speed"] = 0

    def _check_fainted(self):
        # used to check if fainted status changed
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

    def launch_attack(self, other_pokemon):
        pass

    def set_original_trainer(self, ot, ot_id):
        """Sets the original trainer for this pokemon. Can only be set once."""
        ###--TO DO--###
        # add proper checking for original trainer id, along with implementaion
        # of trainer class
        if self._original_trainer != None:
            raise AttributeError("Original trainer cannot be changed again")
        elif ot == None or ot_id == None:
            raise ValueError(
                f"Improper value for original trainer: {ot} {ot_id}")
        else:
            self._original_trainer = ot
            self._original_trainer_id = ot_id

    def pokerus_infect(self):
        """Infect the pokemon with pokerus.

        If the pokemon currently has pokerus, or has been previously cured of
        it, its status will not change. The pokemon will only be infected if it
        has never before been in contact with the virus. The pokemon will always
        posses the positive effects of pokerus after a call to this method,
        regardless of previous infection status.
        """
        if self._pokerus == None:
            self._pokerus = True
