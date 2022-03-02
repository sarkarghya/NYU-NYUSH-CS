'''
Note:
To get autograded on gradescope, you program can't print anything.
'''

def binar(A, x):
    low = 0
    high =len(A)-1
    while low <= high:
        mid = (low + high)//2
        if A[mid] < x:
            low = mid + 1
        elif A[mid] > x:
            high = mid - 1
        else:
            return True
    return None

def is_sorted(T, S):
    """
    tests if T is a sorting of S. No sorting function is allowed
    required runtime: O(nlogn) in the worst case

    :param T: List -- list of integers
    :param S: List -- list of integers, the original list
    
    :return: True/False
    """
    for i in range(len(T) - 2):
        if (T[i] < T[i + 1] and T[i + 1] > T[i + 2]) or (T[i] > T[i + 1] and T[i + 1] < T[i + 2]):
            return False
    if len(T) > 1 and T[0] > T[1]:
        T.reverse()
    for s in S:
        if not binar(T, s):
            return False
    return True

def main():
    print(is_sorted([1, 2, 3, 4, 5], [2, 4, 3, 1, 5]))  # Expected: True
    print((is_sorted([1, 2, 3, 5, 9], [2, 4, 3, 1, 5])))  # Expected: False
    print(is_sorted([1, 2, 3, 5, 4], [2, 4, 3, 1, 5]))  # Expect: False
    print(is_sorted([5, 4, 3, 2, 1], [2, 4, 3, 1, 5]))  # Expect: True

if __name__ == '__main__':
    main()
    
