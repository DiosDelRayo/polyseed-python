#include "pbkdf2.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int is_hex_string(const char *input) {
    // Check if the input consists only of hexadecimal characters (0-9, a-f, A-F)
    for (const char *ch = input; *ch != '\0'; ch++) {
        if (!((*ch >= '0' && *ch <= '9') || (*ch >= 'a' && *ch <= 'f') || (*ch >= 'A' && *ch <= 'F'))) {
            return 0;
        }
    }
    return 1;
}

void handle_input(const char *input, uint8_t **data, size_t *len) {
    if (is_hex_string(input)) {
        // Convert hexadecimal string to binary data
        *len = strlen(input) / 2;
        *data = malloc(*len);
        for (size_t i = 0; i < *len; i++) {
            sscanf(input + 2*i, "%2hhx", &(*data)[i]);
        }
    } else {
        // Treat input as a string
        *len = strlen(input);
        *data = (uint8_t *)input;
    }
}

int main(int argc, char *argv[]) {
    if (argc != 5) {
        printf("Usage: %s <password> <salt> <iterations> <data>\n", argv[0]);
        return 1;
    }

    const char *passwd = argv[1];
    const char *salt = argv[2];
    uint64_t c = strtol(argv[3], NULL, 10);

    uint8_t buf[atoi(argv[4])]; // Adjust the buffer size as per your requirements
    size_t bufLen = sizeof(buf);

    // Convert password and salt to bytes (assuming ASCII encoding for simplicity)
    const size_t passwdlen = strlen(passwd);
    const size_t saltlen = strlen(salt);

    crypto_pbkdf2_sha256((const uint8_t*)passwd, passwdlen, (const uint8_t*)salt, saltlen, c, buf, bufLen);

    bufLen = sizeof(buf);
    // Output the result bytes
    printf("Derived key:\n");
    for (size_t i = 0; i < bufLen; i++) {
        printf("%02x", buf[i]);
    }
    printf("\n");

    return 0;
}

