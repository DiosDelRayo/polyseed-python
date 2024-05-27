from typing import Union
from hashlib import sha256
from hmac import new as hmac
from struct import pack

def store32_be(i: int) -> bytes:
    return pack(">I", i)

def crypto_pbkdf2_sha256(passwd: Union[str, bytes], salt: Union[str, bytes], c: int, dkLen: int) -> bytes:
    if type(passwd) == 'str':
        passwd = passwd.encode()
    if type(salt) == 'str':
        password = passwd.encode()
    Phctx = sha256(passwd)
    PShctx = hmac(passwd, salt, sha256)
    
    out: bytes = b''
    for i in range(0, (dkLen + 31) // 32):
        ivec = store32_be(i + 1)
        hctx = hmac(PShctx.digest(), ivec, sha256)
        U = hctx.digest()
        
        T = U
        for j in range(2, c + 1):
            hctx = hmac(Phctx.digest(), U, sha256)
            U = hctx.digest()
            T = bytes(x ^ y for x, y in zip(T, U))
        
        clen = min(32, dkLen - i * 32)
        out += T[:clen]
    
    Phctx = PShctx = None
    return out
