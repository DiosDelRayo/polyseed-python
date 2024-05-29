from binascii import unhexlify, hexlify
import hmac
import hashlib
import os
import struct


def pbkdf2(digestmod, password: 'bytes', salt, count, dk_length) -> 'bytes':
    '''
    PBKDF2, from PKCS #5 v2.0:
        http://tools.ietf.org/html/rfc2898

    For proper usage, see NIST Special Publication 800-132:
        http://csrc.nist.gov/publications/PubsSPs.html

    The arguments for this function are:

        digestmod
            a crypographic hash constructor, such as hashlib.sha256
            which will be used as an argument to the hmac function.
            Note that the performance difference between sha1 and
            sha256 is not very big. New applications should choose
            sha256 or better.

        password
            The arbitrary-length password (passphrase) (bytes)

        salt
            A bunch of random bytes, generated using a cryptographically
            strong random number generator (such as os.urandom()). NIST
            recommend the salt be _at least_ 128bits (16 bytes) long.

        count
            The iteration count. Set this value as large as you can
            tolerate. NIST recommend that the absolute minimum value
            be 1000. However, it should generally be in the range of
            tens of thousands, or however many cause about a half-second
            delay to the user.

        dk_length
            The lenght of the desired key in bytes. This doesn't need
            to be the same size as the hash functions digest size, but
            it makes sense to use a larger digest hash function if your
            key size is large. 

    '''
    def pbkdf2_function(pw, salt, count, i):
        # in the first iteration, the hmac message is the salt
        # concatinated with the block number in the form of \x00\x00\x00\x01
        r = u = hmac.new(pw, salt + struct.pack(">i", i), digestmod).digest()
        for i in range(2, count + 1):
            # in subsequent iterations, the hmac message is the
            # previous hmac digest. The key is always the users password
            # see the hmac specification for notes on padding and stretching
            u = hmac.new(pw, u, digestmod).digest()
            # this is the exclusive or of the two byte-strings
            r = bytes(i ^ j for i, j in zip(r, u))
        return r
    dk, h_length = b'', digestmod().digest_size
    # we generate as many blocks as are required to
    # concatinate to the desired key size:
    blocks = (dk_length // h_length) + (1 if dk_length % h_length else 0)
    for i in range(1, blocks + 1):
        dk += pbkdf2_function(password, salt, count, i)
    # The length of the key wil be dk_length to the nearest
    # hash block size, i.e. larger than or equal to it. We
    # slice it to the desired length befor returning it.
    return dk[:dk_length]


if __name__ == '__main__':
    KDF_NUM_ITERATIONS = 10000

    secretHexString = "23152d18e4955b3d4a3b2c0bf6eada5058893800000000000000000000000000";
    saltHexString = "504f4c5953454544206b657900ffffff000000001e0000000000000000000000";
    secret = unhexlify(secretHexString)
    salt = unhexlify(saltHexString)[:16]
    print(f'Secret: {hexlify(secret).decode()}');
    print(f'Salt:   {hexlify(salt).decode()}');
    # print(ab64_decode(pbkdf2_sha256.using(rounds=KDF_NUM_ITERATIONS, salt=salt).hash(secret).split('$')[-1]))
    key = pbkdf2(hashlib.sha256, secret, salt, KDF_NUM_ITERATIONS, 32)
    print(f'Key:    {hexlify(key).decode()}');
