import random


def d6():
    return random.randint(6) + 1


def two_d6():
    return d6() + d6()


def d3():
    roll = d6()
    match roll:
        case 1, 2:
            return 1
        case 3, 4:
            return 2
        case 5, 6:
            return 3
        case _:
            raise ValueError('d6 roll out of bounds')
