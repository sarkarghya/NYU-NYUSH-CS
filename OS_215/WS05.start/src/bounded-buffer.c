#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <ctype.h>
#include <pthread.h>

#define MAX_CAP 10
#define NC 6
#define NP 6
#define NVAL 35

int buffer[MAX_CAP]; 
int count;
int production_count, consumption_count;
int potential_production, potential_consumption;

// int producers_waiting = 0;
// int consumers_waiting = 0;

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cond_empty = PTHREAD_COND_INITIALIZER;
pthread_cond_t cond_full = PTHREAD_COND_INITIALIZER;


void* producer(void *argv){
    while (1) {
        pthread_mutex_lock(&mutex);
        potential_production++;
        if (potential_production > NVAL) {
            pthread_mutex_unlock(&mutex);
            break;
        }
        while (count == MAX_CAP) {
            // producers_waiting++;
            pthread_cond_wait(&cond_empty, &mutex); 
            // producers_waiting--;
        }
        int item = rand() % 100 + 1; 
        buffer[count] = item;
        count++;
        production_count++;
        // printf("%d Consumers waiting\n", consumers_waiting); 
        printf("Producer produced %d items, %d\n", production_count, item);
        pthread_cond_signal(&cond_full);
        pthread_mutex_unlock(&mutex);
    }
    pthread_exit((void*)0);
}


void* consumer(void *argv){
    while (1) {
        pthread_mutex_lock(&mutex);
        potential_consumption++;
        if (potential_consumption > NVAL) {
            pthread_mutex_unlock(&mutex);
            break;
        }
        while (count == 0) {
            // consumers_waiting++;
            pthread_cond_wait(&cond_full, &mutex);
            // consumers_waiting--;
        }
        int item = buffer[count-1];
        count--;
        consumption_count++;
        // printf("%d Producers waiting\n", producers_waiting);
        printf("Consumer consumed %d items, %d\n", consumption_count, item); 
        pthread_cond_signal(&cond_empty);
        pthread_mutex_unlock(&mutex);
    }
    pthread_exit((void*)0);
}


int main (int argc, char ** argv) {

    int i;
    count = 0;

    production_count = 0;
    consumption_count = 0;

    potential_production = 0;
    potential_consumption = 0;

    printf("MT> %d producers\n", NP);
    printf("MT> %d consumers\n", NC);

    pthread_t tid_p[NP];
    pthread_t tid_c[NC];

    for (i = 0; i < NP; i++)
        pthread_create(&tid_p[i], NULL, producer, NULL);

    for (i = 0; i < NC; i++)
        pthread_create(&tid_c[i], NULL, consumer, NULL);

    for (i = 0; i < NP; i++) 
        pthread_join(tid_p[i], NULL);
    
    for (i = 0; i < NC; i++)
        pthread_join(tid_c[i], NULL);

    return EXIT_SUCCESS;
}
