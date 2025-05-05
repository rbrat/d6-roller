import pytest
from ..mocks import profile_intercessor, profile_terminator, weapon_bolter, weapon_ccw
from d6_roller.schemas.profile import MeleeWeapon, RangedWeapon, Profile
from pydantic_core import ValidationError


class TestProfile:
    def test_creation(self):
        with pytest.raises(ValidationError) as exc:
            Profile(name='wrong toughness', t=-1, sv=3, w=2)
        assert exc.type is ValidationError
        with pytest.raises(ValidationError) as exc:
            Profile(name='wrong save', t=-1, sv=7, w=2)
        assert exc.type is ValidationError
        with pytest.raises(ValidationError) as exc:
            Profile(name='wrong wounds', t=4, sv=3, w=0)
        assert exc.type is ValidationError

    def test_str(self):
        assert str(profile_intercessor) == 'intercessor [T 4 Sv 3+ W 2]'
        assert str(profile_terminator) == 'terminator [T 5 Sv 2+ INV 4+ W 3]'

    def test_invuln(self):
        with pytest.raises(ValidationError) as exc:
            Profile(name='wrong invuln', t=5, sv=2, w=3, inv=1)
        assert exc.type is ValidationError


class TestWeapon:
    def test_melee_creation(self):
        with pytest.raises(ValidationError) as exc:
            MeleeWeapon(name='wrong ap', skill=3, a=1, s=4, ap=2, d=1)  # type: ignore
        assert exc.type is ValidationError
        with pytest.raises(ValidationError) as exc:
            MeleeWeapon(name='wrong skill', skill=1, a=1, s=4, ap=-2, d=1)  # type: ignore
        assert exc.type is ValidationError
        with pytest.raises(ValueError) as exc:
            MeleeWeapon(name='wrong damage', skill=1, a=1, s=4, ap=-2, d='D20')  # type: ignore
        assert exc.type is ValueError

    def test_ranged_creation(self):
        with pytest.raises(ValidationError) as exc:
            RangedWeapon(name='no range', skill=2, a=1, s=4, ap=2, d=1)  # type: ignore
        assert exc.type is ValidationError

    def test_str(self):
        assert str(weapon_ccw) == 'close combat weapon [A 3 BS/WS 3+ S 4 AP 0 D 1]'
        assert str(weapon_bolter) == 'bolt rifle [A 2 BS/WS 3+ S 4 AP -1 D 1]'
