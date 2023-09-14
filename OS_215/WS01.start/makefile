CC=gcc -Wall
BIN=bin
INC=include
LIB=lib
OBJ=obj
SRC=src


all: runstack


# ${OBJ}/stack_array.o: ${INC}/stack.h ${SRC}/stack_array.c
# 	${CC} -c -o ${OBJ}/stack_array.o ${SRC}/stack_array.c -I${INC}

# ${OBJ}/stack_test.o: ${INC}/stack.h ${SRC}/stack_test.c
# 	${CC} -c -o ${OBJ}/stack_test.o ${SRC}/stack_test.c -I${INC}

# ${BIN}/stack_test: ${OBJ}/stack_test.o ${OBJ}/stack_array.o
# 	${CC} -o ${BIN}/stack_test ${OBJ}/stack_test.o ${OBJ}/stack_array.o


# runstack: ${BIN}/stack_test
# 	echo "Testing Stack"
# 	${BIN}/stack_test


## Q3

# ${LIB}/libstack.a: ${OBJ}/stack_list.o ${OBJ}/list_impl.o
# 	ar rcv ${LIB}/libstack.a ${OBJ}/stack_list.o ${OBJ}/list_impl.o
# 	ranlib ${LIB}/libstack.a

# ${OBJ}/stack_list.o: ${INC}/list.h ${INC}/stack.h ${SRC}/stack_list.c
# 	${CC} -c -o ${OBJ}/stack_list.o ${SRC}/stack_list.c -I${INC}

# ${OBJ}/list_impl.o: ${INC}/list.h ${SRC}/list_impl.c
# 	${CC} -c -o ${OBJ}/list_impl.o ${SRC}/list_impl.c -I${INC}

# ${OBJ}/stack_test.o: ${INC}/stack.h ${SRC}/stack_test.c
# 	${CC} -c -o ${OBJ}/stack_test.o ${SRC}/stack_test.c -I${INC}

# ${BIN}/stack_test: ${OBJ}/stack_test.o ${LIB}/libstack.a
# 	${CC} -o ${BIN}/stack_test ${OBJ}/stack_test.o -L${LIB} -lstack


# runlibstack: ${BIN}/stack_test
# 	echo "Testing Lib Stack"
# 	${BIN}/stack_test

runstack: ${BIN}/stack_test
	echo "Testing Stack"
	${BIN}/stack_test

## Q4

${LIB}/libstack.a: ${OBJ}/list_impl.o ${OBJ}/fifo_list.o
	ar rcv ${LIB}/libstack.a ${OBJ}/list_impl.o ${OBJ}/fifo_list.o
	ranlib ${LIB}/libstack.a

${OBJ}/list_impl.o: ${INC}/list.h ${SRC}/list_impl.c
	${CC} -c -o ${OBJ}/list_impl.o ${SRC}/list_impl.c -I${INC}

${OBJ}/fifo_list.o: ${INC}/list.h ${INC}/fifo.h ${SRC}/fifo_list.c
	${CC} -c -o ${OBJ}/fifo_list.o ${SRC}/fifo_list.c -I${INC}

${OBJ}/fifo_test.o: ${INC}/fifo.h ${SRC}/fifo_test.c
	${CC} -c -o ${OBJ}/fifo_test.o ${SRC}/fifo_test.c -I${INC}

${BIN}/fifo_test: ${OBJ}/fifo_test.o ${LIB}/libstack.a
	${CC} -o ${BIN}/fifo_test ${OBJ}/fifo_test.o -L${LIB} -lstack


runlibfifo:  ${BIN}/fifo_test
	echo "Testing Fifo"
	${BIN}/fifo_test



clean:
	rm -f ${OBJ}/* ${BIN}/* ${LIB}/*
