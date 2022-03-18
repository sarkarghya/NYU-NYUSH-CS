'Assignment 4: Dynamic arrays'
__note__ = "Your codes should start from line 150"


import random


"""This class UserDefinedDynamicArray is the same as in-class"""


import ctypes


class UserDefinedDynamicArray:
    def __init__(self, I=None):
        # I is any iterable
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
        if I:
            for i in I:
                self.append(i)

    def __len__(self):
        return self._n

    def append(self, x):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = x
        self._n += 1

    def _resize(self, newsize):
        A = self._make_array(newsize)
        self._capacity = newsize
        for i in range(self._n):
            A[i] = self._A[i]
        self._A = A

    def _make_array(self, size):
        return (size * ctypes.py_object)()

    def __getitem__(self, i):
        return self._A[i]

    def __setitem__(self, i, x):
        self._A[i] = x   # setitem

    def __delitem__(self, i):  # Remove by index
        for j in range(i, self._n - 1):
            self._A[j] = self._A[j + 1]
        self[-1] = None  # Calls __setitem__
        self._n -= 1
        if (self._n * 4 < self._capacity):
            self._resize(self._capacity // 2)

    def __str__(self):
        return "[" \
               + "".join(str(self[i]) + "," for i in range(self._n-1)) \
               + (str(self[self._n-1]) if not len(self)==0 else "") \
               + "]"


"""The following is a new class for Assignent 4: integer matrix"""


class UDDA_Matrix:
    def __init__( self, numRows=0, numCols=0 ):
        # Create a 2-D UDDA of all zeros
        self._theRows = UserDefinedDynamicArray()
        for _ in range( numRows ) :
            self._theRows.append(UserDefinedDynamicArray([0] * numCols))
        self.r = numRows
        self.c = numCols

    # Gets the contents of the element at
    # 1. position [i, j]
    # 2. row [i]
    def __getitem__( self, ndxTuple ):
        if isinstance(ndxTuple, int):
            if ndxTuple < 0:
                ndxTuple += self.r
            assert ndxTuple >= 0 and ndxTuple < self.r, "Array subscript out of range."
            return self._theRows[ndxTuple]
        else:
            if ndxTuple[0]<0:
                ndxTuple[0] += self.r
            if ndxTuple[1]<0:
                ndxTuple[1] += self.c
            assert ndxTuple[0] >= 0 and ndxTuple[0] < self.r and ndxTuple[1] >= 0 and ndxTuple[1] < self.c, \
            "Array subscript out of range."
            return self._theRows[ndxTuple[0]][ndxTuple[1]]

    # Returns a read-only copy of column
    def get_column(self, col):
        if col < 0:
            col += self.c
        assert col >= 0 and col < self.c, "Array subscript out of range."
        mycol = UserDefinedDynamicArray()
        for i in range(self.r):
            mycol.append(self._theRows[i][col])
        return mycol

    def __str__(self):
        out = ""
        for i in range(self.r):
            out += "".join(str(self[i,j])+"," for j in range(self.c)) + "\n"
        return out

    # Sets the contents of the element at
    # 1. position [i, j] as value
    # 2. row[i] as value if value is a 1D array
    # 3. row[i] as [value, value,..., value] if value is int
    def __setitem__(self, key, value):
        if isinstance(key, int):
            if key < 0:
                key += self.r
            assert key >= 0 and key < self.r, "Array subscript out of range."
            if isinstance(value, int) or value == None :
                for i in range(self.c):
                    self._theRows[key][i] = value
            else:
                assert len(value) == self.c, "Incorrect Input size"
                for i in range(len(value)):
                    self._theRows[key][i] = value[i]
        else:
            if key[0]<0:
                key[0] += self.r
            if key[1]<0:
                key[1] += self.c
            assert key[0] >= 0 and key[0] < self.r and key[1] >= 0 and key[1] < self.c, \
            "Array subscript out of range."
            self._theRows[key[0]][key[1]] = value

    # Sets the contents of the element at
    # 1. col[j] as value if value is a 1D array
    # 2. col[j] as [value, value,..., value]^T if value is int
    def set_column(self, col, value):
        if col < 0:
            col += self.c
        assert col >= 0 and col < self.c, "Array subscript out of range."
        if isinstance(value, int) or value == None:
            for i in range(self.r):
                self._theRows[i][col] = value
        else:
            assert len(value) == self.r, "Incorrect Input size"
            for i in range(self.r):
                self._theRows[i][col] = value[i]

    # Returns the maximum value within this(self) matrix
    def max_value(self):
        to_return = self[0, 0]
        for r in range(self.r):
            for c in range(self.c):
                if self[r, c] > to_return:
                    to_return = self[r, c]
        return to_return

    # Scales the matrix by the given scalar.
    def scaleBy(self, scalar):
        for r in range( self.r ) :
            for c in range( self.c ) :
                self[ r, c ] *= scalar

    def transpose(self):
        newMatrix = UDDA_Matrix( self.c, self.r )
        for r in range( self.r) :
            for c in range( self.c ) :
                newMatrix[c, r] = self[r,c]
        return newMatrix

    def __add__(self, other):
        # Create the new matrix.
        newMatrix = UDDA_Matrix( self.r, self.c )
        # Add the corresponding elements in the two matrices.
        for r in range( self.r) :
            for c in range( self.c ) :
                newMatrix[r,c] = self[r,c] + other[r,c]
        return newMatrix

    # Creates and returns a new matrix that results from matrix subtraction.
    def __sub__(self, other):
        # Create the new matrix.
        newMatrix = UDDA_Matrix( self.r, self.c )
        # Add the corresponding elements in the two matrices.
        for r in range( self.r) :
            for c in range( self.c ) :
                newMatrix[r,c] = self[r,c] - other[r,c]
        return newMatrix

    def __mul__(self, other):
        newMatrix = UDDA_Matrix(self.r, other.c)
        for m in range(self.r):
            for i in range(other.c):
                newMatrix[m, i] = 0
                for j in range(self.c):
                    newMatrix[m, i] += self[m, j] * other[j, i]
        return newMatrix



def main():
    #########Test codes#########
    m1 = UDDA_Matrix(3, 2)
    m2 = UDDA_Matrix(2, 3)
    m3 = UDDA_Matrix(3, 2)

    # Fill m1，m2, m3 with random values
    for row in range(m1.r):
        for col in range(m1.c):
            m1[row, col] = random.randint(-9, 9)

    for row in range(m2.r):
        for col in range(m2.c):
            m2[row, col] = random.randint(-9, 9)

    for row in range(m3.r):
        for col in range(m3.c):
            m3[row, col] = random.randint(-9, 9)

    # Comment them out if you are submitting on gradescope!
    print("matrix 1 is: \n", m1, sep="")
    print("matrix 2 is: \n", m2, sep="")
    print("matrix 3 is: \n", m3, sep="")
    print("------------------------------------------------------")
    print("Maximum value of matrix 1 is", m1.max_value())
    print("------------------------------------------------------")
    print("Transpose of matrix 1:\n", m1.transpose(), sep="")
    print("Transpose of matrix 2:\n", m2.transpose(), sep="")
    print("Transpose of matrix 3:\n", m3.transpose(), sep="")
    print("------------------------------------------------------")
    print("matrix 1 add matrix 3:\n", m1 + m3, sep="")
    print("matrix 1 subtract matrix 3:\n", m1 - m3, sep="")
    print("matrix 1 multiply matrix 2:\n", m1 * m2, sep="")
    print("------------------------------------------------------")
    m1.scaleBy(-4)
    print("Scale matrix m1 -4 times: \n", m1, sep="")


if __name__ == '__main__':
    main()