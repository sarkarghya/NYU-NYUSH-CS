"""
Assignment 1 question 2 String Generator

note:
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.
"""
from itertools import permutations 

def string_generator():
    """
    :return: an iterator that would yield all possible strings formed by
             using the characters ‘c’ , ‘a’ , ‘t’ , ‘d’ , ‘o’ , and ‘g’ exactly once.
    """
    # To do 
    return map(''.join,permutations('catdog'))
"""
def string_generator():
    s = 'catdog'

    # create a list and intialize
    par = []
    par.append(s[0])
 
    for i in range(1, len(s)):
        for j in range(len(par))[::-1]:
            curr = par.pop(j)
            for k in range(len(curr) + 1):
                par.append(curr[:k] + s[i] + curr[k:])
 
    return iter(par)
"""
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
