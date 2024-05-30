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

static const polyseed_lang* get_lang_by_name(const char* name) {
    for (int i = 0; i < polyseed_get_num_langs(); ++i) {
        const polyseed_lang* lang = polyseed_get_lang(i);
        if (0 == strcmp(name, polyseed_get_lang_name_en(lang))) {
            return lang;
        }
        if (0 == strcmp(name, polyseed_get_lang_name(lang))) {
            return lang;
        }
    }
    return NULL;
}

int main(int argc, char* argv[]) {

    if (sodium_init() == -1) {
        printf("sodium_init failed\n");
        return 1;
    }

    polyseed_init();


    const char* password = (argc > 1)?argv[1]:NULL;
    polyseed_status result;
    polyseed_data* seed1;

    //create a new seed
    printf("Generating new seed...\n");
    result = polyseed_create(0, &seed1);
    if (result != POLYSEED_OK) {
        printf("ERROR: %i\n", result);
        return 1;
    }

    //generate a key from the seed
    uint8_t key1[32];
    polyseed_keygen(seed1, POLYSEED_MONERO, sizeof(key1), key1);
    printf("Data:  [");
    for (unsigned i = 0; i < sizeof(key1); ++i) {
	    printf("%i", key1[i] & 0xff);
	    if(i != sizeof(key1) - 1)
		    printf(", ");
    }
    printf("]\n");
    printf("Private key: ");
    for (unsigned i = 0; i < sizeof(key1); ++i)
		printf("%02x", key1[i] & 0xff);
    printf("\n");

    if(password != NULL) {
	    printf("Encrypting with password '%s' ...\n", password);
	    polyseed_crypt(seed1, password);
    }

    //encode into a mnemonic phrase
    polyseed_str phrase;
    polyseed_encode(seed1, get_lang_by_name("English"), POLYSEED_MONERO, phrase);
    printf("Mnemonic: %s\n", phrase);

    polyseed_free(seed1);

    return 0;
}
