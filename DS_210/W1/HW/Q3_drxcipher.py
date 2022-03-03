"""
Assignment 1 question 3 Dr X Cipher

note:
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.
"""


def encryptX(plain, key):
    """
    :param plain: String -- a python input string. The plain text.
    :param key: String -- a python input string. The key.

    :return: String -- the cipher python string text.
    """
    # To do
    o_key = key[:]
    while len(plain)>len(o_key):
        o_key += plain[:len(key)][::-1]

    c=''
    for n in range(len(plain)):
        p = ord(plain[n]) - ord("A")
        k = ord(o_key[n]) - ord("A")
        c += chr((p+k)%26 + ord("A"))
    return c

def decryptX(cipher, key):
    '''
    :param cipher: String -- a python input string. The cipher text.
    :param key: String -- a python input string. The key.

    :return: String -- the plain python string text.
    '''
    # To do
    #"""
    mirror = [chr(ord('A') + (ord('A')-ord(x))%26) for x in key]
    key = encryptX(cipher, mirror)[:len(key)][::-1]
    while len(cipher) > len(mirror):
        mirror += [chr(ord('A') + (ord('A')-ord(x))%26) for x in key]
    return encryptX(cipher, mirror)

    #"""


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
