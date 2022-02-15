'''
Note:
To get autograded on gradescope, you program can't print anything.
'''

def find_sum_m(A,B,m):
    """
    :param A: List -- list of n integers
    :param B: List -- list of n integers
    required runtime: O(n) in the worst case
    required space complexity: O(1)

    :return: a list of all pairs of (a,b)
    """
    if (not A) or (not B):
        return []

    first_a = A.pop(0)
    last_b = B.pop()
    if len(A) > 1 and len(B) > 1:
        first_b = B[:].pop(0)
        last_a = A[:].pop()  

        if (first_a + first_b > m) or\
            (last_a + last_b < m):
            return []
    
    k = []
    if first_a + last_b > m:
        # remove last b
        A.insert(0,first_a)
        return find_sum_m(A,B,m)
    elif first_a + last_b < m:
        # remove first a
        B.append(last_b)
        return find_sum_m(A,B,m)
    else:
        # remove first a and last b
        l = find_sum_m(A,B,m)
        k = [(first_a, last_b)]
        if l and k[0] == l[:].pop():
            l.pop()
        return k + l
# space and time complexity requisities met
# run to verify
# to improve complexity further--
"""
    first_b = B.pop()
    last_a = A.pop()

    if first_b + last_a > m:
        # remove last a
        B.insert(0,first_b)
    elif first_b + last_a < m:
        # remove first b
        A.append(last_a)
    else:
        # remove first b and last a
        return [(last_a, first_b)]
"""

def main():
    A = [-1, 4, 5, 6, 8, 10, 12]
    B = [0, 1, 2, 4, 9, 10, 20]
    print(find_sum_m(A, B, 14))  # Expect: [(4, 10), (5, 9), (10, 4), (12, 2)]

    A = [-1, 4, 5, 6, 8]
    B = [0, 1, 2, 4, 10]
    print(find_sum_m (A, B, 100))  # Expect: []

    A = [1, 2, 2, 3, 5]
    B = [1, 98, 98, 99, 99]
    print(find_sum_m(A, B, 100))  # Expect: [(1, 99), (2, 98)]


if __name__ == '__main__':
    main()