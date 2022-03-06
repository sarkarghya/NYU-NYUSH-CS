
def pend(ls,num, n):
    if len(ls) == 0:
        return []
    ls[0].append(num)
    if getSum(ls[0]) > n:
        #print(getSum(ls[0]),n)
        del ls[0]
    if len(ls) == 0:
        return []
    return [ls[0]]+ pend(ls[1:],num, n)
#'''
def getSum(piece):
    if len(piece)==0:
        return 0
    else:
        return piece[0] + getSum(piece[1:]) 

def filt(ls, N):
    if len(ls)==0:
        return []
    else:
        if getSum(ls[0]) == N:
            return [ls[0]] + filt(ls[1:],N)
        else:
            return [] + filt(ls[1:],N)


def throw_stones(N, M):
    """
    N: Number of stones (N>=1)
    M: Number of days (M>=1)
    """
    # TODO:
    if M == 0:
        return [[]]
    st_1 = pend(throw_stones(N-1,M-1),1, N)
    st_2 = []
    if M%2: #odd day
        st_2 = pend(throw_stones(N-2,M-1),2, N)
    st_3 = pend(throw_stones(N-3,M-1),3, N)
    res = st_1 + st_2 + st_3
    return filt(res, N)


def main():
    print(throw_stones(N=5,
                       M=3))  # Expect: [(1, 1, 3), (1, 3, 1), (2, 1, 2), (3, 1, 1)] or [[1, 1, 3], [1, 3, 1], [2, 1, 2], [3, 1, 1]]
    print(throw_stones(N=6, M=2))  # Expect: [(3, 3)] or [[3, 3]]


if __name__ == '__main__':
    main()