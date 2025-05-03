import numpy as np
from numpy import random
from pydantic import BaseModel, Field
from functools import reduce
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
    dice_num: int = Field(default=None)
    dice_size: str = Field(default=None)
    stationary: int = Field(default=None)

    def __init__(self, value: str, **data):
        super().__init__(**data)
        if not value:
            return
        value = value.upper().replace(' ', '')
        if 'D' not in value:  # stationary value, no roll required
            self.stationary = int(value)
            return
        if '+' in value:  # both stationary and random parts
            dice, stationary = value.split('+', maxsplit=2)
        else:
            dice, stationary = value, 0
        num, size = dice.split('D')
        self.dice_num = int(num or 1)
        self.dice_size = size
        self.stationary = int(stationary)

    @property
    def get(self) -> int:
        result = 0
        if self.dice_num:
            result = reduce(random.choice, [DICE_MAP[self.dice_size] for _ in range(self.dice_num)], 0)
        result += self.stationary
        return result

    def __str__(self):
        if not self.dice_num:
            return str(self.stationary)
        stationary = f'+{self.stationary}' if self.stationary else ''
        if len(self.dice_num) == 1:
            return f'D{len(self.dice[0])}{stationary}'
        return f'{len(self.dice)}D{len(self.dice[0])}{self.stationary}'
