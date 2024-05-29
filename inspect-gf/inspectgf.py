





SECRET_KEY = '23152d18e4955b3d4a3b2c0bf6eada5058893800000000000000000000000000'
GF_BITS = 11
POLY_NUM_CHECK_DIGITS = 1
SECRET_BITS = 150
SECRET_BUFFER_SIZE = 32
POLYSEED_NUM_WORDS = 16
DATE_BITS = 10
DATE_MASK = (1 << DATE_BITS) - 1
FEATURE_BITS = 5
FEATURE_MASK = (1 << FEATURE_BITS) - 1
CHAR_BIT = 8



def print_secret(secret):
    print("secret:  " + ''.join(format(x, '02x') for x in secret))






















# phrase: label cart fee spice decorate next holiday stand mom clown cool huge repeat expire giraffe own
coeff = [993, 280, 676, 1676, 456, 1194, 870, 1700, 1142, 352, 382, 885, 1461, 643, 785, 1264]

data_secret = bytearray([0] * SECRET_BUFFER_SIZE)


data_checksum = coeff[0]

extra_val = 0
extra_bits = 0

word_bits = 0
word_val = 0

secret_idx = 0
secret_bits = 0
seed_bits = 0

for i in range(POLY_NUM_CHECK_DIGITS, POLYSEED_NUM_WORDS):
    print("-------------------------------------------------------------------------")
    word_val = coeff[i]

    extra_val <<= 1
    extra_val |= word_val & 1
    word_val >>= 1
    word_bits = GF_BITS - 1
    extra_bits += 1
    print(f"Word: {i:02}, coeff: {coeff[i]}, word_val: {word_val}, extra_val: {extra_val}")
    print(f"          word_bits: {word_bits}, extra_bits: {extra_bits}\n")

    while word_bits > 0:
        print("---------> word_bits:", word_bits)
        if secret_bits == CHAR_BIT:
            print(f"         -> CHAR_BIT == secret_bits: {secret_bits}, seed_bits: {seed_bits}, secret_idx: {secret_idx}")
            secret_idx += 1
            seed_bits += secret_bits
            secret_bits = 0
            print(f"         => secret_bits: {secret_bits}, seed_bits: {seed_bits}, secret_idx: {secret_idx}")

        chunk_bits = min(word_bits, 8 - secret_bits)
        print(f"         -> chunk_bits: {chunk_bits}, word_bits: {word_bits}, secret_bits: {secret_bits}")
        word_bits -= chunk_bits
        print(f"         => word_bits: {word_bits}")
        chunk_mask = (1 << chunk_bits) - 1
        print(f"         => chunkmask: {chunk_mask:08b} ({chunk_mask})")
        if chunk_bits < CHAR_BIT:
            print(f"         -> CHAR_BIT > chunk_bits: {chunk_bits}")
            data_secret[secret_idx] <<= chunk_bits
            print(f"         => data_secret[{secret_idx}]: {data_secret[secret_idx]}")

        print(f"         -> data_secret[{secret_idx}]: {data_secret[secret_idx]}, word_val: {word_val}, word_bits: {word_bits}, chunk_mask: {chunk_mask}")
        data_secret[secret_idx] |= (word_val >> word_bits) & chunk_mask
        print(f"         => data_secret[{secret_idx}]: {data_secret[secret_idx]}, word_val: {word_val}, word_bits: {word_bits}, chunk_mask: {chunk_mask}")
        print(f"         -> secret_bits: {secret_bits}, chunk_bits: {chunk_bits}")
        secret_bits += chunk_bits
        print(f"         => secret_bits: {secret_bits}, chunk_bits: {chunk_bits}")

    print_secret(data_secret)


print(f"          seed_bits: {seed_bits}, secret_bits: {secret_bits}")
seed_bits += secret_bits
print(f"          seed_bits: {seed_bits}, secret_bits: {secret_bits}")

assert word_bits == 0
assert seed_bits == SECRET_BITS
assert extra_bits == FEATURE_BITS + DATE_BITS

data_birthday = extra_val & DATE_MASK
data_features = extra_val >> DATE_BITS
print("=========================================================================")
print_secret(data_secret)
print(f"checksum: {data_checksum}")
print(f"birthday: {data_birthday}")
print(f"features: {data_features:08b}")
if ''.join(format(x, '02x') for x in data_secret) == SECRET_KEY:
    print('Secret correct.')
else:
    print('Secret INCORRECT!')
