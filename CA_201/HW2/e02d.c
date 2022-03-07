#include<stdio.h>
// program has no errors because we have already used long long unsigned int declaration
// otherwise we would have seen an overflow
void main(){
    int i;
    unsigned long long fact = 1; //long long unsigned int
    while (i < 20){
        i++;
        fact *= i ;// computes factorial
        printf("%d! = %llu\n", i, fact); // int and unsigned long long int
    }
    return;
}