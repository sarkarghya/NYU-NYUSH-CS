/**********************************************/
/*     (c) L. Apvrille, Telecom ParisTech     */
/* Extended version by O. Marin, NYU Shanghai */
/**********************************************/


#include <os-scheduling.h>
#include <string.h>


char * states[] = {"upcoming  ", "ready     ", "running   ", "suspended ", "terminated"};


char * getStateString(int state) {
    return states[state];
}

/* Returns the number of tasks that still have to be run, */
/* that is, all tasks which still have computations to perform */
int hasTasksToSchedule(task tasks[], int nbOfTasks) {
    int total = 0;
    int i;
    
    for(i=0; i<nbOfTasks; i++) {
        if (tasks[i].state != TERMINATED) {
            total ++;
        }
    }
    return total;
}


void printTasks(task tasks[], int nbOfTasks) {
    int i;
    
    for(i=0; i<nbOfTasks; i++) {
        printf("Task: %s \t arrivalDate:%d    \t state:%s \t computations:%d/%d\n",
               tasks[i].name, tasks[i].arrivalDate, getStateString(tasks[i].state),
               tasks[i].executionTime, tasks[i].computationTime);
    }
}


void printQueues(task tasks[], sched_data* schedData) {
    int i, j, taskIndex = 0;
    printf("Nb of queues %d\n", schedData->nbOfQueues);
    for (i = 0; i < schedData->nbOfQueues; i++) {
        j = 0;
        printf("Q%d => ", i);
        while (j < MAX_NB_OF_TASKS) {
            taskIndex = schedData->queues[i][j];
            if (taskIndex == -1) {
                j = MAX_NB_OF_TASKS;
            } else {
                printf("%s ", tasks[taskIndex].name);
                j++;
            }
        }
        printf("\n");
    }
}

void printFinalStatistics(task tasks[], int nbOfTasks, int totalTime) {
    int i, turnaroundTime;
    int totalWaitingTime = 0;
    double penaltyRate = 0;
    int averageWaitingTime = 0;
    double throughput = 0;
    printf("STATISTICS ########\n");
    for(i=0; i<nbOfTasks; i++) {
        turnaroundTime = 0;
        totalWaitingTime += 0;
        penaltyRate = 0;
        printf("Task: %s \t turnaround time:%d \t penalty rate:%2.2f\n",
               tasks[i].name, turnaroundTime, penaltyRate);
    }
    printf("Average waiting time = %2.2f\n", averageWaitingTime);
    printf("Throughput = %2.2f\n\n", throughput);
}


/* Returns the index of the elected task  */
/*         -1 if no task could be elected */
int scheduler(char* policy, task tasks[], int nbOfTasks, sched_data *schedData, int currentTime) {
    if (strcmp(policy, "FCFS") == 0)
        return FCFS(tasks, nbOfTasks, schedData, currentTime);
    if (strcmp(policy, "SJF") == 0)
        return SJF(tasks, nbOfTasks, schedData, currentTime);
    if (strcmp(policy, "SRTF") == 0)
        return SRTF(tasks, nbOfTasks, schedData, currentTime);
    if (strcmp(policy, "RR") == 0)
        return RR(tasks, nbOfTasks, schedData, currentTime);
    if (strcmp(policy, "MFQ") == 0)
        return MFQ(tasks, nbOfTasks, schedData, currentTime);
    if (strcmp(policy, "IORR") == 0)
        return IORR(tasks, nbOfTasks, schedData, currentTime);
    return -1;
}


int main(int argc, char *argv[]){
    char line [MAX_LINE_SIZE]; /* or other suitable maximum line size */
    task tasks[MAX_NB_OF_TASKS];
    sched_data *schedData = (sched_data*)malloc(sizeof(sched_data));
    int nbOfTasks = 0;
    int time = 0;
    int taskIndex;
    
    /**** Read the task file, and store into a struct ****/
    FILE *file = fopen (argv[1], "r" );
    if (file == NULL) {
        perror(argv[1]);
        return -1;
    }
    
    printf("Scheduling policy is %s\n", argv[2]);
    
    /* Adjust policy parameters */
    if (strcmp(argv[2], "RR") == 0)
        schedData->quantum = atoi(argv[3]);
    
    /* Read the file line by line */
    printf("Loading file of tasks\n");
    while (fgets(line, sizeof(line), file) != NULL ) {
        sscanf(line, "%s %u %u\n", tasks[nbOfTasks].name, &(tasks[nbOfTasks].computationTime), &(tasks[nbOfTasks].arrivalDate));
        tasks[nbOfTasks].state = UPCOMING;
        tasks[nbOfTasks].executionTime = 0;
        nbOfTasks ++;
    }
    fclose(file);
    printf("%d tasks loaded\n\n", nbOfTasks);
    
    /**** Schedule the set of tasks ****/
    printf("Scheduling the set of tasks\n");
    
    
    while(hasTasksToSchedule(tasks, nbOfTasks) > 0) {
        printTasks(tasks, nbOfTasks);
        taskIndex = scheduler(argv[2], tasks, nbOfTasks, schedData, time);
        if (taskIndex >= 0) {
            printf("\nTime %d: %s\n", time,  tasks[taskIndex].name);
        } else {
            printf("\nTime %d: no task to schedule\n", time);
        }
        time ++;
//  For debugging purposes only
//        getchar();
    }
    
    
    /**** That's all folks ****/
    printTasks(tasks, nbOfTasks);
    time --;
    printf("\n\nAll done after %d units of time\n", time);
    printf("\n######## %s ", argv[2]);
    printFinalStatistics(tasks, nbOfTasks, time);
    return 0;
}


