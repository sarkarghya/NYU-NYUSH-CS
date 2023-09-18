/**
 * Definition of a doubly linked list
 **/


#define _XOPEN_SOURCE 700


typedef struct cell_type {
	struct cell_type *previous;
	struct cell_type *next;
	void *content;
} cell;


struct list_type {
	cell* head;
	cell* tail;
};


/* Initialization of the list */
void init_list(struct list_type *l);

/* Insertion of a new element.
 The new element is added to the head of the list. */
void insert_head(struct list_type *l, void* element);

/* Extraction of the element at the head of the list.
 Returns (also deletes) that element.  */
void* extract_head(struct list_type *l);

/* Extraction of the element at the tail of the list.
 Returns (also deletes) that element.  */
void* extract_tail(struct list_type *l);

/* Returns the number of elements in the list */
int list_size(struct list_type *l);
