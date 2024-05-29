#include <stdint.h>
#include <assert.h>
#include <string.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

#define SECRET_KEY "23152d18e4955b3d4a3b2c0bf6eada5058893800000000000000000000000000"
#define GF_BITS 11
#define POLY_NUM_CHECK_DIGITS 1
#define SECRET_BITS 150
#define SECRET_BUFFER_SIZE 32
#define POLYSEED_NUM_WORDS 16
#define DATE_BITS 10
#define DATE_MASK ((1u << DATE_BITS) - 1)
#define FEATURE_BITS 5
#define FEATURE_MASK ((1u<<FEATURE_BITS)-1)

#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))

void print_secret(uint8_t secret[], size_t size) {
	printf("secret:  ");
	for(unsigned i = 0; i < size; i++)
		printf("%02x", secret[i]);
	printf("\n");
}

int compare_secret(const uint8_t secret[], size_t size) {
	if (size != strlen(SECRET_KEY) / 2) {
		return 0;
	}

	for (unsigned i = 0; i < size; i++) {
		char byte[3] = {SECRET_KEY[i * 2], SECRET_KEY[i * 2 + 1], '\0'};
		uint8_t key_byte = (uint8_t)strtoul(byte, NULL, 16);
		if (secret[i] != key_byte) {
			return 0;
		}
	}

	return 1;
}

int main(int argc, char* argv[]) {
	// phrase: label cart fee spice decorate next holiday stand mom clown cool huge repeat expire giraffe own
	uint_fast16_t coeff[POLYSEED_NUM_WORDS] = {993, 280, 676, 1676, 456, 1194, 870, 1700, 1142, 352, 382, 885, 1461, 643, 785, 1264};

	uint8_t data_secret[SECRET_BUFFER_SIZE];
	memset(data_secret, 0, sizeof(data_secret));

	uint_fast16_t data_checksum = coeff[0];

	unsigned extra_val = 0;
	unsigned extra_bits = 0;

	unsigned word_bits = 0;
	unsigned word_val = 0;

	unsigned secret_idx = 0;
	unsigned secret_bits = 0;
	unsigned seed_bits = 0;

	for (int i = POLY_NUM_CHECK_DIGITS; i < POLYSEED_NUM_WORDS; ++i) {
		printf("-------------------------------------------------------------------------\n");
		word_val = coeff[i];

		extra_val <<= 1;
		extra_val |= word_val & 1;
		word_val >>= 1;
		word_bits = GF_BITS - 1;
		extra_bits++;
		printf("Word: %02i, coeff: %lu, word_val: %u, extra_val: %u\n", i, coeff[i], word_val, extra_val);
		printf("          word_bits: %u, extra_bits: %u\n\n", word_bits, extra_bits);

		while (word_bits > 0) {
			printf("---------> word_bits: %u\n", word_bits); 
			if (secret_bits == CHAR_BIT) {
				printf("         -> CHAR_BIT == secret_bits: %u, seed_bits: %u, secret_idx: %u\n", secret_bits, seed_bits, secret_idx); 
				secret_idx++;
				seed_bits += secret_bits;
				secret_bits = 0;
				printf("         => secret_bits: %u, seed_bits: %u, secret_idx: %u\n", secret_bits, seed_bits, secret_idx); 
			}
			unsigned chunk_bits = MIN(word_bits, CHAR_BIT - secret_bits);
			printf("         -> chunk_bits: %u, word_bits: %u, secret_bits: %u\n", chunk_bits, word_bits, secret_bits); 
			word_bits -= chunk_bits;
			printf("         => word_bits: %u\n", word_bits); 
			unsigned chunk_mask = ((1u << chunk_bits) - 1);
			printf("         => chunkmask: %08b (%u)\n", chunk_mask, chunk_mask); 
			if (chunk_bits < CHAR_BIT) {
				printf("         -> CHAR_BIT > chunk_bits: %u\n", chunk_bits); 
				data_secret[secret_idx] <<= chunk_bits;
				printf("         => data_secret[%u]: %u\n", secret_idx, data_secret[secret_idx]); 
			}
			printf("         -> data_secret[%u]: %u, word_val: %u, word_bits: %u, chunk_mask: %u\n", secret_idx, data_secret[secret_idx], word_val, word_bits, chunk_mask); 
			data_secret[secret_idx] |= (word_val >> word_bits) & chunk_mask;
			printf("         => data_secret[%u]: %u, word_val: %u, word_bits: %u, chunk_mask: %u\n", secret_idx, data_secret[secret_idx], word_val, word_bits, chunk_mask); 
			printf("         -> secret_bits: %u, chunk_bits: %u\n", secret_bits, chunk_bits); 
			secret_bits += chunk_bits;
			printf("         => secret_bits: %u, chunk_bits: %u\n", secret_bits, chunk_bits); 
		}
		print_secret(data_secret, sizeof(data_secret));
	}

	printf("          seed_bits: %u, secret_bits: %u\n", seed_bits, secret_bits);
	seed_bits += secret_bits;
	printf("          seed_bits: %u, secret_bits: %u\n", seed_bits, secret_bits);

	assert(word_bits == 0);
	assert(seed_bits == SECRET_BITS);
	assert(extra_bits == FEATURE_BITS + DATE_BITS);

	unsigned data_birthday = extra_val & DATE_MASK;
	unsigned data_features = extra_val >> DATE_BITS;
	printf("=========================================================================\n");
	print_secret(data_secret, sizeof(data_secret));
	printf("checksum: %lu\n", data_checksum);
	printf("birthday:  %u\n", data_birthday);
	printf("features:  %08b\n", data_features);
	if(compare_secret(data_secret, sizeof(data_secret)))
		printf("Secret correct.\n");
	else
		printf("Secret INCORRECT!\n");
}
