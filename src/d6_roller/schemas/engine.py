from typing import Self
from pydantic import BaseModel, Field, PositiveInt, NonNegativeInt, model_validator
from .lazyint import RandInt


class SequenceThreshold(BaseModel):
    to_hit: PositiveInt | None = Field(gt=1, le=6)
    to_wound: PositiveInt = Field(gt=1, le=6)
    save: PositiveInt | None = Field(gt=1, le=6)


class Sequence(BaseModel):
    attacks: RandInt
    threshold: SequenceThreshold
    damage: RandInt

    def __str__(self):
        attacks = f'{self.attacks} attacks'
        hit = f'{self.threshold.to_hit}+ to hit' if self.threshold.to_hit else 'autohit'
        wound = f'{self.threshold.to_wound}+ to wound'
        save = f'{self.threshold.save}+ to save' \
            if self.threshold.save else 'no save'
        damage = f'with {self.damage} damage each'
        return f'{attacks}, {hit}, {wound}, {save} {damage}'


class RollResult(BaseModel):
    success: NonNegativeInt
    crit: NonNegativeInt

    @model_validator(mode='after')
    def is_correct(self) -> Self:
        if self.crit > self.success:
            raise ValueError('crit value cannot exceed success value')
        return self

    def __str__(self):
        return f'{self.success} total, {self.crit} crits'
