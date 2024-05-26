import struct
from typing import List

SECRET_BUFFER_SIZE = 32
SECRET_BITS = 150
SECRET_SIZE = (SECRET_BITS + 7) // 8  # 19
CLEAR_BITS = SECRET_SIZE * 8 - SECRET_BITS  # 2
CLEAR_MASK = ~((1 << CLEAR_BITS) - 1)
TOTAL_BITS = 256 * 24  # GF_BITS * POLYSEED_NUM_WORDS

STORAGE_HEADER = b'POLYSEED'
HEADER_SIZE = len(STORAGE_HEADER)
EXTRA_BYTE = 0xFF
STORAGE_FOOTER = 0x7000


class PolyseedDataFormatException(Exception):
    pass


# Seed data structure for serialization
class PolyseedData:
    def __init__(self, birthday: int = 0, features: int = 0, secret: bytes = b'\x00' * SECRET_BUFFER_SIZE, checksum: int = 0):
        self.birthday = birthday
        self.features = features
        self.secret = secret[:SECRET_SIZE]
        self.checksum = checksum & 0x7F  # GF_MASK

    def polyseed_data_store(self) -> List[int]:
        storage = STORAGE_HEADER.copy()
        pos = HEADER_SIZE
        storage[pos:pos+2] = struct.pack('<H', (self.features << 10) | self.birthday)
        pos += 2
        storage[pos:pos+SECRET_SIZE] = self.secret
        pos += SECRET_SIZE
        storage.append(EXTRA_BYTE)
        pos += 1
        storage[pos:pos+2] = struct.pack('<H', STORAGE_FOOTER | self.checksum)
        return storage

    @classmethod
    def polyseed_data_load(cls, storage: List[int]) -> PolyseedData:
        if storage[:HEADER_SIZE] != STORAGE_HEADER:
            raise PolyseedDataFormatException()

        pos = HEADER_SIZE
        v1 = struct.unpack('<H', storage[pos:pos+2])[0]
        birthday = v1 & 0x3FF
        features = v1 >> 10
        if features > 0x1F:
            raise PolyseedDataFormatException()

        pos += 2
        secret = storage[pos:pos+SECRET_SIZE]
        if secret[-1] & ~CLEAR_MASK:
            raise PolyseedDataFormatException()

        pos += SECRET_SIZE
        if storage[pos] != EXTRA_BYTE:
            raise PolyseedDataFormatException()

        pos += 1
        v2 = struct.unpack('<H', storage[pos:pos+2])[0]
        checksum = v2 & 0x7F
        footer = v2 & ~0x7F
        if footer != STORAGE_FOOTER:
            raise PolyseedDataFormatException()

        return PolyseedData(birthday, features, secret, checksum)
