/**
 * Definition of a stack
 **/

#define _XOPEN_SOURCE 700

/* Capacity of the stack */
#ifndef STACK_SIZE
#define STACK_SIZE 12
#endif


/* Initialization of the stack */
int init_stack();

/* Insertion: adds an element to the top of the stack */
int push(void* element);

/* Extraction: the element at the top of the stack is removed and its value is returned */
void* pop();

/* Returns the number of elements in the stack */
int size();
