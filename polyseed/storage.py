import struct

SECRET_BUFFER_SIZE = 32
SECRET_BITS = 150
SECRET_SIZE = (SECRET_BITS + 7) // 8  # 19
CLEAR_BITS = SECRET_SIZE * 8 - SECRET_BITS  # 2
CLEAR_MASK = ~((1 << CLEAR_BITS) - 1)
TOTAL_BITS = 256 * 24  # GF_BITS * POLYSEED_NUM_WORDS

# Seed data structure for serialization
class PolyseedData:
    def __init__(self, birthday=0, features=0, secret=b'\x00' * SECRET_BUFFER_SIZE, checksum=0):
        self.birthday = birthday
        self.features = features
        self.secret = secret[:SECRET_SIZE]
        self.checksum = checksum & 0x7F  # GF_MASK

STORAGE_HEADER = b'POLYSEED'
HEADER_SIZE = len(STORAGE_HEADER)
EXTRA_BYTE = 0xFF
STORAGE_FOOTER = 0x7000

def polyseed_data_store(data, storage):
    storage[:] = STORAGE_HEADER
    pos = HEADER_SIZE
    storage[pos:pos+2] = struct.pack('<H', (data.features << 10) | data.birthday)
    pos += 2
    storage[pos:pos+SECRET_SIZE] = data.secret
    pos += SECRET_SIZE
    storage[pos] = EXTRA_BYTE
    pos += 1
    storage[pos:pos+2] = struct.pack('<H', STORAGE_FOOTER | data.checksum)

def polyseed_data_load(storage):
    if storage[:HEADER_SIZE] != STORAGE_HEADER:
        return 'POLYSEED_ERR_FORMAT', None

    pos = HEADER_SIZE
    v1 = struct.unpack('<H', storage[pos:pos+2])[0]
    birthday = v1 & 0x3FF
    features = v1 >> 10
    if features > 0x1F:
        return 'POLYSEED_ERR_FORMAT', None

    pos += 2
    secret = storage[pos:pos+SECRET_SIZE]
    if secret[-1] & ~CLEAR_MASK:
        return 'POLYSEED_ERR_FORMAT', None

    pos += SECRET_SIZE
    if storage[pos] != EXTRA_BYTE:
        return 'POLYSEED_ERR_FORMAT', None

    pos += 1
    v2 = struct.unpack('<H', storage[pos:pos+2])[0]
    checksum = v2 & 0x7F
    footer = v2 & ~0x7F
    if footer != STORAGE_FOOTER:
        return 'POLYSEED_ERR_FORMAT', None

    data = PolyseedData(birthday, features, secret, checksum)
    return 'POLYSEED_OK', data
