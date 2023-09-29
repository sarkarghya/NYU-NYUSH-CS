#define _XOPEN_SOURCE 700

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

#define MAX_LINE_SIZE 512
#define MAX_NB_OF_TASKS 32
#define MAX_TASK_NAME_SIZE 32
#define MAX_NB_OF_QUEUES 8

#define UPCOMING 0
#define READY 1
#define RUNNING 2
#define SLEEPING 3
#define TERMINATED 4


typedef struct task {
    /* Initial elements */
    char name[MAX_TASK_NAME_SIZE]; //task name
    unsigned int computationTime; //task duration
    unsigned int arrivalDate; //date of insertion in the system
    /* Used by scheduler */
    unsigned int state;
    unsigned int executionTime; //nb of cycles on processor
    unsigned int cyclesInQuantum;
    unsigned int completionDate;
} task;

typedef struct sched_data {
    int quantum;
    int nbOfQueues;
    int queues[MAX_NB_OF_QUEUES][MAX_NB_OF_TASKS];
} sched_data;

void printTasks(task tasks[], int nbOfTasks);

void printQueues(task tasks[], sched_data* schedData);

int FCFS(task tasks[], int nbOfTasks, sched_data* schedData, int currentTime);

int SJF(task tasks[], int nbOfTasks, sched_data* schedData, int currentTime);

int SRTF(task tasks[], int nbOfTasks, sched_data* schedData, int currentTime);

int RR(task tasks[], int nbOfTasks, sched_data* schedData, int currentTime);

int MFQ(task tasks[], int nbOfTasks, sched_data* schedData, int currentTime);

int IORR(task tasks[], int nbOfTasks, sched_data* schedData, int currentTime);