"""
Assignment 1 question 4 the MyComplex class

note:
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.
"""


class MyComplex:
    def __init__(self,real_part = 0, imaginary_part = 0):
        self.re = real_part
        self.im = imaginary_part

    def __add__(self, other):
        '''
        @other: a class Complex object, the other complex number.
        DO NOT MODIFY self.
        @return: a ***new*** class Complex object, which is the sum of self + other.
        '''
        result = MyComplex()
        result.re = self.re + other.re
        result.im = self.im + other.im
        return result

    def __iadd__(self, other):
        '''
        @other: a class Complex object, the other complex number.
        @return: self. The value of self should become the sum of self + other.
        '''
        self.re = self.re + other.re
        self.im = self.im + other.im
        return self

    def __sub__(self, other):
        '''
        @other: a class Copmlex object, the other complex number.
        @return: a new class Complex object, which is the subtraction of self - other.
        '''
        result = MyComplex()
        result.re = self.re - other.re
        result.im = self.im - other.im
        return result

    def __mul__(self, other):
        '''
        @other: a class Complex object, the other Complex number.
        @return: a new class Complex object, which is the multiplication of self * other.
        '''
        result = MyComplex()
        result.re = self.re*other.re-self.im*other.im
        result.im = self.re*other.im+self.im*other.re
        return result

    def __eq__(self, other):
        '''
        @other: a class Complex object, the other complex number.
        @return: True if the float value of self is equal to other;
                 False if the float value of self is not equal to other.
        '''
        return self.re == other.re and self.im == other.im

    def __truediv__(self, other):
        '''
        @other: a class Complex object, the other Complex number.
        @return: a new class Complex object, which is the division of self / other.
        '''
        if other.im==0:
            result = MyComplex(self.re/other.re,self.im/other.re)
            return result

        result = self * MyComplex(other.re, -other.im)
        denominator = MyComplex(other.re**2 + other.im**2,0)
        result = result/denominator
        return result

    def __str__(self):
        '''
        Displays the self Complex object nicely.
        Recommended format:
        Suppose,
        self.re = 0.5
        self.im = 0.6
        Then, should return "0.5 + 0.6i"

        @return: The string representation of self Fraction object.
        '''
        if self.im>0:
            return str(self.re)  + '+' + str(self.im) + "i"
        if self.im<0:
            return str(self.re) + str(self.im) + "i"
        else:
            return str(self.re)


def main():
    x = MyComplex(4, -6)
    y = MyComplex(3, 4)
    print(x)        # 4 - 6i
    print(y)        # 3 + 4i
    print(x + y)    # 7 - 2i
    z = x - y
    print(x)        # 4 - 6i
    print(z)        # 1 - 10i
    z += y
    print(z)        # 4 - 6i

    print(x * y)    # 36 - 2i
    print(x / y)    # -0.48 - 1.36i

    print(x*y/y == x)  # True
    print(x/y == MyComplex(-0.48, -1.36))  # True
    print(x == MyComplex(-7, 4))   # False


if __name__ == '__main__':
    main()
