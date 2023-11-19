#define _XOPEN_SOURCE 700

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define N 5

void* thread_control(void* arg) {
    int *tmp = (int*)malloc(sizeof(int));
    *tmp = (*(int*)arg)*2; /** use memcp if arg references a more complex type/structure **/
    printf("tid = %ld -- val %d\n", (long)pthread_self(), *tmp);
    pthread_exit((void*)(size_t)*tmp);
}


int main(int argc, char** argv) {
    
    int i, j;
    int *pt_i;
    int return_value;
    pthread_t tid[N];
    
    for (i = 0; i < N; i++){
        pt_i = (int*)malloc(sizeof(int));
        *pt_i = i;
        pthread_create((pthread_t*)&tid[i], NULL, thread_control, (void*)pt_i);
    }
    
    for (j = 0; j < N; j++) {
        printf("MT> tid[%d] = %ld\n", j, (long)tid[j]);
        if(pthread_join(tid[j], (void**)&return_value) != 0) {
            perror("join");
            exit(1);
        }
        printf("MT> val -- %d\n", return_value);
    }

    printf("MT> End of program\n");
    
    return 0;
}
