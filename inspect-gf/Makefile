default: compare

inspect-gf: inspectgf.o
	gcc -g $^ -lpolyseed -lutf8proc -lsodium -o $@

inspectgf.o: inspectgf.c
	gcc -g -c inspectgf.c -Wall

clean:
	rm *.o inspect-gf c.txt python.txt

c.txt: inspect-gf
	./inspect-gf > c.txt

python.txt: inspectgf.py
	python inspectgf.py > python.txt

compare: c.txt python.txt
	diff c.txt python.txt

compare-output: c.txt python.txt
	vimdiff c.txt python.txt

compare-src: inspectgf.c inspectgf.py
	vimdiff inspectgf.c inspectgf.py
