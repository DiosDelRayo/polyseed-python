from .constants import (
    FEATURE_BITS,
    FEATURE_MASK,
    INTERNAL_FEATURES,
    USER_FEATURES,
    USER_FEATURES_MASK,
    ENCRYPTED_MASK
)
from .lang import Language
from .storage import PolyseedData
from .gf import GFPoly
from .polyseed import Polyseed
from .pbkdf2 import pbkdf2_sha256

from typing import Optional

def generate(password: Optional[str]) -> Polyseed:
    polyseed = Polyseed.create(0)  # TODO: wht is sane or do I need to expose to arguments?
    if password:
        polyseed.crypt(password)
    return polyseed

def recover(phrase: str, password: Optional[str]) -> Polyseed:
    polyseed = Polyseed.decode(phrase)
    if polyseed.is_encrypted() and password:
        polyseed.crypt(password)
    return polyseed

def show_polyseed(polyseed: Polyseed) -> None:
    key = polyseed.keygen()
    encrypted = 'yes' if polyseed.is_encrypted() else 'no'
    phrase = polyseed.encode()
    data = [int(b) for b in polyseed.seed.secret]
    out = f'''
coeff:       {polyseed.poly.coeffs}
Data:        {data}
private key: {key.hex()}
phrase:      {phrase}
encrypted:   {encrypted}
secret:      {polyseed.seed.secret.hex()}
    '''.strip()
    print(out)
