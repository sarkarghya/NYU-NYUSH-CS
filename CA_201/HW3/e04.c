#include <stdio.h>

/* Exercise 4.1 */
int eval(int x, int a[], int n)
{
    int result = a[0]; 
    for (int i=1; i<n; i++)
        result = result*x + a[i];
    return result;
}
 

int main()
{
    int a[] = {32, 13, 14};
    int x = 3;
    int n = sizeof(a)/sizeof(a[0]);
    printf("%d", eval(x, a, n));
    return 0;
}
/* Exercise 4.1 */
// already does n multiplications