#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 10:49:18 2020

@author: xg7
"""

from employee_class_student import Employee
import pickle as pk


def main(quit_system):
    MENU = ("1.Look up\n"
            "2.Add new employee\n"
            "3.Change employee information\n"
            "4.Delete employee\n"
            "5.Quit\n"
            "Please select an operation: ") 
        
 
    option = input(MENU)
    
    if option not in "12345":
#        raise Exception("Invalid option!", option) 
        print("Invalid option!", option)
        return quit_system
    try:
##     loading the emp_database.dat,
        with open('emp_database.dat', 'rb') as file:
            emp_dict = pk.load(file) # you code for loading emp_dict 
            #print(emp_dict)
    except (FileNotFoundError, EOFError):
        emp_dict = {}
     
    if option == '1':
        lookUp = input("Please given the ID: ")
        try:
            theEmployee = emp_dict[lookUp]
            print("ID: {ID}\n{name}\n{dept}\n{jobtitle}".format(ID = theEmployee.get_ID(),\
              name = theEmployee.get_name(), dept = theEmployee.get_department(),\
              jobtitle = theEmployee.get_jobTitle())) 
        except KeyError:
            print("No such an ID.")
    elif option == '2':
        empInfo = input("Please given name/ID/department/job title: ")
        empInfo = empInfo.split('/')
        #print("empInfo", empInfo)
        try:
            k_id = empInfo[1]
            emp_dict[k_id] = Employee()
            emp_dict[k_id].set_name(empInfo[0])
            emp_dict[k_id].set_ID(empInfo[1])
            emp_dict[k_id].set_department(empInfo[2])
            emp_dict[k_id].set_jobTitle(empInfo[3])
        except IndexError:
            print("Incorrect input format.")
        
    elif option == '3':
    ##Please remove the pass and complete this branch
        k_id = input("Please give the ID: ")
        try:
            theEmployee = emp_dict[k_id]            
            change_val = ["Name", "Department", "Job Title"]
            set_target = [theEmployee.set_name, theEmployee.set_department, theEmployee.set_jobTitle]
            get_seed = [theEmployee.get_name(), theEmployee.get_department(), theEmployee.get_jobTitle()]
            print(f"The currently stored values for employee ID {theEmployee.get_ID()} are as follows")
            [print(f'{n+1}) {v}: {get_seed[n]}') for n,v in enumerate(change_val)]
            idx = int(input("I want to change entry number:")) - 1 
            change = input(f'I would you like to change the {change_val[idx]} currently \"{get_seed[idx]}\" to:')
            set_target[idx](change)
            print("The change was successful!")
        except KeyError:
            print("No such an ID.")
        except (IndexError, ValueError):
            print("Incorrect input format.")
    
    
    elif option == '4':
    ##Please remove the pass and complete this branch
        k_id = input("Please give the ID: ")
        try:
            del emp_dict[k_id]
        except KeyError:
            print("No such an ID.")
        
    elif option == '5':
        quit_system = True
        return quit_system
    
    ##saving emp_dict 
    Database = open('emp_database.dat', 'wb')
    ##your code for saving emp_dict insert goes here
    pk.dump(emp_dict, Database)
    
    Database.close()
    return quit_system

     
if __name__ == '__main__':
    
    quit_system = False
    while not quit_system:
        quit_system = main(quit_system)
