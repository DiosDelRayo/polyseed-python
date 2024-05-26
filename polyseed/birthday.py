EPOCH = 1635768000
TIME_STEP = 2629746

DATE_BITS = 10
DATE_MASK = ((1 << DATE_BITS) - 1)

def birthday_encode(time: int) -> int:
    """
    Encode a Unix timestamp into a birthday representation.
    """
    if time == -1 or time < EPOCH:
        return 0

    return int((time - EPOCH) / TIME_STEP) & DATE_MASK

def birthday_decode(birthday: int) -> int:
    """
    Decode a birthday representation into a Unix timestamp.
    """
    return EPOCH + birthday * TIME_STEP
