'''
Note:
To get autograded on gradescope, you program can't print anything.
'''

def merge_generator(I1, I2, I3):
    """
    takes three iterable objects and merges them alternately
    required runtime: O(len(I1) + len(I2) + len(I3)).
    required space complexity: O(1)

    :param I1: Iterable -- the first iterable object.
    :param I2: Iterable -- the second iterable object.
    :param I3: Iterable -- the third iterable object.

    :return: an iterator
    """
    for i in range(max(len(I1), len(I2), len(I3))):
        if i < len(I1):
            yield I1[i]
        if i < len(I2):
            yield I2[i]
        if i < len(I3):
            yield I3[i]


def main():
    for i in merge_generator(range(3), range(95,98), range(-3,0) ):
        print(i, end=", ")
        # Expect: print 0, 95, -3, 1, 96, -2, 2, 97, -1 in the order

    print()
    L = [ i for i in merge_generator( range(1), range(95,98) , range(-2,0) )]
    print(L)  # Expect: [0, 95, -2, 96, -1, 97]

    all = merge_generator( range(4), range(95,96), range(-2,0) )
    print(next(all))  # Expect: 0
    print(next(all))  # Expect: 95
    print(next(all))  # Expect: -2
    print(next(all))  # Expect: 1
    print(next(all))  # Expect: -1
    print(next(all))  # Expect: 2
    print(next(all))  # Expect: 3
    # print(next(all))  # Expect: StopIteration Error

if __name__ == '__main__':
    main()