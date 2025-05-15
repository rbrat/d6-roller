from ..logger import logger
import numpy as np

from ..math import get_thresholds
from ..schemas.profile import Profile, Weapon
from ..schemas.engine import RollResult, Sequence
from ..schemas.lazyint import RandInt
from ..schemas.dice import d6

CHECK_DICT = {
    True: np.ndarray.__ge__,
    False: np.ndarray.__lt__,
}


def make_rolls(dice: int, threshold: int | None, is_positive: bool = False, crit: int | None = None) -> RollResult:
    if not threshold:
        return RollResult(success=dice, crit=0)
    crits = 0
    roll = np.array([np.random.choice(d6) for _ in np.arange(dice)])
    logger.info("Dice rolled %s", roll)
    success = roll[CHECK_DICT[is_positive](roll, threshold)].size
    if is_positive:
        crits = roll[roll >= 6].size
    return RollResult(success=success, crit=crits)


def roll_positive_check(dice: int, threshold: int | None, crit: int | None = None) -> RollResult:
    return make_rolls(dice, threshold, True, crit=crit)


def roll_negative_check(dice: int, threshold: int | None, crit: int | None = None) -> RollResult:
    return make_rolls(dice, threshold, False, crit=crit)


def inflict_damage(dice: int, value: RandInt) -> int:
    roll = np.array([value.get for _ in np.arange(dice)])
    return np.sum(roll)


def run_sequence(sequence: Sequence) -> int:
    hit_result = roll_positive_check(sequence.attacks.get, sequence.threshold.to_hit)
    logger.info('rolled %s successful hits', hit_result)
    wound_result = roll_positive_check(hit_result.success, sequence.threshold.to_wound, crit=hit_result.crit)
    logger.info('rolled %s successful wounds', wound_result)
    save_result = roll_negative_check(wound_result.success, sequence.threshold.save, crit=wound_result.crit)
    logger.info('rolled %s failed saves', save_result)
    return inflict_damage(save_result.success, sequence.damage)


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
