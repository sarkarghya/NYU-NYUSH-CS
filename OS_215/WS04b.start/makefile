CFLAGS=-Iinclude -Wall
LIBRARIES=-lrt -lpthread

## SIMULATION SETTINGS ##
# Change the integer values below to set:
# 	the nb of consumers
NB_CONS=3
# 	the nb of producers
NB_PROD=4
#########################

#compiles and runs your solution
all: build run

#compiles your solution
build: clean src/prodcons.c src/pc_simulator.c
	mkdir obj
	gcc $(CFLAGS) -c -o obj/pc_simulator.o src/pc_simulator.c 
	gcc $(CFLAGS) -c -o obj/prodcons.o src/prodcons.c
	mkdir bin
	gcc $(CFLAGS) -o bin/pc_simulator obj/pc_simulator.o obj/prodcons.o $(LIBRARIES)

#runs your solution
run:
	bin/pc_simulator $(NB_PROD) $(NB_CONS)

#removes all the temporary files
clean:
	rm -rf bin obj

