from .mocks import profile_intercessor, profile_terminator, weapon_bolter, weapon_ccw


class TestProfile:
    def test_creation(self):
        assert str(profile_intercessor) == 'intercessor [T 4 Sv 3+ W 2]'

    def test_invuln(self):
        assert str(profile_terminator) == 'terminator [T 5 Sv 2+ INV 4+ W 3]'


class TestWeapon:
    def test_melee_creation(self):
        assert str(weapon_ccw) == 'close combat weapon [A 3 BS/WS 3+ S 4 AP 0 D 1]'

    def test_ranged_creation(self):
        assert str(weapon_bolter) == 'bolt rifle [A 2 BS/WS 3+ S 4 AP -1 D 1]'
