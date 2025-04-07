from pydantic import BaseModel, Field


class Weapon(BaseModel):
    name: str = Field()
    a: int = Field()
    skill: int = Field()
    s: int = Field()
    ap: int = Field()
    d: int = Field()

    def __str__(self):
        return f"""{self.name} [A {self.a} BS/WS {self.skill}+ S {self.s} AP {self.ap} D {self.d}]"""


class MeleeWeapon(Weapon):
    pass


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
        inv = f'INV {self.inv}+' if self.inv else ''
        return f'{self.name} [T {self.t} Sv {self.sv}+ W {self.w} {inv}]'
