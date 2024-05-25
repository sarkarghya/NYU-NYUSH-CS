#define _XOPEN_SOURCE 700

#include <philosophers.h>

pid_t pids[NPHIL];
dp_shm *sim_shm;

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


void initialize_output() {
    // Create empty output file
    fd = open(FNAME, O_WRONLY|O_CREAT|O_TRUNC, 0600);
}


void initialize_simulation_shared_memory() {
    printf("%%%% Setting up table %%%%\n");
    // Allocate and initialize shared memory segment and semaphores
    int fd, i;
    fd = shm_open(SHM_NAME, O_CREAT | O_RDWR, 0600);
    if (ftruncate(fd, sizeof(dp_shm)) == -1) {
        perror("ftruncate");
        exit(0);
    }
    sim_shm = (dp_shm*)mmap(NULL, sizeof(dp_shm), PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    for (i = 0; i < NPHIL; i++) {
        sim_shm->chopsticks[i] = 1;
    }
    sem_init(&(sim_shm->mx), IS_SHARED, 1);
    sim_shm->meal_counter = 0;
}


void pick_up_left_chopstick(int rank) {
    sem_wait(&(sim_shm->mx));
    sim_shm->chopsticks[rank] = 0;
    print_chopsticks_status();
    sem_post(&(sim_shm->mx));
}


void pick_up_right_chopstick(int rank) {
    sem_wait(&(sim_shm->mx));
    sim_shm->chopsticks[(rank+1)%NPHIL] = 0;
    print_chopsticks_status();
    sem_post(&(sim_shm->mx));
}


void eat_meal(int rank) {
    sem_wait(&(sim_shm->mx));
    sim_shm->meal_counter++;
    printf("%d> Philo %d is eating meal #%d\n", getpid(), rank, sim_shm->meal_counter);
    log_chopsticks_status();
    sem_post(&(sim_shm->mx));
}


void put_down_left_chopstick(int rank) {
    sem_wait(&(sim_shm->mx));
    sim_shm->chopsticks[rank] = 1;
    print_chopsticks_status();
    sem_post(&(sim_shm->mx));
}


void put_down_right_chopstick(int rank) {
    sem_wait(&(sim_shm->mx));
    sim_shm->chopsticks[(rank+1)%NPHIL] = 1;
    print_chopsticks_status();
    sem_post(&(sim_shm->mx));
}


void print_chopsticks_status() {
    int i;
    char *buffer = (char*)malloc(2 * NPHIL * sizeof(char));
    for (i = 0; i < NPHIL; i++) {
        buffer[i * 2] = '0' + sim_shm->chopsticks[i];
        buffer[i * 2 + 1] = ' ';
    }
    printf("%s\n", buffer);
    free(buffer);
}


void log_chopsticks_status() {
    int i;
    char *buffer = (char*)malloc(2 * NPHIL * sizeof(char));
    for (i = 0; i < NPHIL; i++) {
        buffer[i * 2] = '0' + sim_shm->chopsticks[i];
        buffer[i * 2 + 1] = ' ';
    }
    dprintf(fd, "%s\n", buffer);
    free(buffer);
}


void cleanup_simulation(int signal) {
    int i;
    printf("%%%% Cleaning table %%%%\n");
    // Clean up shared memory segment and semaphores
    cleanup();
    sem_close(&(sim_shm->mx));
    munmap(sim_shm, sizeof(dp_shm));
    shm_unlink(SHM_NAME);
    for (i = 0; i < NPHIL; i++)
        kill(pids[i], SIGKILL);
    close(fd);
}


int main(int argc, char *argv[]) {
    int i;
    
    initialize_signals();
    initialize_output();
    initialize_simulation_shared_memory();
    initialize_shared_memory();
    
    // Generate philosophers
    printf("Inviting %d philosophers to the table for %d meals\n", NPHIL, MEALS);
    for (i = 0; ((i < NPHIL) && ((pids[i] = fork()) > 0)); i++)
        ;   //Do nothing
    
    // Start simulation
    if (i < NPHIL) {
        // Each child is a philosopher of rank i
        // It eats MEALS times, and then exits
        philosopher(i);
    }
    
    for (i = 0; i != NPHIL; i++) {
        wait(NULL);
    }
    printf("All philosophers have left the table\n");

    // Clean up
    cleanup_simulation(SIGINT);

    return 0;
}
