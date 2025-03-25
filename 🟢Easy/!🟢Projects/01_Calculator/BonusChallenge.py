#second calculator
while exit == False:
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
    exit = input("Would you like to exit? ").lower()
    if exit == "yes":
        exit = True
    else:
        exit = False

#* Congrats, good luck on your next project!!🎉