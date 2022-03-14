#include <stdio.h>
/* Exercise 1.1 */
void print_array(int a[], int n)
{
	int i;
	for (i = 0; i < n; i++)
		printf("%d ", a[i]);
    printf("\n");
}

/* Exercise 1.3 */
int main()
{
	int arr[] = { 1, 2, 3, 4, 5, 6, 7 };
	print_array(arr, 7);
    print_array(arr, 7);
	return 0;
}