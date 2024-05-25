#include <prodcons.h>

//TODO: Declare extra structures, types, and variables here

#define _XOPEN_SOURCE 700
#define BFSHM_NAME "/phishm:0"

typedef struct prodcons_extra_shared_memory {
    sem_t tables[BUFSZ];
    sem_t mx_p;
    sem_t mx_c;
    sem_t empty_slots;  
    sem_t full_slots;
} pcx_shm;

pcx_shm *buf_shm;

void initialize_extra_shared_memory() {
    //TODO: initialize the extra elements you declared at the top of the file
    int fd;
    fd = shm_open(BFSHM_NAME, O_CREAT | O_RDWR, 0600);
    if (ftruncate(fd, sizeof(pcx_shm)) == -1) {
        perror("ftruncate");
        exit(0);
    }
    buf_shm = (pcx_shm*)mmap(NULL, sizeof(pcx_shm), PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);

    for(int i = 0; i < BUFSZ; i++) {
        sem_init(&buf_shm->tables[i], IS_SHARED, 1); 
    }

    sem_init(&(buf_shm->empty_slots), IS_SHARED, BUFSZ);
    sem_init(&(buf_shm->full_slots), IS_SHARED, 0); 
    sem_init(&(buf_shm->mx_p), IS_SHARED, 1);
    sem_init(&(buf_shm->mx_c), IS_SHARED, 1);

}

void cleanup_extra() {
    //TODO: close and remove the extra elements you declared at the top of the file

    for(int i = 0; i < BUFSZ; i++) {
        sem_close(&buf_shm->tables[i]);
    }

    sem_close(&(buf_shm->mx_p));
    sem_close(&(buf_shm->mx_c));
    sem_close(&(buf_shm->empty_slots));
    sem_close(&(buf_shm->full_slots)); 
    munmap(buf_shm, sizeof(pcx_shm));
    shm_unlink(BFSHM_NAME);
}


void insert_value(int rank, pc_shm *my_shm) {
    //TODO: Modify this function at your convenience
    
    int index;

    sem_wait(&(buf_shm->mx_p));

    if (my_shm->i_prod - my_shm->i_cons == BUFSZ) {
        sem_post(&(buf_shm->mx_p));
        sem_wait(&(buf_shm->empty_slots));
    }

    index = (my_shm->i_prod)%BUFSZ;
    my_shm->i_prod++;

    sem_post(&(buf_shm->mx_p));

    sem_wait(&(buf_shm->tables[index]));
    // if (my_shm->buffer[index]!= -1) {
    //     sem_post(&(buf_shm->tables[index]));
    // }
    printf("%d> Inserting value %d in cell %d\n", rank, getpid(), index);
    my_shm->buffer[index] = getpid();
    
    sem_post(&(buf_shm->tables[index]));
    
    sem_post(&(buf_shm->full_slots));


    //Uncomment the line below to introduce delay during cell filling
    // sleep(rand()%2+1);
}


void extract_value(int rank, pc_shm *my_shm) {
    //TODO: Modify this function at your convenience
    int val, index;
    sem_wait(&(buf_shm->mx_c));
    if(my_shm->i_cons == my_shm->i_prod) {
        sem_post(&(buf_shm->mx_c));
        sem_wait(&(buf_shm->full_slots)); 
    }
    index = (my_shm->i_cons)%BUFSZ;
    my_shm->i_cons++;

    sem_post(&(buf_shm->mx_c));

    sem_wait(&(buf_shm->tables[index]));
    // if (my_shm->buffer[index]== -1) {
    //     sem_post(&(buf_shm->tables[index]));
    // }
    val = my_shm->buffer[index];
    my_shm->buffer[index] = -1;
    
    printf("%d> Extracted value %d in cell %d\n", rank, val, index);
    sem_post(&(buf_shm->tables[index]));
    
    sem_post(&(buf_shm->empty_slots));
    
}



