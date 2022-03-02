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
    accum_prod = m
    k = 0
    while accum_prod < n:
        k += 1
        accum_prod *= m
    return k

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
    m_powers, cur_prod, l = [], m, 1
    while cur_prod < n:
        m_powers.append([cur_prod, l])
        cur_prod *= cur_prod
        l *= 2
    k, cur_prod = 0, 1
    for i in range(len(m_powers) - 1, -1, -1):
        if cur_prod * m_powers[i][0] <= n:
            k += m_powers[i][1]
            cur_prod *= m_powers[i][0]
    return k

def main():
    print(LG1(3,345))  # Expect: 5
    print(LG1(3,3_000_000_000))  # Expect: 19

    print(LG2(2, 1000))  # Expect: 9
    print(LG2(2, 3_000_000_000))  # Expect: 31

if __name__ == '__main__':
    main()