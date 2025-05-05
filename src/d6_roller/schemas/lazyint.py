from numpy import random
from pydantic import BaseModel, Field
from .dice import d6, d3

DICE_MAP = {
    '6': d6,
    '3': d3
}


class RandInt(BaseModel):
    """
    this class represents profile values that can be random or determined (e.g. attacks number or damage value),
    like "1", "2" or "D6", "D3+3", "2D6+1".
    DICE_MAP constraints available dice
    """
    dice_num: int = Field(default=0)
    dice_size: str = Field(default='')
    stationary: int = Field(default=0)

    def __init__(self, value: str, **data):
        if not value:
            raise ValueError("Value required")
        super().__init__(**data)
        value = value.upper().replace(' ', '')
        if 'D' not in value:  # stationary value, no roll required
            self.stationary = int(value)
            return
        if '+' in value:  # both stationary and random parts
            dice, stationary = value.split('+', maxsplit=2)
        else:
            dice, stationary = value, 0
        num, size = dice.split('D', maxsplit=2)
        if size not in DICE_MAP.keys():
            raise ValueError('Unknown dice size')
        self.dice_num = int(num or 1)
        self.dice_size = size
        self.stationary = int(stationary)

    @property
    def get(self) -> int:
        match self.dice_num:
            case 0: return self.stationary
            case _:
                return sum([random.choice(DICE_MAP[self.dice_size]) for _ in range(self.dice_num)]) + self.stationary

    def __str__(self):
        match self.dice_num:
            case 0: return str(self.stationary)
            case 1: return f'D{self.dice_size}{f"+{self.stationary}" if self.stationary else ""}'
            case _: return f'{self.dice_num}D{self.dice_size}{f"+{self.stationary}" if self.stationary else ""}'
