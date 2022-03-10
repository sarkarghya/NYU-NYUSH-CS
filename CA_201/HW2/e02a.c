#include<stdio.h>
void main(){
    int n, i;
    unsigned long long fact = 1; //long long unsigned int
    printf("Enter a number : ");
    scanf("%d", &n);

    if (n < 0) //show error if number is negative
        printf("Please enter positive numbers!");
    else{
        for(i=1; i<=n; ++i){
            fact *= i ;// computes factorial
        } // ++i returns value before it is incremented
        printf("%d! = %llu", n, fact); // int and unsigned long long int
    }
    return;
}