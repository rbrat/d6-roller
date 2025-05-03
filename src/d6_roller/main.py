from .schemas.profile import Profile, RangedWeapon
from .engine import simulate


def main():
    intercessor = Profile(
        name='intercessor',
        t=4,
        sv=3,
        w=2,
    )
    bolter = RangedWeapon(
        name='bolt rifle',
        a='2',  # type: ignore
        skill=3,
        s=4,
        ap=-1,
        d='1',  # type: ignore
        range=24
    )
    simulate(bolter, intercessor)
