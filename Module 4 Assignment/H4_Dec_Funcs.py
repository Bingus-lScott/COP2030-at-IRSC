# Homework 4: Numeric Processing / Decorated Functions
# Program By: Landon Scott
# File Name: H4_Dec_Funcs.py
# Function: This program reads and writes to files

# --Function Declaration--

# Displays the meny
def menu():
    '''t'''
    print("Enter an operation")
    print("1 Add")
    print("2 Sub")
    print("3 Multiply")
    print("4 Divide")
    print("0 Quit")
    
    return input(">")

# Runs the correct calculation
def calc(x):
    '''t'''
    if(x == 1):
        print(announce(add))
    elif(x == 2):
        print(announce(sub))
    elif(x == 3):
        print(announce(mult))
    elif(x == 4):
        print(announce(div))

#Gets the user's operand
def get_operand():
    '''Returns the operand inputted by the user'''
    return float(input("Enter an operand: "))

# Operations
def add(x,y):
    '''Returns arg1 + arg2'''
    return x+y
def sub(x,y):
    '''Returns arg1 - arg2'''
    return x-y
def mult(x,y):
    '''Returns arg1 * arg2'''
    return x*y
def div(x,y):
    '''Returns arg1 / arg2'''
    return x/y

# Decorator Function #1
def check_valid(func):
    '''Checks if the inputted user data from the menu function is valid,
    if it is it passes it to the calc function for use,
    otherwise an error message is displayed and the program continues'''
    operation = func() 
    
    if(operation == '1'):
        calc(1)
        return
    elif(operation == '2'):
        calc(2)
        return
    elif(operation == '3'):
        calc(3)
        return
    elif(operation == '4'):
        calc(4)
        return
    elif(operation == '0'):
        print("Good Bye!")
        exit(0)
        return
    else:
        print("Invalid Input!")
             
    return

# Decorator Function #2
def announce(func):
    '''Announces the operation being done in the console then continues function operatiom
n'''
    result = func(get_operand(), get_operand())
    print("Performing ", func.__name__)
    return result

# --Execution--

while(1):
    check_valid(menu)