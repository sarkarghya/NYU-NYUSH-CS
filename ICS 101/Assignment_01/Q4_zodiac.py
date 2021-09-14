# get user input
your_year =  input("Enter a year: ")
while True:
    try:
        year = int(your_year)
        while year < 0:
            print("Input should be non-negative")
            year = int(input("Enter a year: "))
        zod_list = [
            "Monkey",
            "Rooster",
            "Dog",
            "Pig",
            "Rat",
            "Ox",
            "Tiger",
            "Hare",
            "Dragon",
            "Snake",
            "Horse",
            "Sheep"
            ]
        print(year, "is the year of", zod_list[year % 12])
        break
    except:
        print("Input should be a non-negative integer")
        your_year =  input("Enter a year: ")
        
"""
This program is important
"""
## you code needs to do the following things:
## 1. check if it is a integer; if not, ask the user to re input 
## 2. check if it is non negative; if not, ask the user to re input 
## 3. print the user's animal of the year on the screen
