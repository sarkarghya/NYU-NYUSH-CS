#define _XOPEN_SOURCE 700

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <fcntl.h>
#include <time.h>
#include <ctype.h>
#include <sched.h>

#define NB_THREADS 4
#define NB_LOOPS 5

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cond = PTHREAD_COND_INITIALIZER;
int countup, first;


void wait_barrier(int n) {
    pthread_mutex_lock(&mutex);
    countup++;
    while (countup < n)
        pthread_cond_wait(&cond, &mutex);
        // While waiting, it releases the mutex (&mutex) 
        // and waits on the condition variable (&cond)
    if (first == 0) {
        first = 1;
        pthread_cond_broadcast(&cond);
    }
    pthread_mutex_unlock(&mutex);
}


void* thread_func(void* arg) {
    printf ("afore barrier\n");
    wait_barrier (NB_THREADS);
    printf ("after barrier\n");
    pthread_exit ( (void*)0);
}


int main(int argc, char** argv) {
    
    int i;
    pthread_t tid[NB_THREADS];
    
    countup = 0;
    first = 0;
    
    for (i = 0; i < NB_THREADS; i++)
        pthread_create((tid+i), 0, thread_func, 0);
    
    for (i = 0; i < NB_THREADS; i++)
        pthread_join(tid[i], NULL);
    
    printf("%ld> END PROG\n", pthread_self());
    
    return EXIT_SUCCESS;
    
}
