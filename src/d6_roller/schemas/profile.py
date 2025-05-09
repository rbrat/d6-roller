from pydantic import BaseModel, Field, PositiveInt, NonPositiveInt
from .lazyint import RandInt


class Weapon(BaseModel):
    __rand_fields__ = ['a', 'd']

    name: str = Field()
    a: RandInt = Field()
    skill: PositiveInt | None = Field(gt=1, le=6)
    s: PositiveInt = Field()
    ap: NonPositiveInt = Field()
    d: RandInt = Field()

    def _convert_random_fields(self, data):
        for field_name in self.__rand_fields__:
            if field_name in data:
                data[field_name] = RandInt(value=str(data[field_name]))
        return data

    def __init__(self, **data):
        data = self._convert_random_fields(data)
        super().__init__(**data)

    def __str__(self):
        skill = f'{self.skill}+' if self.skill else 'N/A'
        return f"""{self.name} [A {self.a} BS/WS {skill} S {self.s} AP {self.ap} D {self.d}]"""


class MeleeWeapon(Weapon):
    ...


class RangedWeapon(Weapon):
    range: PositiveInt = Field()


class Profile(BaseModel):
    name: str = Field()
    t: PositiveInt = Field()
    sv: PositiveInt = Field(gt=1, le=6)
    w: PositiveInt = Field()
    inv: PositiveInt | None = Field(default=None, gt=1, le=6)
    ranged_weapons: list[RangedWeapon] | None = Field(default=[])
    melee_weapons: list[MeleeWeapon] | None = Field(default=[])

    def __str__(self):
        inv = f'INV {self.inv}+ ' if self.inv else ''
        return f'{self.name} [T {self.t} Sv {self.sv}+ {inv}W {self.w}]'


Unit = list[Profile]
