default: polyseed-generate polyseed-recover pbkdf2_sha256

pbkdf2_sha256: pbkdf2.o execpbkdf2sha256.o
	gcc -g $^ -lpolyseed -lutf8proc -lsodium -o $@

polyseed-generate: pbkdf2.o polyseedgen.o
	gcc -g $^ -lpolyseed -lutf8proc -lsodium -o $@

polyseed-recover: pbkdf2.o polyseedrecover.o
	gcc -g $^ -lpolyseed -lutf8proc -lsodium -o $@

pbkdf2.o: pbkdf2.c pbkdf2.h
	gcc -g -c pbkdf2.c -Wall

execpbkdf2sha256.o: execpbkdf2sha256.c
	gcc -g -c execpbkdf2sha256.c -Wall

polyseedrecover.o: polyseedrecover.c
	gcc -g -c polyseedrecover.c -Wall

polyseedgen.o: polyseedgen.c
	gcc -g -c polyseedgen.c -Wall

clean:
	rm *.o pbkdf2_sha256 polyseed-generate polyseed-recover
