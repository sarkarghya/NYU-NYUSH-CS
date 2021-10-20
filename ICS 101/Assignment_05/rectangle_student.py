#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 00:52:11 2020

@author: xg7
"""
from point import Point
try:
    import matplotlib.pyplot as plt
except:
    pass


class Polygon:
    """
    A polygon class with a list of points
    """
    
    def __init__(self):
        self.points = []
        
    def add_point(self, x, y):
        self.points.append(Point(x, y)) #### please
        
    def get_point(self, index):
        #check that the index is valid
        if 0 < index <= len(self.points):
            return self.points[index-1]
        else:
            return 
        
    def plot(self):
        x = []
        y = []
        for i in range(len(self.points)):
            x.append(self.points[i].x)
            y.append(self.points[i].y)
        x.append(self.points[0].x)
        y.append(self.points[0].y)
        try:
            plt.plot(x, y)
            plt.show()
        except:
            pass
        return
    
    def insert_point_at(self, x, y, index):
        self.points.insert(index, Point(x, y))
    
           
class Rectangle(Polygon):
    """
    A rectangle class with a point as a left lower corner
    """
    ##complete the Rectangle to pass the test
    def __init__(self, width, height, p=None):
        super().__init__()
        self.width = width
        self.height = height
        if p is not None:
            self.ll_point = p
        else:
            self.ll_point = Point()
        self.points.append(self.ll_point)
        self.points.append(Point(self.ll_point.x + self.width, self.ll_point.y))
        self.points.append(Point(self.ll_point.x + self.width, self.ll_point.y + self.height))
        self.points.append(Point(self.ll_point.x, self.ll_point.y + self.height))

## test  
if __name__ == "__main__":
    p1 = Polygon()
    p1.add_point(0, 0)
    p1.add_point(0, 3)
    p1.add_point(4, 0)
    #p1.add_point(4, 3)
    #p1.plot()
    
    rect = Rectangle(5, 4, Point(1, 0)) # Try Rectangle(5, 5)
    rect.plot()
            
        
        
