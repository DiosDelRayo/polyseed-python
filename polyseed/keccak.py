from Cryptodome.Hash import keccak


def keccak_256(data: bytes) -> keccak.Keccak_Hash:
    """
    Return a hashlib-compatible Keccak 256 object for the given data.
    """
    h = keccak.new(digest_bits=256)
    h.update(data)
    return h
