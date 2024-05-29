#include <string.h>
#include <stdio.h>
#include <stdint.h>

#include <sodium/crypto_auth_hmacsha256.h>
#include <sodium/utils.h>

#define KDF_NUM_ITERATIONS 10000

static inline void store32_be(uint8_t dst[4], uint32_t w) {
	dst[3] = (uint8_t) w; w >>= 8;
	dst[2] = (uint8_t) w; w >>= 8;
	dst[1] = (uint8_t) w; w >>= 8;
	dst[0] = (uint8_t) w;
}

void crypto_pbkdf2_sha256(
		const uint8_t* passwd, size_t passwdlen,
		const uint8_t* salt, size_t saltlen,
		uint64_t c,
		uint8_t* buf, size_t dkLen) {
	crypto_auth_hmacsha256_state Phctx, PShctx, hctx;
	size_t                       i;
	uint8_t                      ivec[4];
	uint8_t                      U[32];
	uint8_t                      T[32];
	uint64_t                     j;
	int                          k;
	size_t                       clen;

	crypto_auth_hmacsha256_init(&Phctx, passwd, passwdlen);


	PShctx = Phctx;

	crypto_auth_hmacsha256_update(&PShctx, salt, saltlen);


	for (i = 0; i * 32 < dkLen; i++) {
		store32_be(ivec, (uint32_t)(i + 1));
		hctx = PShctx;
		crypto_auth_hmacsha256_update(&hctx, ivec, 4);
		crypto_auth_hmacsha256_final(&hctx, U);

		memcpy(T, U, 32);
		for (j = 2; j <= c; j++) {
			hctx = Phctx;
			crypto_auth_hmacsha256_update(&hctx, U, 32);
			crypto_auth_hmacsha256_final(&hctx, U);

			for (k = 0; k < 32; k++) {
				T[k] ^= U[k];
			}
		}

		clen = dkLen - i * 32;
		if (clen > 32) {
			clen = 32;
		}
		memcpy(&buf[i * 32], T, clen);
	}
	sodium_memzero((void*)&Phctx, sizeof Phctx);
	sodium_memzero((void*)&PShctx, sizeof PShctx);
}

// Function to convert hex string to byte array
void hexStringToBytes(const char* hexString, uint8_t* bytes, size_t length) {
	size_t i, j;
	for (i = 0, j = 0; i < length; i++, j += 2) {
		sscanf(hexString + j, "%2hhX", &bytes[i]);
	}
}

int main(int argc, char* argv[]) {
	uint8_t secret[32];
	uint8_t salt[16];

	const char* keyHexString = "23152d18e4955b3d4a3b2c0bf6eada5058893800000000000000000000000000";
	const char* saltHexString = "504f4c5953454544206b657900ffffff000000001e0000000000000000000000";

	hexStringToBytes(keyHexString, secret, 32);
	hexStringToBytes(saltHexString, salt, 16);

	printf("Secret: ");
	for (size_t i = 0; i < 32; i++) {
		printf("%02X", secret[i]);
	}
	printf("\n");

	printf("Salt:   ");
	for (size_t i = 0; i < 16; i++) {
		printf("%02X", salt[i]);
	}
	printf("\n");
	uint8_t buf[32];
	uint64_t iter = KDF_NUM_ITERATIONS;
	crypto_pbkdf2_sha256(secret, sizeof(secret), salt, sizeof(salt), iter, buf, sizeof(buf));
	printf("Key:    ");
	for (size_t i = 0; i < sizeof(buf); i++) {
		printf("%02X", buf[i]);
	}
	printf("\n");
}
