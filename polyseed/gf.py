from typing import Tuple
from . import PolyseedData, SECRET_BYTES, CHAR_BIT, SECRET_BITS, FEATURE_BITS, DATE_BITS, DATE_MASK, POLYSEED_NUM_WORDS

GF_BITS = 11
GF_SIZE = 1 << GF_BITS
GF_MASK = GF_SIZE - 1
POLY_NUM_CHECK_DIGITS = 1
SHARE_BITS = 10  # bits of the secret per word
DATA_WORDS = POLYSEED_NUM_WORDS - POLY_NUM_CHECK_DIGITS

polyseed_mul2_table = [5, 7, 1, 3, 13, 15, 9, 11]

class GFPoly:
    def __init__(self, coeffs: Tuple[int, ...]):
        self.coeffs = coeffs

    def eval(self) -> int:
        """Horner's method at x = 2"""
        result = self.coeffs[-1]
        for coeff in self.coeffs[-2::-1]:
            result = gf_elem_mul2(result) ^ coeff
        return result

    def encode(self) -> None:
        self.coeffs = (*self.coeffs[:-1], self.eval())

    def check(self) -> bool:
        return self.eval() == 0

def gf_elem_mul2(x: int) -> int:
    if x < 1024:
        return 2 * x
    return polyseed_mul2_table[x % 8] + 16 * ((x - 1024) // 8)

def data_to_poly(data: PolyseedData) -> GFPoly:
    extra_val = (data.features << DATE_BITS) | data.birthday
    extra_bits = FEATURE_BITS + DATE_BITS

    word_bits = 0
    word_val = 0

    secret_idx = 0
    secret_val = data.secret[secret_idx]
    secret_bits = CHAR_BIT
    seed_rem_bits = SECRET_BITS - CHAR_BIT

    coeffs = [0] * POLYSEED_NUM_WORDS

    for i in range(DATA_WORDS):
        while word_bits < SHARE_BITS:
            if secret_bits == 0:
                secret_idx += 1
                secret_bits = min(seed_rem_bits, CHAR_BIT)
                secret_val = data.secret[secret_idx]
                seed_rem_bits -= secret_bits
            chunk_bits = min(secret_bits, SHARE_BITS - word_bits)
            secret_bits -= chunk_bits
            word_bits += chunk_bits
            word_val <<= chunk_bits
            word_val |= (secret_val >> secret_bits) & ((1 << chunk_bits) - 1)
        word_val <<= 1
        extra_bits -= 1
        word_val |= (extra_val >> extra_bits) & 1
        coeffs[POLY_NUM_CHECK_DIGITS + i] = word_val
        word_val = 0
        word_bits = 0

    assert seed_rem_bits == 0
    assert secret_bits == 0
    assert extra_bits == 0

    return GFPoly(tuple(coeffs))

def poly_to_data(poly: GFPoly) -> PolyseedData:

    data = PolyseedData()
    data.birthday = 0
    data.features = 0
    data.secret = bytearray(SECRET_BYTES)
    data.checksum = poly.coeffs[0]

    extra_val = 0
    extra_bits = 0

    word_bits = 0
    word_val = 0

    secret_idx = 0
    secret_bits = 0
    seed_bits = 0

    for i in range(POLY_NUM_CHECK_DIGITS, POLYSEED_NUM_WORDS):
        word_val = poly.coeffs[i]

        extra_val <<= 1
        extra_val |= word_val & 1
        word_val >>= 1
        word_bits = GF_BITS - 1
        extra_bits += 1

        while word_bits > 0:
            if secret_bits == CHAR_BIT:
                secret_idx += 1
                seed_bits += secret_bits
                secret_bits = 0
            chunk_bits = min(word_bits, CHAR_BIT - secret_bits)
            word_bits -= chunk_bits
            chunk_mask = (1 << chunk_bits) - 1
            if chunk_bits < CHAR_BIT:
                data.secret[secret_idx] <<= chunk_bits
            data.secret[secret_idx] |= (word_val >> word_bits) & chunk_mask
            secret_bits += chunk_bits

    seed_bits += secret_bits

    assert word_bits == 0
    assert seed_bits == SECRET_BITS
    assert extra_bits == FEATURE_BITS + DATE_BITS

    data.birthday = extra_val & DATE_MASK
    data.features = extra_val >> DATE_BITS

    return data
