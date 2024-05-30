#include <polyseed.h>

#include <sodium/core.h>
#include <sodium/utils.h>
#include <sodium/randombytes.h>
#include <utf8proc.h>

#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "pbkdf2.h"

typedef uint_fast16_t gf_elem;


/* Seed data structure for serialization */
typedef struct polyseed_data {
    unsigned birthday;
    unsigned features;
    /* padded with zeroes for future compatibility with longer seeds */
    uint8_t secret[32];
    gf_elem checksum;
} polyseed_data;


#define MIN(a,b) ((a)>(b)?(b):(a))

static size_t utf8_nfc(const char* str, polyseed_str norm) {
    utf8proc_uint8_t* s = utf8proc_NFC((const utf8proc_uint8_t*)str);
    size_t len = strlen((const char*)s);
    size_t size = MIN(len, (size_t)POLYSEED_STR_SIZE - 1);
    memcpy(norm, s, size);
    norm[size] = '\0';
    sodium_memzero(s, len);
    free(s);
    return size;
}

static size_t utf8_nfkd(const char* str, polyseed_str norm) {
    utf8proc_uint8_t* s = utf8proc_NFKD((const utf8proc_uint8_t*)str);
    size_t len = strlen((const char*)s);
    size_t size = MIN(len, (size_t)POLYSEED_STR_SIZE - 1);
    memcpy(norm, s, size);
    norm[size] = '\0';
    sodium_memzero(s, len);
    free(s);
    return size;
}

static void polyseed_init() {
    polyseed_dependency pd = {
        .randbytes = &randombytes_buf,
        .pbkdf2_sha256 = &crypto_pbkdf2_sha256,
        .memzero = &sodium_memzero,
        .u8_nfc = &utf8_nfc,
        .u8_nfkd = &utf8_nfkd,
        .time = NULL,
        .alloc = NULL,
        .free = NULL,
    };
    polyseed_inject(&pd);
}

#define FEATURE_FOO 1
#define FEATURE_BAR 2
#define FEATURE_QUX 4

int main(int argc, char* argv[]) {

    if (sodium_init() == -1) {
        printf("sodium_init failed\n");
        return 1;
    }

    polyseed_init();

    // polyseed_enable_features(FEATURE_FOO | FEATURE_BAR);

    if(argc < 2) {
	    printf("You need to specify the seed phrase!\n");
	    return 2;
    }
    const char* password = (argc > 2)?argv[2]:NULL;
    polyseed_status result;

    //decode a seed from the phrase
    printf("Decoding mnemonic phrase...\n");

    polyseed_data* seed;
    const polyseed_lang* lang;
    result = polyseed_decode(argv[1], POLYSEED_MONERO, &lang, &seed);
    if (result != POLYSEED_OK) {
        printf("ERROR: %i\n", result);
        return 1;
    }
    //printf("Detected language: %s\n", polyseed_get_lang_name_en(lang));

    printf("encrypted:   %s\n", polyseed_is_encrypted(seed) ? "yes" : "no");

    printf("Data:        [");
    for (unsigned i = 0; i < sizeof(seed->secret); ++i) {
	    printf("%i", seed->secret[i] & 0xff);
	    if(i != sizeof(seed->secret) - 1)
		    printf(", ");
    }
    printf("]\n");

    if (polyseed_get_feature(seed, FEATURE_FOO)) {
        printf("Seed has the 'Foo' feature\n");
    }

    //decrypt
    if (polyseed_is_encrypted(seed)) {
	    if(password == NULL) {
		    printf("Password needed but not provided! Abort!\n");
		    return 2;
	    }
	    printf("Decrypting with password '%s' ...\n", password);
        polyseed_crypt(seed, password);
    }

    //recover the key
    uint8_t key2[32];
    polyseed_keygen(seed, POLYSEED_MONERO, sizeof(key2), key2);
    printf("private key: ");
    for (unsigned i = 0; i < sizeof(key2); ++i)
	    printf("%02x", key2[i] & 0xff);
    printf("\n");

    polyseed_free(seed);

    return 0;
}
