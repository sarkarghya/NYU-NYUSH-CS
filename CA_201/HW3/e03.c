#include <stdio.h>

/* Exercise 3.1 */
void insertion_sort(int a[], int n){
    int c, d, t;
    for (c = 1 ; c <= n - 1; c++) {
        d = c;

        while ( d > 0 && a[d-1] > a[d]) {
            t = a[d];
            a[d] = a[d-1];
            a[d-1] = t;

            d--;
        }
    }
}

/* Exercise 3.2 */
int main()
{
    int n, a[1000], c;

    printf("Enter number of elements\n");
    scanf("%d", &n);

    printf("Enter %d integers\n", n);

    for (c = 0; c < n; c++)
        scanf("%d", &a[c]);

    insertion_sort(a, n);//sort

    printf("Sorted list in ascending order:\n");

    for (c = 0; c <= n - 1; c++) {
        printf("%d\n", a[c]);
    }

    return 0;
}

/* Exercise 3.1 */
//CHECKED