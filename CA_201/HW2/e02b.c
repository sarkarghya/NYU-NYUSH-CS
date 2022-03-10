#include<stdio.h>
void main(){
    int i;
    unsigned long long fact = 1; //long long unsigned int
    while (i < 10){
        i++;// increments by one
        fact *= i ;// computes factorial
        printf("%d! = %llu\n", i, fact); // int and unsigned long long int
    }
    return;
}