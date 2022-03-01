import ctypes
from types import NoneType

class UserDefinedDynamicArray:
    def __init__(self, I=None):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
        if I:
            self.extend(I)

    def __len__(self):
        return self._n

    def append(self, x):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = x
        self._n += 1

    def _resize(self,newsize):
        A = self._make_array(newsize)
        self._capacity = newsize
        for i in range(self._n):
            A[i] = self._A[i]
        self._A = A

    def _make_array(self,size):
        return (size*ctypes.py_object)()

    def __getitem__(self,i):
        if isinstance(i,slice):
            A = UserDefinedDynamicArray()
            for j in range(*i.indices(self._n)): # * operator was used to unpack the slice tuple
                A.append(self._A[j])
            return A
        if i<0:
            i += self._n
        return self._A[i]

    def __str__(self):
        return ''.join(self[:-1])
        #return "[" \
        #       +",".join( [str(i) for i in self[:-1]] ) \
        #       +(str(self[-1]) if not self.is_empty() else "") \
        #       +"]"

    def is_empty(self):
        # return True if the array is empty
        # Your Code (1 line)
        return self.__len__ == 0

    def __iter__(self):
        # we will do in class, iterate through the list using yield
        # Your Code (2 lines)
        pass
        '''
        while True:
            try:
                j = next(self)
            except StopIteration:
                break
            yield f"{j}"

        '''
          #  yield i if i not NULL


    def __setitem__(self,i,x):
        # we will do in class, think about how to handle negative index
        # Your code
        if i<0 or i>self._n:
            print("Out of range")
            return
          
        if self._n==self.capacity:
            self._resize(2*self.capacity)
              
        for i in range(self._n-1,i-1,-1):
            self._A[i+1]=self._A[i]
              
        self._A[i]=x
        self._n+=1

def main():
    myList = UserDefinedDynamicArray()
    for i in range(10):
        myList.append(i+1)
    print("myList: ", myList) # [1,2,3,...,10]
    print(myList[-1]) # Expect: 10
    print(myList[0])  # Expect: 1

if __name__ == '__main__':
    main()
