from .constants import (
    GF_SIZE,
    POLYSEED_NUM_WORDS,
    SECRET_SIZE,
    ENCRYPTED_MASK,
    KDF_NUM_ITERATIONS,
    POLYSEED_STR_SIZE,
    POLYSEED_MONERO,
    POLYSEED_AEON,
    POLYSEED_WOWNERO,
    CLEAR_MASK
)
from .gf import GFPoly
from .storage import PolyseedData
from .tools import random_secret
from .features import make_features, polyseed_features_supported, is_encrypted
from .birthday import birthday_encode, birthday_decode
from .exceptions import (
    PolyseedFeatureUnsupported,
    PolyseedStringSizeExceededException,
    PolyseedWordCountMissmatchException,
    PolyseedChecksumException
)
from .lang import Language
from .pbkdf2 import pbkdf2_sha256

from time import time
from unicodedata import normalize
from struct import pack
from typing import Union, Optional, Callable


class Polyseed:

    def __init__(self, seed: Optional[PolyseedData] = None, poly: Optional[GFPoly] = None, coin: int = POLYSEED_MONERO):
        self.seed: PolyseedData = seed
        self.poly: GFPoly = poly
        self.coin: int = coin

    @staticmethod
    def create(timestamp: Optional[int] = None, features: int = 0, coin: int = POLYSEED_MONERO, random: Callable[[int], bytes] = random_secret) -> 'Polyseed':
        seed_features = make_features(features)
        if not polyseed_features_supported(seed_features):
            raise PolyseedFeatureUnsupported()

        secret_bytes = bytearray(random(SECRET_SIZE))
        secret_bytes[-1] &= CLEAR_MASK
        seed: PolyseedData = PolyseedData(
            birthday_encode(timestamp or time()),
            seed_features,
            bytes(secret_bytes),
            0
        )
        poly: GFPoly = GFPoly.from_data(seed)
        # calculate checksum
        poly.encode()
        # MEMZERO_LOC(poly)
        return Polyseed(poly.to_data(), poly, coin)

    def get_birthday(self) -> int:
        if not self.seed:
            raise Exception('Polyseed has acctually no seed')
        return birthday_decode(self.seed.birthday)

    def get_feature(self, mask:int) -> int:
        if not self.seed:
            raise Exception('Polyseed has acctually no seed')
        return get_features(self.seed.features, mask)

    def encode(self, lang: Optional[Language] = None) -> str:
        if not self.seed:
            raise Exception('Polyseed has acctually no seed')
        if not lang:
            if Language.get_lang_count() < 1:
                raise Exception('No wordlists found')
            lang = Language.get_lang(0)
        if self.coin < 0 or self.coin >= GF_SIZE:
            raise Exception('No known coin')

        # encode polynomial with the existing checksum
        if not self.poly:
            self.poly = GFPoly.from_data(self.seed)
        # apply coin
        self.poly.set_coin(self.coin)

        # output words
        out = lang.phrase_encode(self.poly.coeffs)
        if len(out) >= POLYSEED_STR_SIZE:
            raise PolyseedStringSizeExceededException()

        # compose if needed by the language
        if lang.compose:
            out = normalize('NFC', out)
            if len(out) >= POLYSEED_STR_SIZE:
                raise PolyseedStringSizeExceededException()
        return out

    @staticmethod
    def decode(phrase: str, coin: int = POLYSEED_MONERO) -> 'Polyseed':
        if coin < 0 or coin >= GF_SIZE:
            raise Exception('No known coin')

        # canonical decomposition
        phrase = normalize('NFD', phrase)

        # split into words
        words = phrase.split(' ')
        if len(words) != POLYSEED_NUM_WORDS:
            raise PolyseedWordCountMissmatchException()

        # decode words into polynomial coefficients
        poly: GFPoly = GFPoly(Language.phrase_decode(words)[0])
        
        # finalize polynomial
        poly.set_coin(coin)

        #poly.encode()
        # checksum
        if not poly.check():
            raise PolyseedChecksumException()

        # decode polynomial into seed data
        seed = poly.to_data()

        # check features
        if not polyseed_features_supported(seed.features):
            raise PolyseedFeatureUnsupported()
        return Polyseed(seed, poly, coin)

    @staticmethod
    def decode_explicit(phrase: str, lang: Language, coin: int = POLYSEED_MONERO) -> 'Polyseed':
        if self.coin < 0 or self.coin >= GF_SIZE:
            raise Exception('No known coin')

        # canonical decomposition
        phrase = normalize('NFD', phrase)

        # split into words
        words = phrase.split(' ')
        if len(words) != POLYSEED_NUM_WORDS:
            raise PolyseedWordCountMissmatchException()

        # decode words into polynomial coefficients
        poly: GFPoly = GFPoly(Language.phrase_decode_explicit(words))
        
        # finalize polynomial
        poly.set_coin(coin)

        # checksum
        if not poly.check():
            raise PolyseedChecksumException()

        # decode polynomial into seed data
        seed = poly.to_data()

        # check features
        if not polyseed_features_supported(seed.features):
            raise PolyseedFeatureUnsupported()
        return Polyseed(seed, poly, coin)

    def keygen(self, key_size: int = 32) -> bytes:
        if not self.seed:
            raise Exception('Polyseed has acctually no seed')
        if self.coin < 0 or self.coin >= GF_SIZE:
            raise Exception('No known coin')

        # Define salt
        header: bytes = b'POLYSEED key'
        salt = bytearray(header + bytes(32 - len(header)))
        salt[13] = 0xff
        salt[14] = 0xff
        salt[15] = 0xff
        salt[16] = self.coin
        salt[20] = self.seed.birthday
        salt[24] = self.seed.features
        
        # Perform key derivation
        return pbkdf2_sha256(self.seed.secret, bytes(salt), KDF_NUM_ITERATIONS, key_size)

    def crypt(self, password: Union[str, bytes]) -> None:
        if not self.seed:
            raise Exception('Polyseed has acctually no seed')
        password: bytes = normalize('NFD', password).encode() if type(password) == str else password
        if len(password) >= POLYSEED_STR_SIZE:
            raise PolyseedStringSizeExceededException('password too long')
        polyseed_mask = b'POLYSEED mask'
        salt: bytearray = bytearray(polyseed_mask + b'\0' * (16 - len(polyseed_mask)))
        salt[14] = 0xff;
        salt[15] = 0xff;
        mask = pbkdf2_sha256(password, bytes(salt)[:16], KDF_NUM_ITERATIONS, 32)
        secret = bytearray(self.seed.secret)
        for i in range(0, SECRET_SIZE):
            secret[i] ^= mask[i]
        secret[SECRET_SIZE - 1] &= CLEAR_MASK
        self.seed.secret = bytes(secret)
        self.seed.set_encrypted()
        self.poly = GFPoly.from_data(self.seed)
        self.poly.encode()
        self.seed = self.poly.to_data()

    def is_encrypted(self) -> bool:
        if not self.seed:
            raise Exception('Polyseed has acctually no seed')
        return is_encrypted(self.seed.features)
