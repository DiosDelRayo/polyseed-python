from .constants import (
    GF_SIZE,
    POLYSEED_NUM_WORDS,
    SECRET_SIZE,
    ENCRYPTED_MASK,
    KDF_NUM_ITERATIONS,
    POLYSEED_STR_SIZE
)
from .gf import GFPoly
from .storage import PolyseedData
from .tools import random_secret
from .features import make_features, polyseed_features_supported
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


class Polyseed:

    @staticmethod
    def polyseed_create(features: int) -> PolyseedData:
        seed_features = make_features(features)
        if not polyseed_features_supported(seed_features):
            raise PolyseedFeatureUnsupported()

        poly: GFPoly = GFPoly.from_data(
            PolyseedData(
                birthday_encode(time()),
                seed_features,
                random_secret(SECRET_SIZE),
                0
            )
        )
        # calculate checksum
        poly.encode()
        # MEMZERO_LOC(poly)
        return poly.to_data()

    # TODO: makes this any sense in Python???
    @staticmethod
    def polyseed_free(seed):
        if seed:
            # MEMZERO_PTR(seed, polyseed_data)
            seed = None

    @staticmethod
    def get_birthday(data: PolyseedData) -> int:
        return birthday_decode(data.birthday)

    @staticmethod
    def get_feature(seed: PolyseedData, mask) -> int:
        return get_features(seed.features, mask)

    @staticmethod
    def encode(data: PolyseedData, lang: Language, coin: int) -> str:
        assert 0 <= coin < GF_SIZE

        # encode polynomial with the existing checksum
        poly: GFPoly = GFPoly.from_data(data)
        # apply coin
        poly.set_coin(coin)

        # output words
        out = lang.phrase_encode(poly.coeffs)
        if len(out) >= POLYSEED_STR_SIZE:
            raise PolyseedStringSizeExceededException()

        # compose if needed by the language
        if lang.compose:
            out = normalize('NFC', out)
            if len(out) >= POLYSEED_STR_SIZE:
                raise PolyseedStringSizeExceededException()
        # TODO: MEMZERO_LOC(poly)
        # TODO: MEMZERO_LOC(str_tmp)
        return out

    @staticmethod
    def decode(phrase: str, coin: int):
        assert 0 <= coin < GF_SIZE

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

        # checksum
        #if not poly.check():
        #    raise PolyseedChecksumException()

        # decode polynomial into seed data
        seed = poly.to_data()

        # check features
        if not polyseed_features_supported(seed.features):
            raise PolyseedFeatureUnsupported()
        return seed

    # TODO: code missing! Whatever there happend
    @staticmethod
    def decode_explicit(phrase: str, coin: int, lang: Language):
        assert phrase
        assert 0 <= coin < GF_SIZE
        assert lang

        str_tmp = ''
        words = [0] * POLYSEED_NUM_WORDS
        poly = [0] * 257
        res = 0
        seed = None

        # canonical decomposition
        str_size = normalize('NFD', str_tmp)

        # split into words
        num_words = str_split(str_tmp, words)
        if num_words != POLYSEED_NUM_WORDS:
            res = POLYSEED_ERR_NUM_WORDS

    @staticmethod
    def keygen(seed: PolyseedData, coin: int, key_size: int) -> bytes:
        assert 0 <= coin < GF_SIZE

        # Define salt
        header: bytes = b'POLYSEED key'
        salt = bytearray(header + bytes(32 - len(header)))
        salt[13] = 0xff
        salt[14] = 0xff
        salt[15] = 0xff
        salt.extend(pack('<I', coin))
        salt.extend(pack('<I', seed.birthday))
        salt.extend(pack('<I', seed.features))
        
        # Perform key derivation
        return pbkdf2_sha256(seed.secret, bytes(salt), KDF_NUM_ITERATIONS, key_size)

    @staticmethod
    def crypt(seed: PolyseedData, password: Union[str, bytes]) -> PolyseedData:
        raise Exception('Not implemented yet, kick developers ass')  # TODO: implementation missing

    @staticmethod:
        def is_encrypted(seed: PolyseedData) -> bool:
        raise Exception('Not implemented yet, kick developers ass')  # TODO: implementation missing
