"""
Assignment 1 question 1 Block-wise Palindromes

note:
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.
"""


def block_palindrome(n):
    """
    :param n: a positive integer
    :return: True if n is a block-wise palindrome in blocks size of 2
             False otherwise.
    """
    # To do
    old = n #notice 4 bit numbers
    new = 0 
    while n > 0:
        rem = n & (2**2 -1) # reminder of power of 2
        n = (n >> 2) # 2 (power of 2 for mod) - 1
        new = (new << 2) | rem # xor is addition mod 2
    return old==new


def main():
    print(block_palindrome(215)) # Expect: True
    print(block_palindrome(38))  # Expect: True
    print(block_palindrome(153)) # Expect: False
    print(block_palindrome(105)) # Expect: True


if __name__ == '__main__':
    main()
