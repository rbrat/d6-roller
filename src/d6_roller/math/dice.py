import numpy as np


def build_dice(sides: int = 6) -> np.array:
    return np.array([i for i in range(1, sides + 1)])


d6 = build_dice()
d3 = build_dice(3)
