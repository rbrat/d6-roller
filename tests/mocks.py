from src.d6_roller.schemas.profile import Profile, MeleeWeapon, RangedWeapon

profile_intercessor = Profile(
    name='intercessor',
    t=4,
    sv=3,
    w=2,
)

profile_terminator = Profile(
    name='terminator',
    t=5,
    sv=2,
    w=3,
    inv=4,
)

profile_landraider = Profile(
    name='Land Raider',
    t=12,
    sv=2,
    w=16
)

weapon_ccw = MeleeWeapon(
    name='close combat weapon',
    a='3',  # type: ignore
    skill=3,
    s=4,
    ap=0,
    d='1',  # type: ignore
)

weapon_bolter = RangedWeapon(
    name='bolt rifle',
    a='2',  # type: ignore
    skill=3,
    s=4,
    ap=-1,
    d='1',  # type: ignore
    range=24,
)

weapon_mcpw = MeleeWeapon(
    name='Master-crafted power weapon',
    a='6',  # type: ignore
    skill=2,
    s=6,
    ap=-2,
    d='2',  # type: ignore
)

weapon_pyreblaster = RangedWeapon(
    name='Pyreblaster',
    a='D6',  # type: ignore
    skill=None,
    s=5,
    ap=-1,
    d='1',  # type: ignore
    range=12,
)

weapon_multimelta = RangedWeapon(
    name='Multi-melta',
    a='2',  # type: ignore
    skill=4,
    s=9,
    ap=-4,
    d='D6',  # type: ignore
    range=18,
)

weapon_shoota = RangedWeapon(
    name='Shoota',
    a='2',  # type: ignore
    skill=5,
    s=4,
    ap=0,
    d='1',  # type: ignore
    range=18,
)

weapon_shoota_6 = RangedWeapon(
    name='6-shoota',
    a='2',  # type: ignore
    skill=6,
    s=4,
    ap=0,
    d='1',  # type: ignore
    range=18,
)
