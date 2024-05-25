#include <prodcons.h>

sem_t *sprod;
sem_t *scons;

pc_shm *my_shm;

void cleanup(int sig) {
    cleanup_extra();
    // Clean up shared memory segment and semaphores
    munmap(my_shm, sizeof(pc_shm));
    shm_unlink(PCSHM_NAME);
}

void initialize_shared_memory() {
    // Allocate and initialize shared memory segment and semaphores
    int fd;
    fd = shm_open(PCSHM_NAME, O_CREAT | O_RDWR, 0600);
    if (ftruncate(fd, sizeof(pc_shm)) == -1) {
        perror("ftruncate");
        exit(0);
    }
    my_shm = (pc_shm*)mmap(NULL, sizeof(pc_shm), PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    my_shm->i_prod = 0;
    my_shm->i_cons = 0;
    initialize_extra_shared_memory();
}


void initialize_signals() {
    // Register cleanup function so that ctrl-C triggers it
    struct sigaction action;
    sigset_t mask;
    sigemptyset(&mask);
    action.sa_handler = &cleanup;
    action.sa_flags = 0;
    action.sa_mask = mask;
    sigaction(SIGINT, &action, NULL);
}


void producer(int rank) {
    printf("%d> Producer %d is ready\n", getpid(), rank);

    while (my_shm->i_prod < MAX_ITEMS) {
        sem_wait(sprod);
        insert_value(rank, my_shm);
        sem_post(scons);
    }

    printf("%d> Producer %d is done\n", getpid(), rank);
    exit(0);
}

void consumer(int rank) {
    printf("%d> Consumer %d is ready\n", getpid(), rank);

    while (my_shm->i_cons < MAX_ITEMS) {
        sem_wait(scons);
        extract_value(rank, my_shm);
        sem_post(sprod);
    }

    printf("%d> Consumer %d is done\n", getpid(), rank);
    exit(0);
}


int main(int argc, char** argv) {
    int i, nprods, ncons;
    
    srand(getpid());

    if (argc != 3) {
        printf("Incorrect usage: $ %s <NPRODS> <NCONS>\n", argv[0]);
        exit(1);
    }
    nprods = atoi(argv[1]);
    ncons = atoi(argv[2]);
    
    initialize_signals();
    initialize_shared_memory();
    
    sprod = sem_open("/sprod:0", O_CREAT|O_RDWR, 0600, BUFSZ);
    scons = sem_open("/scons:0", O_CREAT|O_RDWR, 0600, 0);

    // Generate producers & consumers
    printf("Creating %d producers\n", nprods);
    for (i = 0; ((i < nprods) && (fork() > 0)); i++)
        ;   //Do nothing
    if (i < nprods) {
        producer(i);
    }
    printf("Creating %d consumers\n", ncons);
    for (i = 0; ((i < ncons) && (fork() > 0)); i++)
        ;   //Do nothing
    if (i < ncons) {
        consumer(i);
    }

    
    // Start simulation
    
    for (i = 0; i < (ncons+nprods); i++) {
        printf("%d was dead\n", i);
        wait(NULL);
        
    }
    printf("All children have completed their execution\n");

    // Clean up
    sem_close(sprod);
    sem_unlink("/sprod:0");
    sem_close(scons);
    sem_unlink("/scons:0");
    cleanup(SIGINT);

    return 0;

}
