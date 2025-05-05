from pydantic import BaseModel, Field
from .lazyint import RandInt


class Weapon(BaseModel):
    __rand_fields__ = ['a', 'd']

    name: str = Field()
    a: RandInt = Field()
    skill: int | None = Field()
    s: int = Field()
    ap: int = Field()
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
        return f"""{self.name} [A {self.a} BS/WS {self.skill}+ S {self.s} AP {self.ap} D {self.d}]"""


class MeleeWeapon(Weapon):
    ...


class RangedWeapon(Weapon):
    range: int = Field()


class Profile(BaseModel):
    name: str = Field()
    t: int = Field()
    sv: int = Field()
    w: int = Field()
    inv: int | None = Field(default=None)
    ranged_weapons: list[RangedWeapon] | None = Field(default=[])
    melee_weapons: list[MeleeWeapon] | None = Field(default=[])

    def __str__(self):
        inv = f'INV {self.inv}+ ' if self.inv else ''
        return f'{self.name} [T {self.t} Sv {self.sv}+ {inv}W {self.w}]'
