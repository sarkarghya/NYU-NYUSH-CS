#define _XOPEN_SOURCE 700

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define N 5


pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
int val;

void* thread_rand(void* arg) {
    int *tmp = (int*)malloc(sizeof(int));
    *tmp = (*(int*)arg);
    pthread_mutex_lock(&mutex);
    val += (*tmp)*2;
    printf("tid = %ld -- val %d\n", (long)pthread_self(), val);
    pthread_mutex_unlock(&mutex);
    pthread_exit((void*)0);
}


int main(int argc, char** argv) {
    
    int i;
    int *pt_i;
    pthread_t tid[N];
    
    val = 0;
    
    for (i = 0; i < N; i++){
        pt_i = (int*)malloc(sizeof(i));
        *pt_i = i;
        pthread_create((pthread_t*)&tid[i], NULL, thread_rand, (void*)pt_i);
    }
    
    for (i = 0; i < N; i++) {
        printf("tid[%d] = %ld\n", i, (long)tid[i]);
        if(pthread_join(tid[i], NULL) != 0) {
            perror("join");
            exit(1);
        }
    }
    printf("val -- %d\n", val);
    
    return 0;
}
