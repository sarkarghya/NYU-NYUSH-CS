'''
Note:
To get autograded on gradescope, you program can't print anything.
'''
def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
  
    # If we reach here, then the element
    # was not present
    return None

def is_sorted(T, S):
    """
    tests if T is a sorting of S. No sorting function is allowed
    required runtime: O(nlogn) in the worst case

    :param T: List -- list of integers
    :param S: List -- list of integers, the original list
    
    :return: True/False
    """
    for i in range(len(T)-2):
        if (T[i] < T[i + 1] and T[i + 1] > T[i + 2]) \
            or (T[i] > T[i + 1] and T[i + 1] < T[i + 2]): # O(n) complexity
            return False # o(n) complexity
    if len(T) > 1 and T[0] > T[1]:
        K = []
        for i in range( len(T) - 1, -1, -1) :
            K.append(T[i])
        T = K
    for s in S:
        if not binarySearch(T,0,len(T)-1,s):
            return False
    return True

def main():
    print(is_sorted([1, 2, 3, 4, 5], [2, 4, 3, 1, 5]))  # Expected: True
    print((is_sorted([1, 2, 3, 5, 9], [2, 4, 3, 1, 5])))  # Expected: False
    print(is_sorted([1, 2, 3, 5, 4], [2, 4, 3, 1, 5]))  # Expect: False
    print(is_sorted([5, 4, 3, 2, 1], [2, 4, 3, 1, 5]))  # Expect: True

if __name__ == '__main__':
    main()
    
