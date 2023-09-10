#include <list.h>
#include <stdlib.h>
#include <stdio.h>


void init_list(struct list_type *l) {
	l->head = NULL;
	l->tail = NULL;
}
	
	
void insert_head(struct list_type *l, void* element) {
	cell* new_cell = malloc(sizeof(cell));
	new_cell->content = element;
	new_cell->previous = NULL;
	new_cell->next = l->head;
	if (l->head != NULL)
		l->head->previous = new_cell;
	l->head = new_cell;
	if (l->tail == NULL)
			l->tail = l->head;
}


void* extract_head(struct list_type *l) {
    if (l->head == NULL)
		return NULL;

    cell* extracted_cell = l->head;
    void* extracted_element = extracted_cell->content;

    l->head = l->head->next;
    if (l->head != NULL)
        l->head->previous = NULL;

    free(extracted_cell);

    return extracted_element;
}


void* extract_tail(struct list_type *l) {
    if (l->tail == NULL) 
		return NULL;

    cell* extracted_cell = l->tail;
    void* extracted_element = extracted_cell->content;

    l->tail = l->tail->previous;
    if (l->tail != NULL)
        l->tail->next = NULL;

    free(extracted_cell);

    return extracted_element;
}


int list_size(struct list_type *l) {
	/* TODO */
}
	