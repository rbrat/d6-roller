import numpy as np
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
        self.dice_num = int(num or 1)
        self.dice_size = size
        self.stationary = int(stationary)

    @property
    def get(self) -> int:
        result = 0
        if self.dice_num:
            result = sum([random.choice(DICE_MAP[self.dice_size]) for _ in range(self.dice_num)])
        result += self.stationary
        return result

    def __str__(self):
        if not self.dice_num:
            return str(self.stationary)
        stationary = f'+{self.stationary}' if self.stationary else ''
        if self.dice_num == 1:
            return f'D{self.dice_size}{stationary}'
        return f'{self.dice_num}D{self.dice_size}{stationary}'
