from pydantic import BaseModel, Field, PositiveInt
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
        hit = f'{self.threshold.to_hit}+ to hit'
        wound = f'{self.threshold.to_wound}+ to wound'
        save = f'{self.threshold.save}+ to save' \
            if self.threshold.save else 'no save'
        damage = f'with {self.damage} damage each'
        return f'{attacks}, {hit}, {wound}, {save} {damage}'
