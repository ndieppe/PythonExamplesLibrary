#functions and procedures.

"""
In Python:
- A *function* is a block of code that performs a task and returns a value.
- A *procedure* is a block of code that performs a task but does NOT return a value (in Python, procedures are just functions without a return statement).
"""

def greet_user(name):
    
    #* This is a procedure because it does not return a value.
    #* It simply prints a greeting message.
    
    print(f"Hello, {name}! Welcome to learning functions and procedures in Python.")

def add_numbers(a, b):
    
    #* This is a function because it performs a task AND returns a value.
    #* It takes two numbers as arguments and returns their sum.
    
    return a + b

def print_sum(a, b):
    
    #* This is a procedure because it performs a task (printing) but does not return a value.
    sum_result = add_numbers(a, b)  # Calling a function inside a procedure
    print(f"The sum of {a} and {b} is: {sum_result}")

#* Main program execution
# Calling the procedure to greet the user
greet_user("John")  #-> Hello, John! Welcome to learning functions and procedures in Python.

if __name__ == "__main__": #? Top Tip: Always use this line to prevent code from running when importing functions from this file.
    # Calling the procedure to greet the user
    greet_user("Alice") #-> Hello, Alice! Welcome to learning functions and procedures in Python.
    
    # Calling the function and storing its return value
    result = add_numbers(10, 5)
    print(f"Returned sum: {result}")  #-> Returned sum: 15
    
    # Calling the procedure that prints the sum
    print_sum(7, 3) #-> The sum of 7 and 3 is: 10

#* Congrats this is the last lesson ofthe Easy section. 
#* Next go to the Easy projects folder and start building projects (you will learn more on the way)
