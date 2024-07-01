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
from .base58 import encode as b58
from .ed25519 import public_from_secret, scalar_reduce
from .keccak import keccak_256

from binascii import hexlify, unhexlify
from time import time
from unicodedata import normalize
from struct import pack
from typing import Union, Optional, Callable


NET_MAIN = "main"
NET_STAGE = "stage"
NET_TEST = "test"

MASTERADDR_NETBYTES = {
    NET_MAIN: 18,
    NET_TEST: 24,
    NET_STAGE: 53
}


class Polyseed:

    def __init__(self, seed: Optional[PolyseedData] = None, poly: Optional[GFPoly] = None, coin: int = POLYSEED_MONERO):
        self.seed: PolyseedData = seed
        self.poly: GFPoly = poly
        self.coin: int = coin
        self._secret_spend_key_bytes: Optional[bytes] = None
        self._secret_view_key_bytes: Optional[bytes] = None
        self._secret_spend_key: Optional[str] = None
        self._secret_view_key: Optional[str] = None
        self._public_spend_key: Optional[str] = None
        self._public_viewkey: Optional[str] = None
        self._public_address: Dict[str, Optional[str]] = {
            NET_MAIN: None,
            NET_TEST: None,
            NET_STAGE: None
        }

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

    # TODO: makes this any sense in Python???
    @staticmethod
    def polyseed_free(seed):
        if seed:
            # MEMZERO_PTR(seed, polyseed_data)
            seed = None

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
        # TODO: MEMZERO_LOC(poly)
        # TODO: MEMZERO_LOC(str_tmp)
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
        salt[16] = self.coin  # TODO: doublecheck and test
        salt[20] = self.seed.birthday  # TODO: doublecheck and test
        salt[24] = self.seed.features  # TODO: doublecheck and test
        # salt.extend(pack('<I', self.coin))
        # salt.extend(pack('<I', self.seed.birthday))
        # salt.extend(pack('<I', self.seed.features))
        print(f'salt:        {salt.hex()}')
        
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

    @property
    def secret_spend_key(self) -> str:
        if not self._secret_spend_key:
            self._secret_spend_key = hexlify(self.secret_spend_key_bytes).decode()
        return self._secret_spend_key

    @property
    def secret_spend_key_bytes(self) -> bytes:
        if not self._secret_spend_key_bytes:
            self._secret_spend_key_bytes = self.keygen()  # TODO: 2024-06-30, check if that is correct
        return self._secret_spend_key_bytes

    @property
    def secret_view_key(self) -> str:
        if not self._secret_view_key:
            self._secret_view_key = hexlify(self.secret_view_key_bytes).decode()
        return self._secret_view_key

    @property
    def secret_view_key_bytes(self) -> bytes:
        if not self._secret_view_key_bytes:
            self._secret_view_key_bytes = scalar_reduce(keccak_256(self.secret_spend_key_bytes).digest())
        return self._secret_view_key_bytes

    @property
    def public_spend_key(self):
        if not self._public_spend_key:
            self._public_spend_key = hexlify(public_from_secret(self.secret_spend_key_bytes)).decode()
        return self._public_spend_key

    @property
    def public_view_key(self):
        if not self._public_viewkey:
            self._public_viewkey = hexlify(public_from_secret(self.secret_view_key_bytes)).decode()
        return self._public_viewkey

    def public_address(self, network: str = NET_MAIN):
        if network not in MASTERADDR_NETBYTES.keys():
            raise Exception(f'Unkown network: {network}')
        net = MASTERADDR_NETBYTES.get(network)
        if not self._public_address[network]:
            self._public_address[network] = b58(f'{net:x}{self.public_spend_key}{self.public_view_key}'.encode() + keccak_256(unhexlify(f'{net:x}{self.public_spend_key}{self.public_view_key}')).hexdigest()[:8].encode())
        return self._public_address[network]

    @property
    def public_address_main(self) -> str:
        return self.public_address(NET_MAIN)

    @property
    def public_address_test(self) -> str:
        return self.public_address(NET_TEST)

    @property
    def public_address_stage(self) -> str:
        return self.public_address(NET_STAGE)

    def wallet_data(self, network: str = NET_MAIN) -> str:
        return f"""
polyseed:         {self.encode()}
address:          {self.public_address(network)}
secret spend key: {self.secret_spend_key}
secret view key:  {self.secret_view_key}
height:           {self.get_birthday()}
        """.strip()
