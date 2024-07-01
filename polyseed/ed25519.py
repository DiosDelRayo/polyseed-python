from binascii import unhexlify
from nacl.bindings import crypto_core_ed25519_scalar_reduce as ed25519_scalar_reduce
from nacl.bindings import  crypto_scalarmult_ed25519_base_noclamp as scalarmult_B
from nacl.exceptions import RuntimeError as NaclRuntimeError


def scalar_reduce(v: bytes) -> bytes:
    return ed25519_scalar_reduce(v + (64 - len(v)) * b"\0")

def public_from_secret(hk: bytes) -> bytes:
    try:
        return scalarmult_B(hk)
    except NaclRuntimeError:
        raise ValueError("Invalid secret key")
