#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:11:08 2017

@author: xg7
"""

class Employee:
    
    def __init__(self): 
        self.name = None
        self.ID = None
        self.department = None
        self.jobTitle = None
        
##Alternatively, we can using the following to initilialize
## but in this exercise, we use the above for practice purpose.
#    def __init__(self, name, ID, department, jobTitle):
#        self.name = name
#        self.ID = ID
#        self.department = department
#        self.jobTitle = jobTitle
#    
    #setter
    ## set_name is an example for setters.
    def set_name(self, name):
        self.name = name
    
    
    #### please complete the following methods
    def set_ID(self, ID):
        self.ID = ID
    
    def set_department(self, department):
        self.department = department
    
    def set_jobTitle(self, jobTitle):
        self.jobTitle = jobTitle
    
    #getter
    ## get_name is an example for getters.
    def get_name(self):
        return self.name
    
    #### please complete the follwing methods
    def get_ID(self):
        return self.ID
    
    def get_department(self):
        return self.department
    
    def get_jobTitle(self):
        return self.jobTitle
    
    '''
    We can use python inbuit @property for all this
    '''


if __name__ == '__main__':
    emp1 = Employee()
    emp1.set_name("Susan Meyers")
    emp1.set_ID("47899")
    emp1.set_department("Accounting")
    emp1.set_jobTitle("Vice President")
    ### Please input the information of the rest employees in the table
    emp2 = Employee()
    emp2.set_name("Wayne Yin")
    emp2.set_ID("696969")
    emp2.set_department("Universe Creation")
    emp2.set_jobTitle("God")
    emp3 = Employee()
    emp3.set_name("Arghya Sarkar")
    emp3.set_ID("424242")
    emp3.set_department("Chocloate eating")
    emp3.set_jobTitle("Legend")
    
    print(emp1.get_name(), emp1.get_ID(), emp1.get_department(), emp1.get_jobTitle() )
    ### Please complete the following code to show employee information, using the getter you defined
    print(emp2.get_name(), emp2.get_ID(), emp2.get_department(), emp2.get_jobTitle() )
    print(emp3.get_name(), emp3.get_ID(), emp3.get_department(), emp3.get_jobTitle() )
    