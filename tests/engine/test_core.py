from src.d6_roller.engine.core import roll_positive_check, roll_negative_check, inflict_damage, run_sequence, simulate
from src.d6_roller.schemas.lazyint import RandInt
from src.d6_roller.schemas.engine import Sequence, SequenceThreshold
from ..mocks import weapon_bolter, profile_intercessor


class TestCore:
    def test_roll_positive_check(self):
        assert (0 <= roll_positive_check(1, 3) <= 1)
        assert (0 <= roll_positive_check(2, 2) <= 2)
        assert roll_positive_check(2, None) == 2

    def test_roll_negative_check(self):
        assert roll_negative_check(2, None) == 2
        assert 0 <= roll_negative_check(1, 3) <= 1
        assert 0 <= roll_negative_check(2, 6) <= 2

    def test_inflict_damage(self):
        assert inflict_damage(1, RandInt(2)) == 2
        assert 1 <= inflict_damage(1, RandInt('D6')) <= 6
        assert 3 <= inflict_damage(1, RandInt('2D6+1')) <= 13
        assert 3 <= inflict_damage(3, RandInt('D6')) <= 18

    def test_run_sequence(self):
        sequence = Sequence(
            attacks=RandInt(2),
            threshold=SequenceThreshold(to_hit=3, to_wound=4, save=3),
            damage=RandInt(1)
        )
        assert 0 <= run_sequence(sequence) <= 2
        sequence = Sequence(
            attacks=RandInt('D6'),
            threshold=SequenceThreshold(to_hit=None, to_wound=3, save=4),
            damage=RandInt(1)
        )
        assert 0 <= run_sequence(sequence) <= 6

    def test_simulate(self):
        assert 0 <= simulate(weapon_bolter, profile_intercessor) <= 2
