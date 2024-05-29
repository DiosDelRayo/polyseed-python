default: pbkdf2-hmac-sha256

pbkdf2-hmac-sha256: pbkdf2.o
	gcc -g $^ -lpolyseed -lutf8proc -lsodium -o $@


pbkdf2.o: pbkdf2.c pbkdf2.h
	gcc -g -c pbkdf2.c -Wall

clean:
	rm *.o pbkdf2-hmac-sha256
