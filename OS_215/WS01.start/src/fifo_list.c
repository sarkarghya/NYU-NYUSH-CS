#include <fifo.h>
#include <list.h>
#include <stdlib.h>

/* Define FIFO structure */
typedef struct afifo{
    struct list_type *list;
} fifo;

/* Create an instance of FIFO */
fifo f;

/* Initialize the queue */
int init_queue() {
    f.list = malloc(sizeof(struct list_type));
    init_list(f.list);
    return 0;
}

/* Insert a new element at the head of the queue */
int queue(void* element) {
    insert_head(f.list, element);
    return 0;
}

/* Dequeue and return the element at the tail of the queue */
void* dequeue() {
    return extract_tail(f.list);
}

/* Get the number of elements in the queue */
int size() {
    return list_size(f.list);
}
