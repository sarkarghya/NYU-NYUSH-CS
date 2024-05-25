#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <ctype.h>
#include <pthread.h>

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cond = PTHREAD_COND_INITIALIZER;

int td_num;

void* multi_convert(void* argv) {
    FILE *fp1, *fp2;
    char dest_fname[128];
    int c = 1;
    
    fp1 = fopen ((char*)argv, "r");
    strcpy(dest_fname, (char*)argv);
    strcat(dest_fname, ".UPPER.txt");
    printf("%s\n", dest_fname);
    fp2 = fopen (dest_fname, "w");
    if ((fp1 == NULL) || (fp2 == NULL)) {
        perror ( "fopen");
        exit (1);
    }
    
    while (c != EOF) {
        c = fgetc(fp1);
        if (c != EOF)
            fputc(toupper(c), fp2);
//            fputc(toupper(c), stdout);
    }
    
    fclose (fp1);
    fclose (fp2);

    // Protect the counter
    pthread_mutex_lock(&mutex);
    td_num--;
    if(td_num == 0)
        pthread_cond_signal(&cond);
        // signals to release the original thread
    pthread_mutex_unlock(&mutex);
    pthread_exit((void*)0);

}

int main (int argc, char ** argv) {

    int i;
    td_num = argc - 1; 
    pthread_t tid[td_num];

    // printf("MT> %ld Hi I am the original thread\n", (long)pthread_self());
    pthread_mutex_lock(&mutex);
    for (i = 0; i < td_num; i++){
        // printf("argv[%d]: %s\n", i, argv[i+1]);
        pthread_create((pthread_t*)&tid[i], NULL, multi_convert, (char*)argv[i+1]);
    }
    // After creating threads, the main thread waits using pthread_cond_wait 
    pthread_cond_wait(&cond, &mutex);
    // original thread release
    // printf("MT> %ld Hi I am the original thread\n", (long)pthread_self());
    pthread_mutex_unlock(&mutex);

    return EXIT_SUCCESS;
}
