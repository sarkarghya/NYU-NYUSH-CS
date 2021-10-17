#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 13:08:49 2021

@author: bing
"""

# Q2: Cuboid

class Cuboid:
    
    def __init__(self, l, w, h, c):
        self.length = l
        self.width = w
        self.height = h
        self.color = c
    
    def get_attribute(self, attribute):
        if attribute == "length":
            return self.length
        if attribute == "width":
            return self.width
        if attribute == "height":
            return self.height
        if attribute == "color":
            return self.color
    
    def set_attribute(self, attribute, val):
        if attribute == "length":
            self.length = val
        if attribute == "width":
            self.width = val
        if attribute == "height":
            self.height = val
        if attribute == "color":
            self.color = val
    
    def get_area(self):
        return self.width * self.height * 2 + self.width * self.length * 2 + + self.height * self.length * 2
    
    def get_volume(self):
        return self.width*self.height*self.length
    
    def is_equal(self, cuboid):
        if self.length != cuboid.get_attribute("length"):
            return False
        if self.width != cuboid.get_attribute("width"):
            return False
        if self.height != cuboid.get_attribute("height"):
            return False
        if self.color.lower() != cuboid.get_attribute("color").lower():
            return False
        return True
        
    def __str__(self):
        return "Length: {l}, Width: {w}, Height: {h}, Color: {c}, Area: {area}, Volume: {vol}".format(l=self.length, w=self.width, h=self.height, c=self.color, area=self.get_area(), vol=self.get_volume())
    
    
class CuboidList:
    
    def __init__(self, l=[]):
        self.d = {}
        for c in l:
            try:
                self.d[c.get_attribute("color")].append(c)
            except KeyError:
                self.d[c.get_attribute("color")] = [c]
    
    def remove_cuboid(self, c):
        cbs = self.d[c.get_attribute("color")]
        for cb in cbs[::-1]:
            if cb.is_equal(c):
                cbs.remove(cb)
            
    
    def get_cuboids(self, attribute, value):
        values = self.d.values()
        cuboids = []
        for v in values:
            cuboids += v
        for c in cuboids[::-1]:
            if c.get_attribute(attribute) != value:
                cuboids.remove(c)
        return cuboids
    
    def bubble_sort(self, attr):
        values = self.d.values()
        cuboids = []
        for v in values:
            cuboids += v
        for i in range(1, len(cuboids)):
            for j in range(len(cuboids)):
                if cuboids[i].get_attribute(attr) < cuboids[j].get_attribute(attr):
                    cuboids[i], cuboids[j] = cuboids[j], cuboids[i]
        return cuboids
    
    def sort_bonus(self, attribute):
        values = self.d.values()
        cuboids = []
        for v in values:
            cuboids += v
        cuboids.sort(key=lambda x:x.get_attribute(attribute))
        return cuboids
    
    


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
    ##test Bonus
    # cList = CuboidList(l)
    # c_sorted = cList.sort_bonus("length")
    # for cb in c_height4:
    #     print(cb)
    
    
    