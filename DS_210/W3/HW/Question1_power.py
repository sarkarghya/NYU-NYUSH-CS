def power(x,n):
    """
    Compute x^n, where x, n can both be negative integer.
    :param x: Int -- the base
    :param n: Int -- the exponent

    :return: Int -- x^n
    """
    if n == 0:
        return 1
    if n < 0:
        x, n = 1/x, -n
    res = power(x, n//2)
    if n % 2:
        return res*res*x
    else:
        return res*res

def main():
    print(power(-2, 4))     # 16
    print(power(4, 3))      # 64
    print(power(-2, -3))    # -0.125

if __name__ == '__main__':
    main()

