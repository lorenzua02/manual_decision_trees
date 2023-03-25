from collections import Counter
import numpy as np


def mode(a: np.ndarray | list) -> int:
    count = Counter(a)
    return max(count, key=count.get)
