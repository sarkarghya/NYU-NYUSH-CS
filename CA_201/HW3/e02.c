#include <stdio.h>

int array_len( int arr[] ) {
	int count = 0;

    // Increment our counter until NULL TERMINATOR is found
    while (arr[count] != '\0') {
      count++;
    }
    return (count);
}

/* Exercise 2.1 */
void linear_search (int a[], int length, int val)
{
	int i;
    for(i=0;i<length;++i)
        if(a[i]==val)
            break;
     
    if(i<length)
        printf("Element found at index %d \n",i);
    else
        printf("Element not found \n");
}

/* Exercise 2.2 */
int is_sorted(int a[] , int length) {
    int i = 0, ord = 1;
    while (ord == 1 && i < length - 1) {
        if (a[i] > a[i+1])
            ord = 0;
        i++;
    }
    return ord;
}

/* Exercise 2.3 */
int binary_search (int a[], int length, int val) {   
    int b = 0, s = length - 1, flag = 1;
    while (b <= s) {
        int m = b + (s - b) / 2;
        if (a[m] == val)
            return m;

        if (a[m] < val)
            b = m + 1;
        else
            s = m - 1;
    }
 
    // if we reach here, then element was
    // not present
    return -1;
}
// If a binary search is called on an unsorted array the index may not be found effectively

int main()
{
	int arr[100] = { 1, 2, 3, 4, 5, 6, 7 };
	linear_search(arr, array_len(arr), 3);
    linear_search(arr, array_len(arr), 8);
    // Please feel free to alter array
    if (is_sorted(arr, array_len(arr)))
        printf("Array is sorted \n");
    else 
        printf("Array not sorted \n");

    printf("%d \n", binary_search(arr, array_len(arr), 3));
    printf("%d \n", binary_search(arr, array_len(arr), 8));//-1 when index not found
    //int arr[100] = {} to see empty array
	return 0;
}