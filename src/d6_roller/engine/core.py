import numpy as np
from numpy import random
from ..schemas import Profile, Weapon, Sequence
from ..math import get_thresholds, d6, d3


def roll_hit(dice: int, threshold: int) -> np.array:
    roll = np.array([random.choice(d6) for _ in range(dice)])
    return roll[roll >= threshold].size


def roll_save(dice: int, threshold: int | None) -> np.array:
    if not threshold:
        return dice
    roll = np.array([random.choice(d6) for _ in range(dice)])
    return roll[roll < threshold].size


def inflict_damage(dice: int, value: int) -> np.array:
    roll = np.array([value for _ in range(dice)])
    return roll


def make_rolls(sequence: Sequence) -> list[int]:
    dice = roll_hit(sequence.attacks, sequence.threshold.to_hit)
    print(f'rolled {dice} successful hits')
    dice = roll_hit(dice, sequence.threshold.to_wound)
    print(f'rolled {dice} successful wounds')
    dice = roll_save(dice, sequence.threshold.save)
    print(f'rolled {dice} failed saves')
    return inflict_damage(dice, sequence.damage)


def simulate(attacker: Weapon, defender: Profile):
    sequence = Sequence(
        attacks=attacker.a,
        threshold=get_thresholds(attacker, defender),
        damage=attacker.d
    )
    print(f'Attacking {defender} with {attacker}')
    print(sequence)
    rolls = make_rolls(sequence)
    print(rolls)
    print(f'total damage {np.sum(rolls)}')
