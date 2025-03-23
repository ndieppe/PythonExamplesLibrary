# Calculator

#* This is a simple calculator that can do addition, subtraction, multiplication, and division. It is a good project to practice using operators in Python.

#? Task: Create a simple calculator that first asks the user what method they would like to use (addition, subtraction, multiplication, division) and then asks the user for two numbers, returning the result of the method with the two numbers.

operation = input("Would you like to add, subtract, multiply, or divide? ").lower() #.lower() makes the input lowercase
number1 = float(input("Enter the first number: ")) #float() is used to convert the input to a number
number2 = float(input("Enter the second number: "))
if operation == "add":
    print(number1 + number2)
elif operation == "subtract":           
    print(number1 - number2)
elif operation == "multiply":
    print(number1 * number2)
elif operation == "divide":
    print(number1 / number2)

#* BONUS CHALLENGE: Add a loop so the user can do more than one calculation without having to restart the program (solution is in BonusChallenge.py)