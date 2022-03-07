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

"""
#max and min can be easily created using iteration
def max(ls):
    max_value = None

    for num in ls:
        if (max_value is None or num > max_value):
            max_value = num
    return max_value

def min(ls):
    min_value = None

    for num in ls:
        if (min_value is None or num < min_value):
            min_value = num
    return min_value

#similarly can the for loop of map
#we can avoid casting into string by using % 10 (mod 10)
# but I used it since we have not been explicitly restrained from doing that
"""

def main():
    print(recur(21512))
    print(recur(9891287402))
    print(recur(-7873287432))
    print(iterative(21512))
    print(iterative(9891287402))
    print(iterative(-7873287432))

if __name__ == '__main__':
    main()