# Q1 Write a python program to display a user name followed by Good AfterNoon using input() function

# user_name = input("Enter your name : ")

# print(f"Good AfrerNoon , {user_name}")   # we can use variables in string using 'f' string

# Q2 Write a program to fill name and date in a template 

# name = input("Enter the name : ")
# date = input("Enter the date : ")


# template = f'''
#             Dear {name},
#             You are selected!
#             {date} 
# '''  

# print(template)

# Q3 Write a program to detect double spaces in a string 

double_space = "It is a good day"

isDoubleSpace = double_space.__contains__("  ")
print(isDoubleSpace)
