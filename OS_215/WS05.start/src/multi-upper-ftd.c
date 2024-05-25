#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <ctype.h>
#include <pthread.h>

#define NB_THREAD 3
#define MAX_FILES 100
#define MAX_FNAME_LENGTH 255

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cond = PTHREAD_COND_INITIALIZER;

int total_files;
char fname_list[MAX_FILES][MAX_FNAME_LENGTH];

void* multi_convert(void* argv) {
    
    int index;
    while (1) {
        pthread_mutex_lock(&mutex);
        index = total_files - 1;
        total_files--;
        pthread_mutex_unlock(&mutex);
        if (index < 0)
            break;

        printf("ST - PROCESS> %ld - %s\n", (long)pthread_self(), (char*)fname_list[index]);

        FILE *fp1, *fp2;
        char dest_fname[128];
        int c = 1;
        
        fp1 = fopen ((char*)fname_list[index], "r");
        strcpy(dest_fname, (char*)fname_list[index]);
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

    }

    // printf("ST - EXIT> %ld \n", (long)pthread_self());
    pthread_exit((void*)0);

}

int main (int argc, char ** argv) {

    int i;
    total_files = argc - 1;
    for (int j = 0; j < total_files; j++)
        strcpy(fname_list[j], argv[j+1]);

    pthread_t tid[NB_THREAD];
    // printf("%d threads created\n", num_threads);

    pthread_mutex_lock(&mutex);
    for (i = 0; i < NB_THREAD; i++){
        pthread_create((pthread_t*)&tid[i], NULL, multi_convert, NULL);
    }
    pthread_mutex_unlock(&mutex);

    for (i = 0; i < NB_THREAD; i++){
        // We do not need to consider join status here
        if(pthread_join(tid[i], NULL) != 0) {
            perror("join");
            exit(1);
        }
    }
    return EXIT_SUCCESS;
}