from collections import defaultdict
import numpy as np


def mode(a: np.ndarray | list) -> int:
    counter = defaultdict(int)
    for value in a:
        counter[value] += 1
    ordered = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    return ordered[0][0]
