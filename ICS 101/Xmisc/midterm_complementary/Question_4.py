"""
Created on Sun Mar 14 13:08:49 2021

@author: bing
"""

# Q2.1: Cuboid

class Cuboid:
    # -----replace every "pass" with your code ----#
    def __init__(self, l, w, h, c):
        pass
    def get_attribute(self, attribute):
        pass
    def set_attribute(self, attribute, val):
        pass
    def get_area(self):
        pass
    def get_volume(self):
        pass
    def is_equal(self, cuboid):
        pass
    def __str__(self):
        pass

# Q2.2: CuboidLIst
class CuboidList:

    def __init__(self, l=[]):
        pass
    def remove_cuboid(self, c):
        pass
    def get_cuboids(self, attribute, value):
        pass
    def bubble_sort(self, attr):
        pass
    def sort_bonus(self, attribute):
        """bonus"""
        pass




##Tests, you can comment out them if needed.
if __name__ == "__main__":
## Q2.1
    c = Cuboid(1, 2, 3, "blue")
    ## test 1
    print(c.color)
    ## test 2
    print(c.get_attribute("color"))
    ## test 3
    c.set_attribute("length", 10)
    c.set_attribute("color", "red")
    print(c.color)
    ## test 4
    print(c.get_area())
    ## test 5
    print(c.get_volume())
    ## test 6
    print(c)
    ## test 7
    c1 = Cuboid(1, 2, 3, "blue")
    c2 = Cuboid(2, 3, 4, "blue")
    c3 = Cuboid(1, 2, 3, "BLUE")
    print(c1.is_equal(c2))
    print(c1.is_equal(c3))

## Q2.2
    l = [
         Cuboid(1, 2, 3, "blue"), Cuboid(4, 2, 3, "blue"),
         Cuboid(1, 2, 3, "red"), Cuboid(2, 2, 3, "orange"),
         Cuboid(3, 2, 4, "red"), Cuboid(5, 4, 4, "blue"),
         Cuboid(3, 3, 3, "blue")
         ]

    cList = CuboidList(l)
    ##test 1
    print("---test of initializer---")
    print(cList.d)
    ##test 2
    print("---test of remove---")
    c = Cuboid(1, 2, 3, "blue")
    cList.remove_cuboid(c)
    print(cList.d)
    ##test 3
    print("---test of get_cuboids: height 4---")
    c_height4 = cList.get_cuboids("height", 4)
    for cb in c_height4:
        print(cb)
    ##test4
    print("---test of sort: length---")
    cList = CuboidList(l)
    c_sorted = cList.bubble_sort("length")
    for cb in c_sorted:
        print(cb)
    #test Bonus
    cList = CuboidList(l)
    c_sorted = cList.sort_bonus("length")
    for cb in c_height4:
        print(cb)
