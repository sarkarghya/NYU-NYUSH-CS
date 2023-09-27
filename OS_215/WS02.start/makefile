CC=gcc -Wall
BIN=bin
INC=include
LIB=lib
OBJ=obj
SRC=src


${BIN}/decoder: ${SRC}/decoder.c ${INC}/decoder.h
	${CC} -o ${BIN}/decoder ${SRC}/decoder.c ${INC}/decoder.h -I${INC}

Q2: ${BIN}/decoder
	@echo "##################################################"
	${BIN}/decoder
	@echo "##################################################"


${LIB}/libstack.a: ${OBJ}/converters.o
	ar rcv ${LIB}/libstack.a ${OBJ}/converters.o
	ranlib ${LIB}/libstack.a

${OBJ}/converters.o: ${INC}/converters.h ${SRC}/converters.c
	${CC} -c -o ${OBJ}/converters.o ${SRC}/converters.c -I${INC}

${OBJ}/multi-converter.o: ${INC}/converters.h ${SRC}/multi-converter.c
	${CC} -c -o ${OBJ}/multi-converter.o ${SRC}/multi-converter.c -I${INC}

${BIN}/multi-converter: ${OBJ}/multi-converter.o ${LIB}/libstack.a
	${CC} -o ${BIN}/multi-converter ${OBJ}/multi-converter.o -L${LIB} -lstack

Q3: ${BIN}/multi-converter
	@echo "##################################################"
	${BIN}/multi-converter EUR "100.0"
	@echo "##################################################"


clean:
	rm -f ${LIB}/* ${OBJ}/* ${BIN}/*
