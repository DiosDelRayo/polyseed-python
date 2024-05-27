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

def generate(password: Optional[str]) -> Polyseed:
    raise Exception('Not implemented yet, kick developers ass')  # TODO: implementation missing

def recover(phrase: str, password: Optional[str]) -> Polyseed:
    raise Exception('Not implemented yet, kick developers ass')  # TODO: implementation missing
