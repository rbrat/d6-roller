import numpy as np
from numpy import random

from ..math import get_thresholds
from ..schemas.profile import Profile, Weapon
from ..schemas.engine import Sequence
from ..schemas.lazyint import RandInt
from ..schemas.dice import d6


def roll_hit(dice: int, threshold: int | None) -> int:
    if not threshold:
        return dice
    roll = np.array([random.choice(d6) for _ in range(dice)])
    return roll[roll >= threshold].size


def roll_save(dice: int, threshold: int | None) -> int:
    if not threshold:
        return dice
    roll = np.array([random.choice(d6) for _ in range(dice)])
    return roll[roll < threshold].size


def inflict_damage(dice: int, value: RandInt) -> int:
    roll = np.array([value.get for _ in range(dice)])
    return np.sum(roll)


def make_rolls(sequence: Sequence) -> int:
    dice = roll_hit(sequence.attacks.get, sequence.threshold.to_hit)
    print(f'rolled {dice} successful hits')
    dice = roll_hit(dice, sequence.threshold.to_wound)
    print(f'rolled {dice} successful wounds')
    dice = roll_save(dice, sequence.threshold.save)
    print(f'rolled {dice} failed saves')
    return inflict_damage(dice, sequence.damage)


def simulate(attacker: Weapon, defender: Profile) -> int:
    sequence = Sequence(
        attacks=attacker.a,
        threshold=get_thresholds(attacker, defender),
        damage=attacker.d
    )
    print(f'Attacking {defender} with {attacker}')
    print(sequence)
    damage = make_rolls(sequence)
    return damage
