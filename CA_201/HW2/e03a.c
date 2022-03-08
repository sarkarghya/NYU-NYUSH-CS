#include <stdio.h>
#include <stdlib.h>
#include <time.h>
 
void main(){
    
    // Use current time as seed for random generator
    srand((unsigned)time(NULL));
    printf("%d\n", rand() % 10 + 1); //use mod to limit output
    printf("%d\n", rand() % 10 + 1);
 
    return;
}