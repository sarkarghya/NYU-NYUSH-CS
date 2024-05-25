CFLAGS=-Iinclude -Wall
LIBRARIES=-lrt -lpthread

## SIMULATION SETTINGS ##
# Change the integer values below to set:
# 	the nb of philosophers
NB_PHILS=-DNPHIL=4
# 	the nb of meals per philosopher
NB_MEALS=-DMEALS=5
#########################

#compiles and runs your solution
all: build run

#compiles two examples
#1. bin/noconc forces philosophers to eat one at a time
#2. bin/bad does something pretty uncool too
demos: clean src/philosophers-bad.c src/philosophers-no-concurrency.c src/dp_simulator.c
	mkdir obj
	gcc $(CFLAGS) -c -o obj/dp_simulator.o src/dp_simulator.c
	gcc $(CFLAGS) -c -o obj/philosophers-bad.o src/philosophers-bad.c
	gcc $(CFLAGS) -c -o obj/philosophers-nc.o src/philosophers-no-concurrency.c
	mkdir bin
	gcc $(CFLAGS) -o bin/bad obj/dp_simulator.o obj/philosophers-bad.o $(LIBRARIES)
	gcc $(CFLAGS) -o bin/noconc obj/dp_simulator.o obj/philosophers-nc.o $(LIBRARIES)
	bin/bad

#compiles your solution
build: clean src/philosophers.c src/dp_simulator.c
	mkdir obj
	gcc $(CFLAGS) -c -o obj/dp_simulator.o src/dp_simulator.c $(NB_PHILS) $(NB_MEALS)
	gcc $(CFLAGS) -c -o obj/philosophers.o src/philosophers.c $(NB_PHILS) $(NB_MEALS)
	mkdir bin
	gcc $(CFLAGS) -o bin/dp_simulator obj/dp_simulator.o obj/philosophers.o $(LIBRARIES)

#runs your solution
run:
	bin/dp_simulator

#removes all the temporary files
clean:
	rm -rf bin obj dp-output.txt
