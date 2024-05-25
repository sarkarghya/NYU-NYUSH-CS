CFLAGS =-Iinclude -Wall -lpthread

all: build run

build: clean build_multi-upper build_multi-upper-ftd build_bounded-buffer

build_multi-upper: 
	gcc $(CFLAGS) -c -o obj/multi-upper.o src/multi-upper.c
	gcc $(CFLAGS) -o bin/multi-upper obj/multi-upper.o

build_multi-upper-ftd: 
	gcc $(CFLAGS) -c -o obj/multi-upper-ftd.o src/multi-upper-ftd.c
	gcc $(CFLAGS) -o bin/multi-upper-ftd obj/multi-upper-ftd.o

build_bounded-buffer: 
	gcc $(CFLAGS) -c -o obj/bounded-buffer.o src/bounded-buffer.c
	gcc $(CFLAGS) -o bin/bounded-buffer obj/bounded-buffer.o

run: run_Q1 run_Q2 run_Q3

run_Q1:
	bin/multi-upper text/rt1.txt text/rt2.txt text/rt3.txt text/rt4.txt

run_Q2:
	bin/multi-upper-ftd text/rt1.txt text/rt2.txt text/rt3.txt text/rt4.txt text/rt5.txt text/rt6.txt text/rt7.txt text/rt8.txt

run_Q3:
	bin/bounded-buffer

clean:
	rm -rf bin/* obj/* opf/* text/*.UPPER.txt