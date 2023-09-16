
First Name: Arghya

Last Name: Sarkar

NYU ID: abs9425

=======================================================================================
Files submitted:

src:
	fifo_list.c: Question 4
	fifo_test.c: Question 4
	list_impl.c: Question 2, Question 3, Question 4
	stack_array.c: Question 1
	stack_list.c: Question 3
	stack_test.c: Question 1, Question2, Question 3

include:
	fifo.h: Question 4
	list.h: Question 2, Question 3, Question 4
	stack.h: Question 1, Question 2, Question 3 and Question 3


=======================================================================================
Compilation rules in the Makefile:

# A few examples below
# make libstack: 	generates and registers the array-based stack library (lib/libstack.a) (Q2)
# make stacksize: 	recompiles the stack with a new value for STACK_SIZE as a compilation directive and runs the stack test (Q3)
# make newlibstack:	recompiles the stack, implemented as a double-linked list, then integrates it in an update of libstack.a (Q5)
# make Q5:		uses newlibstack to recompile the binary executable (bin/stack_test), then runs it (Q5)
# make libfifo: 	compiles a dynamic queue implemented as a double-linked list, then integrates it in a library (lib/libfifo.a) (Q6)

Question 1:
	No compilation rules required.

Question 2:
	No compilation rules required.

Question 3:
	The first block creates a library file (libstack.a) by combining two object files (stack_list.o and list_impl.o) using the ar command. Then, it updates the library using ranlib.
	The subsequent blocks compile specific source files (stack_list.c and list_impl.c) into corresponding object files (stack_list.o and list_impl.o) using the CC compiler.
	Lastly, there's a rule for building the stack_test executable. It depends on stack_test.o and the libstack.a library. The linker (CC) is used to create the executable.
	The runlibstack target runs the stack_test program.

Question 4:
	The first block creates a library file "libstack.a" using the object files "list_impl.o" and "fifo_list.o". It uses the 'ar' and 'ranlib' commands.
	The second block says that the file "list_impl.o" in the OBJ directory depends on "list.h" in INC and "list_impl.c" in SRC. It uses the C compiler (CC) to do this.
	The third block does something similar for "fifo_list.o" and has additional dependencies.
	The fourth block is for "fifo_test.o" depends on ${INC}/fifo.h and ${SRC}/fifo_test.c. It compiles fifo_test.c into an object file.
	The fifth block creates an executable file "fifo_test" using "fifo_test.o" and "libstack.a". It links the library using the '-L' flag.
	The last block, "runlibfifo", is a custom target that runs the "fifo_test" program.

=======================================================================================
Comments:

Question 4:
	I was reminded of the fact that `make clean` is necessary. Without make clean there are conflicts with other parts of the code.

=======================================================================================
Textual answers: 

Question 5:
	To determine the size of the list in O(1) time complexity, one should make the following changes.

	1. Open the file `list.h`.
	2. Inside the `struct list_type`, add a new integer variable (let's call it `size`) to keep track of the number of elements in the list. Initialize it to 0.

	You would modify the struct:

	struct list_type {
		cell* head;
		cell* tail;
		int size; // Add this line
	};

	3. When inserting a new element into the list (in the `insert_head` function), increment the `size` variable by 1.

	Modification in the `insert_head` function:

	void insert_head(struct list_type *l, void* element) {
		// ... existing code ...
		l->size++; // Add this line
	}

	4. When extracting an element from the list (in the `extract_head` and `extract_tail` functions), decrement the `size` variable by 1.

	Modification in the `extract_head` function (do the same for `extract_tail`):

	void* extract_head(struct list_type *l) {
		// ... existing code ...
		l->size--; // Add this line
		return extracted_element;
	}

	5. Finally, implement the `list_size` function to return the value of the `size` variable.

	int list_size(struct list_type *l) {
		return l->size;
	}

	With these changes, We'll be able to determine the size of the list in constant time (O(1)).


	