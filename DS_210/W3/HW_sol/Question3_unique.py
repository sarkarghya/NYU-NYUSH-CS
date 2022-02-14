def search(S, start, end, target):
    """
    if target is in S[start, end], return True; else False
    """
    if start > end:
        return False
    if S[start] == target:
        return True
    # search the next item in the range
    return search(S, start + 1, end, target)


def uniqueness_helper(S, i):
    """
    Input:
    Requirement: 1) cannot use list slicing; 2) recursive
    """
    if i >= len(S):
        return True

    target = S[i]
    # check if target is in [i+1, end]
    if search(S, i + 1, len(S) - 1, target):
        return False
    return uniqueness_helper(S, i + 1)


def unique(S):
    return uniqueness_helper(S, 0)



def main():
    print(unique([1,7,6,5,4,3,1]))   # False
    print(unique([9,4,3,2,1,8]))     # True
    print(unique(['9',[],4,3,2,1,8]))     # True
    print(unique([1, 3, 2, 1]))    # False
    print(unique([3, 1, 2, 5]))    # True


if __name__ == '__main__':
    main()