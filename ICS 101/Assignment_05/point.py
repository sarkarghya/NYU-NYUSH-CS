#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 00:12:40 2020

@author: xg7
"""

class Point:
    """A class to represent a two-dimensional point"""
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
        
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, new_x):
        self.x = new_x
        
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, new_y):
        self.y = new_y
        
    def move(self, dx, dy):
        self._x += dx
        self._y += dy
    
    def distance(self, point2):
        dx = self._x - point2.x
        dy = self._y - point2.y
        return (dx**2 + dy**2)**0.5
    
    def equals(self, point2):
        return (self.x == point2.x) and (self.y == point2.y)

        
if __name__ == '__main__':
    p1 = Point()
    p1.move(2, 3)
    
    p2 = Point()
    p2.move(5, 7)
    
    print(p1.distance(p2))
