import pytest
from src.d6_roller.schemas.lazyint import RandInt


class TestRandint:
    def test_static(self):
        with pytest.raises(ValueError) as exc:
            RandInt(-3)
        assert exc.type is ValueError
        assert RandInt(3).get == 3
        assert RandInt(6).get == 6

    def test_random(self):
        assert (1 <= RandInt('D6').get <= 6)
        assert (1 <= RandInt('D3').get <= 3)
        with pytest.raises(ValueError) as exc:
            RandInt('D20')
        assert exc.type is ValueError

    def test_multi_dice(self):
        assert (2 <= RandInt('2D6').get <= 12)
        assert (3 <= RandInt('3D6').get <= 18)

    def test_combined(self):
        assert (2 <= RandInt('D6+1').get <= 7)
        assert (4 <= RandInt('2D6+2').get <= 14)
        assert (4 <= RandInt('D3+3').get <= 6)
        assert (6 <= RandInt('3D3+3').get <= 12)

    def test_str(self):
        assert str(RandInt('D6')) == 'D6'
        assert str(RandInt('D3')) == 'D3'
        assert str(RandInt('d3')) == 'D3'
        assert str(RandInt('D6+1')) == 'D6+1'
        assert str(RandInt('3D6')) == '3D6'
        assert str(RandInt('2D6 + 1')) == '2D6+1'
