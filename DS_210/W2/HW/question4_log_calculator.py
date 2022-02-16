'''
Note:
To get autograded on gradescope, you program can't print anything.
'''

def LG1(m,n):
    """
    using the first method, calculate k = lg_m n

    The only arithmetical operations you may use are + and *.
    remember to mention your runtime in terms of k as comment!

    :param m: positive integer, the base
    :param n: positive integer

    :return: k, the greatest integer such that m^k ≤ n
    """
    p, k = m, 0
    while p < n: # net complexity of operations O(log n)
        k += 1
        p *= m
    return k # in terms of k complexity is O(k)

def LG2(m,n):
    """
     using the second method, calculate k = lg_m n
     The only arithmetical operations you may use are + and *.

     :param m: positive integer, the base
     :param n: positive integer
     required runtime complexity: O(logk) in the worst case
     required memory complexity: O(logk)

     :return: k, the greatest integer such that m^k ≤ n
     """
    ls, p = [], 1
    while m < n:
        ls.append((m, p))
        m *= m
        p *= 2
    k, p = 0, 1
    while ls:
        j = ls.pop()
        if p * j[0] <= n:
            k += j[1]
            p *= j[0]
    return k


def main():
    print(LG1(3,345))  # Expect: 5
    print(LG1(3,3_000_000_000))  # Expect: 19

    print(LG2(2, 1000))  # Expect: 9
    print(LG2(2, 3_000_000_000))  # Expect: 31

if __name__ == '__main__':
    main()