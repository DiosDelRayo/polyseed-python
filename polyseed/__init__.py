from .constants import (
    FEATURE_BITS,
    FEATURE_MASK,
    INTERNAL_FEATURES,
    USER_FEATURES,
    USER_FEATURES_MASK,
    ENCRYPTED_MASK,
    POLYSEED_MONERO
)
from .exceptions import PolyseedMissingPasswordException, PolyseedLanguageNotFoundException
from .lang import Language
from .storage import PolyseedData
from .gf import GFPoly
from .polyseed import Polyseed
from .pbkdf2 import pbkdf2_sha256

from typing import Optional


def seed_phrase_from_bytes(random: bytes, timestamp: Optional[int] = None, coin: int = POLYSEED_MONERO, language: Optional[str] = None) -> Polyseed:  # TODO: 2024-07-02, language selection not working!
    polyseed = Polyseed.create(timestamp, 0, coin, lambda size: random[:size])
    if language:
        try:
            return polyseed.encode(Language.get_lang_by_code(language))
        except PolyseedLanguageNotFoundException:
            pass
    return polyseed.encode()

def generate(timestamp: Optional[int] = None, password: Optional[str] = None, coin: int = POLYSEED_MONERO) -> Polyseed:
    polyseed = Polyseed.create(timestamp, 0, coin)
    key = polyseed.keygen()
    print(f'private key: {key.hex()}')
    if password and password != '':
        polyseed.crypt(password)
    return polyseed

def recover(phrase: str, password: Optional[str]) -> Polyseed:
    polyseed = Polyseed.decode(phrase)
    if polyseed.is_encrypted():
        if password:
            polyseed.crypt(password)
        else:
            raise PolyseedMissingPasswordException('Password needed but not provided! Abort!')
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
