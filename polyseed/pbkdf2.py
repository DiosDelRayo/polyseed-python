from typing import Union
from passlib.hash import pbkdf2_sha256 as passlib_pbkdf2_sha256
from binascii import unhexlify, hexlify
from passlib.utils.binary import ab64_decode

def pbkdf2_sha256(passwd: Union[str, bytes], salt: Union[str, bytes], c: int, dkLen: int) -> bytes:
    if type(passwd) == 'str':
        passwd = passwd.encode()
    if type(salt) == 'str':
        password = passwd.encode()
    return ab64_decode(passlib_pbkdf2_sha256.using(rounds=c, salt=salt).hash(passwd).split('$')[-1].encode())
