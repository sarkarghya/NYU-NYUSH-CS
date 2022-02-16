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
    bin_num2, new_num = n, 0
    while n > 0:
        new_dig = n & 3
        n >>= 2
        new_num = (new_num<<2) | new_dig
    # print('our new_num is', bin(new_num),end="\n")
    return new_num == bin_num2



def main():
    print(block_palindrome(215)) # Expect: True
    print(block_palindrome(38))  # Expect: True
    print(block_palindrome(153)) # Expect: False
    print(block_palindrome(105)) # Expect: True


if __name__ == '__main__':
    main()
