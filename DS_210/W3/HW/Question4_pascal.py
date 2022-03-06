def pedro(ls):
    if len(ls) == 1:
        return [1]
    k = [ls.pop() + ls[len(ls)-1]]
    return pedro(ls[:len(ls)]) + k

def pascal(k):
    """
    :param k: Int -- Level k of pascal triangle

    :return: List[Int] -- a list of pascal values at level k
    """
    if k == 0:
        return [1]
    elif k == 1:
        return [1,1]
    else:
        return pedro(pascal(k-1)) + [1]


def main():
    print(pascal(3))    # [1, 3, 3, 1]
    print(pascal(0))    # [1]
    print(pascal(5))    # [1, 5, 10, 10, 5, 1]


if __name__ == '__main__':
    main()







