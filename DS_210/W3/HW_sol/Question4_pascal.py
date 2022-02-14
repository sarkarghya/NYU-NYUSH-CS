def pascal(k):
    """
    :param k: Int -- Level k of pascal triangle

    :return: List[Int] -- a list of pascal values at level k
    """
    pass
    return pascal_helper(k,k)


def pascal_helper(k, i):
    if i == 0:
        return [1]
    if i == k:
        return pascal_helper(k,i-1)+[1]
    lissy_minus_one = pascal_helper(k - 1, i)
    return pascal_helper(k, i - 1) + [lissy_minus_one[i - 1] + lissy_minus_one[i]]


def main():
    print(pascal(3))    # [1, 3, 3, 1]
    print(pascal(0))    # [1]
    print(pascal(5))    # [1, 5, 10, 10, 5, 1]


if __name__ == '__main__':
    main()







