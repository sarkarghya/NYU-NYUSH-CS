Name  - Arghya Sarkar
NetID - abs9425

** I know sem_t empty_slots and sem_t full_slots are not required but I just impemented them for extra safety and testing purposes. **

The extra shared memory segment contains a semaphore for each buffer cell to control access to that cell exclusively. There are also semaphores to track empty and full slots in the buffer and mutex semaphores for producers and consumers to coordinate access to the buffer counters.

When a producer wants to insert a value, it acquires the producer mutex semaphore to check that the buffer is not full. If full, it releases the mutex and waits on the empty slots semaphore. It then calculates the index to insert into, increments the producer counter, and releases the mutex. It waits on the cell's semaphore, inserts the value, and posts the cell's semaphore. It finally posts the full slots semaphore.

When a consumer wants to extract a value, it does something similar - acquiring the consumer mutex to check the buffer is not empty, waiting on the full slots semaphore if so, calculating index, incrementing consumer counter, releasing mutex, waiting and posting the cell semaphore, and posting the empty slots semaphore.

This allows maximum concurrency since processes can access different cells concurrently. It prevents concurrent access to the same cell. Producers cannot fill occupied cells, and consumers cannot empty vacant cells. The mutexes prevent concurrent updates to the counters. The empty and full slots semaphores prevent overflow/underflow. Together this avoids deadlock.

Note: This solution may still give deadlocks for unknown reasons but its quite rare (once every 20-150 times).
count=0; while true; do make && make clean; ((count++)); done
echo $count