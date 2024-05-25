#define _XOPEN_SOURCE 700

#include <errno.h>
#include <fcntl.h>
#include <math.h>
#include <semaphore.h>
#include <signal.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/wait.h>
#include <sys/stat.h>

#define PCSHM_NAME "/pcshm:0"

#define IS_SHARED 1         //Default share setting for unnamed semaphores
#define BUFSZ 4
#define MAX_ITEMS 16

typedef struct prodcons_shared_memory{
    int i_cons;
    int i_prod;
    int buffer[BUFSZ];
} pc_shm;



void initialize_extra_shared_memory();

void insert_value(int rank, pc_shm *my_shm);

void extract_value(int rank, pc_shm *my_shm);

void cleanup_extra();
