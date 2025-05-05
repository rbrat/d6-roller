from src.d6_roller.math.determiner import get_thresholds, hit, wound, save
from src.d6_roller.schemas.engine import SequenceThreshold
from ..mocks import (
    profile_intercessor,
    profile_terminator,
    weapon_bolter,
    weapon_ccw,
    weapon_mcpw,
    weapon_pyreblaster,
    weapon_shoota,
    weapon_multimelta,
    weapon_shoota_6,
    profile_landraider
)


class TestDeterminer:
    def test_hit(self):
        assert hit(weapon_pyreblaster) is None
        assert hit(weapon_mcpw) == 2
        assert hit(weapon_bolter) == 3
        assert hit(weapon_multimelta) == 4
        assert hit(weapon_shoota) == 5
        assert hit(weapon_shoota_6) == 6

    def test_wound(self):
        assert wound(weapon_multimelta, profile_intercessor) == 2
        assert wound(weapon_pyreblaster, profile_intercessor) == 3
        assert wound(weapon_bolter, profile_intercessor) == 4
        assert wound(weapon_bolter, profile_terminator) == 5
        assert wound(weapon_bolter, profile_landraider) == 6

    def test_save(self):
        assert save(weapon_ccw, profile_intercessor) == 3  # no ap
        assert save(weapon_multimelta, profile_intercessor) is None  # 7+, no save
        assert save(weapon_multimelta, profile_terminator) == 4  # inv 4+
        assert save(weapon_multimelta, profile_landraider) == 6

    def test_cumulative(self):
        assert get_thresholds(weapon_bolter, profile_intercessor) == SequenceThreshold(to_hit=3, to_wound=4, save=4)
        assert get_thresholds(weapon_multimelta, profile_intercessor) == SequenceThreshold(
            to_hit=4, to_wound=2, save=None
        )
        assert get_thresholds(weapon_multimelta, profile_terminator) == SequenceThreshold(to_hit=4, to_wound=3, save=4)
