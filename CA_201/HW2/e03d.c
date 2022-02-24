#include <stdio.h>
#include <stdlib.h>
#include <time.h>
 
void main(){
    int r, c;
    // Use current time as seed for random generator
    srand((unsigned)time(NULL));
    for(int i = 0; i<10; i++){
        for(int i = 0; i<10; i++){
            r = rand() % 6 + 1;
            if (r == 6)
                c++; // increase count by one
            printf("%d ", r);
            } //use mod to limit output
        printf("\n");
        }
    printf("Number of 6 in matrix is %d", c);
    return;
}