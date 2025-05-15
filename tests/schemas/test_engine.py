import pytest
from pydantic_core import ValidationError
from d6_roller.schemas.engine import RollResult


class TestRollResult:
    def test_creation(self):
        assert RollResult(success=2, crit=0) == RollResult(success=2, crit=0)
        with pytest.raises(ValidationError) as exc:
            RollResult(success=2, crit=5)
        assert exc.type is ValidationError
        with pytest.raises(ValidationError) as exc:
            RollResult(success=-2, crit=0)
        assert exc.type is ValidationError
        with pytest.raises(ValidationError) as exc:
            RollResult(success=2, crit=-1)
        assert exc.type is ValidationError
