#include <stdio.h>
/* Exercise 1.1 */
void print_array(int a[], int n)
{
	int i;
	for (i = 0; i < n; i++)
		printf("%d ", a[i]);
    printf("\n");
}

/* Exercise 1.2 */
int array_len( int arr[] ) {
	int count = 0;

    // Increment our counter until NULL TERMINATOR is found
    while (arr[count] != '\0') {
      count++;
    }
    return (count);
}

void read_array(int a[], int n)
{
	int i;
	int l = array_len(a);
	printf("Please enter items to append \n");
	for (i = 0; i < n; i++)
		scanf("%d",&a[i+l]);
}

/* Exercise 1.3 */
int main()
{
	int arr[100] = { 1, 2, 3, 4, 5, 6, 7 };
	print_array(arr, 7);
	//int arr[100] = {} to see empty array
  	printf("Array length = %d \n", array_len(arr));
	read_array(arr, 3); //basically appends 3 items
    print_array(arr, 10);	
	return 0;
}