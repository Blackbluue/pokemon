"""Contains classes and methods used to create effects in battle.

The effects created from this module can result from Pokemon's battle moves,
abilities, or items."""

def verify_move(move_info):
    """Check that the data passed by the info argument is a usable move.

    No effect is actually generated from this function, and no lasting
    operations are performed. A True return value means the move is verified.
    """
    ###--TO DO--###
    # add code to actualyl verify the move
    return True

def apply_move(move_info, source_pokemon, target_pokemon, field):
    """Perform the specified move on the target.

    If a pokemon uses a move on itself, both the source and target pokemon
    should be the same object. Any effects on the field that may alter the
    move will be applied. A numerical status code will be returned to
    signify the result of the move. Codes are as follows:
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

    The actual move_info attribute of a Move object needs to be passed to this
    function, not a copy, in order to apply accurate changes to the current pp
    of the move due to various abilities or other effects on the field. As
    such, this function should only be called directly by a Move object.
    """
    ###--TO DO--###
    # add code to apply the move
    return 0
