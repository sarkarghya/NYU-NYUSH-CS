#include <stdio.h>
#include <stdlib.h>
#include <time.h>
 
void main(){
    // Use current time as seed for random generator
    srand((unsigned)time(NULL));
    
    for(int i = 0; i<10; i++)
        printf("%d ", rand() % 6 + 1); //use mod to limit output
   
    return;
}