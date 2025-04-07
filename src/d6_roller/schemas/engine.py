from pydantic import BaseModel, Field


class SequenceThreshold(BaseModel):
    to_hit: int | None = Field()
    to_wound: int = Field()
    save: int | None = Field()


class Sequence(BaseModel):
    attacks: int = Field()
    threshold: SequenceThreshold = Field()
    damage: int = Field()

    def __str__(self):
        attacks = f'{self.attacks} attacks'
        hit = f'{self.threshold.to_hit}+ to hit'
        wound = f'{self.threshold.to_wound}+ to wound'
        save = f'{self.threshold.save}+ to save' \
            if self.threshold.save else 'no save'
        return f'{attacks}, {hit}, {wound}, {save}'
