# If-else
#* using Condition statements such as "if" we can change the outcome of a program

#* Admin Checker:
Admin = True # This is another example of boolean
if Admin == True: # Here we use a double "==", in python this means compare, where as single "=" means defining
    print("welcome")
else: 
    print("Insufficient authority, Admin required.")

# Now let's try but with user inputs
#* A password checker:
password = "Password7" # Don't ever make this your password
# Now we need to create a new variable for the user to input a password:
user_input = input("Please enter the password")
if user_input == password: 
    print("Welcome!")
else: #This means if user_input did not equal password
    print("Password was incorrect")

#Please try to make your owbn programs utilising If-else before joining us for lesson 6: loops