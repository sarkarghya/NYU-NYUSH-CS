def recur(n):
    if n < 0:
        n  = -n
    if n < 10:
        return n, n
    a,b = recur(n//10)
    return max(n%10, a), min(n%10, b)


def iterative(n):
    """
    Implement this function. This function should do exactly the same job as recur(n).
    """
    if n < 0:
        n  = -n
    a = b = n%10
    while n>=10:
        n = n//10
        a = max(a, n%10)
        b = min(b, n%10)
    return a, b


def main():
    print(recur(21512))
    print(recur(9891287402))
    print(recur(-7873287432))
    print(iterative(21512))
    print(iterative(9891287402))
    print(iterative(-7873287432))


if __name__ == '__main__':
    main()