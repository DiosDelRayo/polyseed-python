from passlib.hash import pbkdf2_sha256
from binascii import unhexlify, hexlify
from passlib.utils.binary import ab64_decode

KDF_NUM_ITERATIONS = 10000

secretHexString = "23152d18e4955b3d4a3b2c0bf6eada5058893800000000000000000000000000";
saltHexString = "504f4c5953454544206b657900ffffff000000001e0000000000000000000000";
secret = unhexlify(secretHexString)
salt = unhexlify(saltHexString)[:16]
print(f'Secret: {hexlify(secret).decode()}');
print(f'Salt:   {hexlify(salt).decode()}');
key = ab64_decode(pbkdf2_sha256.using(rounds=KDF_NUM_ITERATIONS, salt=salt).hash(secret).split('$')[-1].encode())
print(f'Key:    {hexlify(key).decode()}');
