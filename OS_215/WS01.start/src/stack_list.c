#include <stack.h>
#include <list.h>
#include <stdlib.h>

/* Stack structure */
typedef struct Stack {
    struct list_type *list;
} Stack;

Stack stack;

/* Initialization of the stack 
    Allocating memory */
int init_stack() {
    stack.list = malloc(sizeof(struct list_type));
    init_list(stack.list);
    return 0;
}

/* Insertion: adds an element to the top of the stack */
int push(void* element){
    insert_head(stack.list, element);
    return 0;
}

/* Extraction: an element at the top of the stack is removed and its value is returned */
void* pop(){
    return extract_head(stack.list);
}

/* Returns the number of elements */
int size(){
    return list_size(stack.list);
}
