"""
Assignment 1 question 3 Dr X Cipher

note:
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.
"""


def encryptX(plain, key):
    '''
    @plain: a python input string. The plain text.
    @key: a python input string. The key.

    @return: the cipher python string text.
    '''
    new_key = key
    while len(plain)>len(new_key):
        new_key += ''.join(reversed(plain[:len(key)]))
    cipher = []
    for n in range(len(plain)):
        cipher.append( chr(ord('A') + (ord(plain[n]) + ord(new_key[n]) - 2 * ord('A')) % 26) )
    return ''.join(cipher)


def decryptX(cipher, key):
    '''
    @cipher: a python input string. The cipher text.
    @key: a python input string. The key.

    @return: the plain python string text.
    '''
    rev_key = ''.join([chr(ord('A') + (ord('A') + 26 - ord(char))) for char in key])
    plain = encryptX(cipher, rev_key)
    if len(cipher) <= len(key):
        return plain

    plain = plain[:len(key)]
    while len(cipher) > len(rev_key):
        rev_key += ''.join([chr(ord('A') + (ord('A') + 26 - ord(char))) for char in reversed(plain)])
    return encryptX(cipher, rev_key)


def main():
    print(encryptX("ATTACKATDAWN", "QUE"))  # QNXTVKTMDTPN

    print(encryptX("DATASTRUCTURE", "NYUSH"))   # QYNSZLRNCWMRX

    print( encryptX("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NYUSH"))  # NZWVLJJJJJOOOOOTTTTTYYYYYD

    print( encryptX("CUTE", "NYUSH"))  # PSNW

    print(decryptX("QNXTVKTMDTPN", "QUE"))   # ATTACKATDAWN
    print( decryptX("QYNSZLRNCWMRX", "NYUSH"))   # DATASTRUCTURE
    print( decryptX("NZWVLJJJJJOOOOOTTTTTYYYYYD", "NYUSH"))   # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    print( decryptX("PSNW", "NYUSH"))  # CUTE


if __name__ == '__main__':
    main()
