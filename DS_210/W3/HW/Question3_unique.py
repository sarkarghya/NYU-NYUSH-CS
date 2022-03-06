c = [0]
def unique(S):
    """
    :param S: List[Any] -- list of values.
    :return: True if all values within s are unique.
             False otherwise.
    """
    if len(S) == 1:
        return True
    c[0] += 1
    if c[0] > len(S)-1:
        c[0] = 0
        k = S.pop(0)
    if len(S) == 1:
        if S[0] == k:
            return False
        return True
    if S[0] == S[1]:
        return False
    
    S.append(S.pop(1))
    return unique(S)


def main():
    print(unique([0,0]))
    print(unique([1,7,6,5,4,3,1]))   # False
    print(unique([9,4,3,2,1,8]))     # True
    print(unique(['9',[],4,3,2,1,8]))     # True
    print(unique([1, 3, 2, 1]))    # False
    print(unique([3, 1, 2, 5]))    # True


if __name__ == '__main__':
    main()