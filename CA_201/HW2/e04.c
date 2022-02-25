#include <stdio.h> 

int fib(int n){ 
	// Base case
    if (n <= 1){ 
        return n; 
    }
    // Recursive call
    return fib(n - 1) + fib(n - 2); 
} 
  
int main(){ 
    int n, i;
    printf("Enter a Number : ");
    scanf("%d",&n);
    // Printing
    for (i=0; i<=n; ++i)
        printf("Year %d: %d\n", i, fib(i+1));
} 