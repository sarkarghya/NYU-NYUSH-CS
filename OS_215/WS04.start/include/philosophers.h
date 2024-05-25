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

#define SHM_NAME "/sim_shm:0"
#define FNAME "dp_output.txt"
#define IS_SHARED 1         //Default share setting for unnamed semaphores

#ifndef NPHIL
#define NPHIL 4             //Number of philosophers
#endif

#ifndef MEALS
#define MEALS 5             //Number of meals
#endif

int fd;                 //Descriptor of the output file

typedef struct dining_philosophers_shared_memory{
    sem_t mx;
    int chopsticks[NPHIL];
    int meal_counter;
} dp_shm;

//Functions you have to write
void initialize_shared_memory();
void cleanup();
void pick_up_chopsticks(int rank);
void put_down_chopsticks(int rank);

//Functions provided for you
void philosopher(int rank);
void pick_up_left_chopstick(int rank);
void pick_up_right_chopstick(int rank);
void eat_meal(int rank);
void put_down_left_chopstick(int rank);
void put_down_right_chopstick(int rank);
void print_chopsticks_status();
void log_chopsticks_status();

