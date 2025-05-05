from src.d6_roller.engine.core import roll_hit, roll_save, inflict_damage, make_rolls, simulate
from src.d6_roller.schemas.lazyint import RandInt
from src.d6_roller.schemas.engine import Sequence, SequenceThreshold
from ..mocks import weapon_bolter, profile_intercessor


class TestCore:
    def test_roll_hit(self):
        assert (0 <= roll_hit(1, 3) <= 1)
        assert (0 <= roll_hit(2, 2) <= 2)
        assert roll_hit(2, None) == 2

    def test_roll_save(self):
        assert roll_save(2, None) == 2
        assert 0 <= roll_save(1, 3) <= 1
        assert 0 <= roll_save(2, 6) <= 2

    def test_inflict_damage(self):
        assert inflict_damage(1, RandInt(2)) == 2
        assert 1 <= inflict_damage(1, RandInt('D6')) <= 6
        assert 3 <= inflict_damage(1, RandInt('2D6+1')) <= 13
        assert 3 <= inflict_damage(3, RandInt('D6')) <= 18

    def test_make_rolls(self):
        sequence = Sequence(
            attacks=RandInt(2),
            threshold=SequenceThreshold(to_hit=3, to_wound=4, save=3),
            damage=RandInt(1)
        )
        assert 0 <= make_rolls(sequence) <= 2
        sequence = Sequence(
            attacks=RandInt('D6'),
            threshold=SequenceThreshold(to_hit=None, to_wound=3, save=4),
            damage=RandInt(1)
        )
        assert 0 <= make_rolls(sequence) <= 6

    def test_simulate(self):
        assert 0 <= simulate(weapon_bolter, profile_intercessor) <= 2
