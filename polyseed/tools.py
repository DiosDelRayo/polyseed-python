from .constants import CLEAR_MASK
from typing import List
from random import randint

def random_secret(size: int) -> List[int]:
    out = [randint(0, 255) for _ in range(size)]
    out[size - 1] &= CLEAR_MASK
    return out
