from .constants import CLEAR_MASK
from secrets import randbelow

def random_secret(size: int) -> list[int]:
    out = [randbelow(255) for _ in range(size)]
    out[size - 1] &= CLEAR_MASK
    return out
