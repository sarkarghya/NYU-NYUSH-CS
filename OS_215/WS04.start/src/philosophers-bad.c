#include <philosophers.h>


#define _XOPEN_SOURCE 700
#define PHISHM_NAME "/phishm:0"


typedef struct philosophers_shared_memory{
    sem_t sync[NPHIL];
} philo_shm;

philo_shm *my_shm;


void initialize_shared_memory() {
    // Allocate and initialize shared memory segment and semaphores
    int fd, i;
    fd = shm_open(PHISHM_NAME, O_CREAT | O_RDWR, 0600);
    if (ftruncate(fd, sizeof(philo_shm)) == -1) {
        perror("ftruncate");
        exit(0);
    }
    my_shm = (philo_shm*)mmap(NULL, sizeof(philo_shm), PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    for (i = 0; i < NPHIL; i++) {
        sem_init(&(my_shm->sync[i]), IS_SHARED, 1);
    }
}

void pick_up_chopsticks(int rank) {
    sem_wait(&(my_shm->sync[rank]));
    pick_up_left_chopstick(rank);
    sem_wait(&(my_shm->sync[(rank+1)%NPHIL]));
    pick_up_right_chopstick(rank);
}


void put_down_chopsticks(int rank) {
    put_down_left_chopstick(rank);
    sem_post(&(my_shm->sync[rank]));
    put_down_right_chopstick(rank);
    sem_post(&(my_shm->sync[(rank+1)%NPHIL]));
}


void cleanup() {
    // Clean up shared memory segment and semaphores
    int i;
    for (i = 0; i < NPHIL; i++)
        sem_close(&(my_shm->sync[i]));
    munmap(my_shm, sizeof(philo_shm));
    shm_unlink(PHISHM_NAME);
}


void philosopher(int rank) {
    int i;
    
    printf("%d> Philo %d is at the table\n", getpid(), rank);
    srand(getpid());

    for (i = 0; i < MEALS; i++) {
        printf("%d> Philo %d is thinking\n", getpid(), rank);
        // sleep(rand()%2+1);
        printf("%d> Philo %d is hungry\n", getpid(), rank);
        pick_up_chopsticks(rank);
        eat_meal(rank);
        // sleep(rand()%2+1);
        put_down_chopsticks(rank);
    }

    printf("%d> Philo %d is leaving the table\n", getpid(), rank);
    exit(0);
}
