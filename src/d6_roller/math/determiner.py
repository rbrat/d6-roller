from ..schemas.profile import Profile, Weapon
from ..schemas.engine import SequenceThreshold


def hit(attacker: Weapon) -> int:
    return attacker.skill


def wound(attacker: Weapon, defender: Profile) -> int:
    if attacker.s == defender.t:
        return 4
    if attacker.s > defender.t:
        diff_value = attacker.s // defender.t
        if diff_value >= 2:
            return 2
        else:
            return 3
    else:
        diff_value = defender.t // attacker.s
        if diff_value >= 2:
            return 6
        else:
            return 5


def save(attacker: Weapon, defender: Profile) -> int:
    diff_value = defender.sv - attacker.ap
    if defender.inv and diff_value > defender.inv:
        return defender.inv
    if diff_value > 6:
        return None
    return diff_value


def get_thresholds(attacker: Weapon, defender: Profile) -> dict:
    return SequenceThreshold(**{
        'to_hit': hit(attacker),
        'to_wound': wound(attacker, defender),
        'save': save(attacker, defender)
    })
