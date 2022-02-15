"""
Assignment 1 question 2 String Generator

note:
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.
"""


def string_generator():
    """
    :return: an iterator that would yield all possible strings formed by
             using the characters ‘c’ , ‘a’ , ‘t’ , ‘d’ , ‘o’ , and ‘g’ exactly once.
    """
    # To do
    L = [('','catdog')]
    while len(L) > 0:
        cur_string, cands = L.pop()
        if len(cur_string) == 5:
            yield cur_string + cands
        else:
            for next_char in cands:
                new_string = cur_string + next_char
                L.append((new_string, cands.replace(next_char, '')))


def main():
    catdog_it = string_generator()
    print(next(catdog_it))  # Expect: a permutation of 'catdog'
    for i in range(719):
        next(catdog_it)     # should br executed without an error

    # next(catdog_it)        # Should raise a StopIteration error

    catdog_it = string_generator()
    L = list(catdog_it)
    print('tadcgo' in L)    # Expect: True
    print(len(L))           # Expect: 720


if __name__ == '__main__':
    main()
