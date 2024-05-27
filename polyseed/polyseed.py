from .constants import (
    GF_SIZE,
    POLYSEED_NUM_WORDS,
    SECRET_SIZE,
    ENCRYPTED_MASK,
    KDF_NUM_ITERATIONS
)
from .gf import GFPoly
from .storage import PolyseedData
from .tools import random_secret
from .exceptions import PolyseedFeatureUnsupported

from time import time


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
    def polyseed_get_birthday(data: PolyseedData) -> int:
        assert data
        return birthday_decode(data['birthday'])

    @staticmethod
    def polyseed_get_feature(seed: PolyseedData, mask):
        assert seed
        return get_features(seed['features'], mask)

    @staticmethod
    def encode(data: PolyseedData, lang, coin: int) -> str:
        assert lang
        assert 0 <= coin < GF_SIZE

        # encode polynomial with the existing checksum
        poly: GFPoly = GFPoly.from_data(data)
        # apply coin
        poly.set_coin(coin)

        str_tmp = ''
        w = 0

        # output words
        for w in range(POLYSEED_NUM_WORDS - 1):
            str_tmp += lang['words'][poly[w]] + lang['separator']

        str_tmp += lang['words'][w]
        str_size = len(str_tmp)
        assert str_size < POLYSEED_STR_SIZE

        # compose if needed by the language
        if lang['compose']:
            out = normalize('NFC', str_tmp)
            assert len(out) < POLYSEED_STR_SIZE
        else:
            out = str_tmp
        return out
        # MEMZERO_LOC(poly)
        # MEMZERO_LOC(str_tmp)
        # return str_size

    @staticmethod
    def decode(phrase: str, coin: int, lang_out):
        assert 0 <= coin < GF_SIZE

        str_tmp = ''
        words = [0] * POLYSEED_NUM_WORDS
        poly = [0] * 257
        res = 0
        seed = None

        # canonical decomposition
        str_tmp = normalize('NFD', phrase)
        str_size = len(str_tmp)

        # split into words
        words = str_tmp.split(' ')
        num_words = len(words)
        if num_words != POLYSEED_NUM_WORDS:
            res = POLYSEED_ERR_NUM_WORDS
            return res

        # decode words into polynomial coefficients
        res = polyseed_phrase_decode(words, poly, lang_out)
        
        if res != POLYSEED_OK:
            return res

        # finalize polynomial
        poly.set_coin(coin)

        # checksum
        if not gf_poly_check(poly):
            return POLYSEED_ERR_CHECKSUM

        # decode polynomial into seed data
        seed = poly.to_data()

        # check features
        if not polyseed_features_supported(seed['features']):
            del seed
            return POLYSEED_ERR_UNSUPPORTED

        return seed

    def polyseed_decode_explicit(phrase, coin: int, lang):
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
