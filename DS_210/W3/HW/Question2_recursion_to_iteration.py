def recur(n):#5762
    if n < 0:
        n  = -n
    if n < 10:
        return n, n #first digit, first digit
    a,b = recur(n//10) # =recur(576) 57, 5
    #print(max(n%10, a), min(n%10, b))# 7, 5
    return max(n%10, a), min(n%10, b)


def iterative(n):
    """
    Implement this function. This function should do exactly the same job as recur(n).
    """
    k = list(map(int,str(abs(n))))
    return max(k), min(k)


def main():
    print(recur(21512))
    print(recur(9891287402))
    print(recur(-7873287432))
    print(iterative(21512))
    print(iterative(9891287402))
    print(iterative(-7873287432))

if __name__ == '__main__':
    main()