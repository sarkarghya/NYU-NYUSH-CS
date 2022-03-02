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
    counterpart = len(B) - 1
    pairs = []
    for a in A:
        if a + B[counterpart] == m:
            if len(pairs) == 0 or pairs[-1] != (a, B[counterpart]):
                pairs.append((a, B[counterpart]))
        counterpart = max(0, counterpart - 1)
    return pairs

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