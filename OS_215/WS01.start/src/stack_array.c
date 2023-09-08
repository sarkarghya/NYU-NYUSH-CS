#include <stack.h>
#include <stdlib.h>

/* Stack structure */
typedef struct astack{
	void* contents[STACK_SIZE];
	int top;
} stack;


stack s;

/* Initialization of the stack */
int init_stack() {
	s.top = 0;
	return s.top;
}


/* Insert an element */
int push(void* element) {
	if (s.top == STACK_SIZE)
		return -1;
	else {
		s.contents[s.top++] = element;
		return s.top;
	}
}


/* Extract an element */
void* pop() {
	void* result = NULL;
	if (s.top != 0) {
		--s.top;
		result = s.contents[s.top];
	}
	return result;
}


/* Compute the size of the stack  */
int size() {
	return s.top;
}
