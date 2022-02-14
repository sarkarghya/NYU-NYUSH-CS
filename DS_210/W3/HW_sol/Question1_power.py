def power(x,n):
    """
    Compute x^n, where x, n can both be negative integer.
    :param x: Int -- the base
    :param n: Int -- the exponent

    :return: Int -- x^n
    """
    if n==0:
        return 1
    elif n==-1:
        return 1/x
    else:
        partial = power(x,n//2)
        result = partial*partial
        if n%2==1:
            result*=x
        return result

def main():
    print(power(-2, 4))     # 16
    print(power(4, 3))      # 64
    print(power(-2, -3))    # -0.125

if __name__ == '__main__':
    main()

