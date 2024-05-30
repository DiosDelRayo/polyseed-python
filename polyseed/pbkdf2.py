from typing import Union
from hmac import new as hmac
from hashlib import sha256
from struct import pack

def pbkdf2_sha256(password: Union[str, bytes], salt: Union[str, bytes], count: int, dk_length: int) -> bytes:
    if type(password) == 'str':
        password = password.encode()
    if type(salt) == 'str':
        salt = salt.encode()

    # stolen from Stefano Palazzo <stefano.palazzo@gmail.com>
    # see: https://github.com/sfstpala/python3-pbkdf2/blob/master/pbkdf2.py
    # used this code in favor of passlib implemetation to keep dependencies down
    def pbkdf2_function(pw: bytes, salt: bytes, count: int, i: int) -> bytes:
        r = u = hmac(pw, salt + pack(">i", i), sha256).digest()
        for i in range(2, count + 1):
            u = hmac(pw, u, sha256).digest()
            r = bytes(i ^ j for i, j in zip(r, u))
        return r
    dk, h_length = b'', 32
    blocks = (dk_length // h_length) + (1 if dk_length % h_length else 0)
    for i in range(1, blocks + 1):
        dk += pbkdf2_function(password, salt, count, i)
    return dk[:dk_length]
