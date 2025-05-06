from ..logger import logger
import numpy as np
from numpy import random

from ..math import get_thresholds
from ..schemas.profile import Profile, Weapon
from ..schemas.engine import Sequence
from ..schemas.lazyint import RandInt
from ..schemas.dice import d6

CHECK_DICT = {
    True: np.ndarray.__ge__,
    False: np.ndarray.__lt__,
}


def make_rolls(dice: int, threshold: int | None, is_positive: bool = False) -> int:
    if not threshold:
        return dice
    roll = np.array([random.choice(d6) for _ in np.arange(dice)])
    logger.info("Dice rolled %s", roll)
    return roll[CHECK_DICT[is_positive](roll, threshold)].size


def roll_positive_check(dice: int, threshold: int | None) -> int:
    return make_rolls(dice, threshold, True)


def roll_negative_check(dice: int, threshold: int | None) -> int:
    return make_rolls(dice, threshold, False)


def inflict_damage(dice: int, value: RandInt) -> int:
    roll = np.array([value.get for _ in np.arange(dice)])
    return np.sum(roll)


def run_sequence(sequence: Sequence) -> int:
    dice = roll_positive_check(sequence.attacks.get, sequence.threshold.to_hit)
    logger.info('rolled %s successful hits', dice)
    dice = roll_positive_check(dice, sequence.threshold.to_wound)
    logger.info('rolled %s successful wounds', dice)
    dice = roll_negative_check(dice, sequence.threshold.save)
    logger.info('rolled %s failed saves', dice)
    return inflict_damage(dice, sequence.damage)


def simulate(attacker: Weapon, defender: Profile) -> int:
    sequence = Sequence(
        attacks=attacker.a,
        threshold=get_thresholds(attacker, defender),
        damage=attacker.d
    )
    logger.info('Attacking %s with %s', defender, attacker)
    logger.info(sequence)
    damage = run_sequence(sequence)
    return damage
