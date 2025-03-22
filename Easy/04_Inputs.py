# Inputs
# basic syntax: variable = input(string)

#*Remaking last lessons program:
#last lesson we made this program:
FirstName = "Nathan"
LastName = "Dieppe"
Age = 17
print(f"Your new username is {FirstName}_{LastName}{Age}") 

# Now let's reamke it so that a user can type their name in

FirstName = input("Please enter your first name: ") #? Top tip: If you leave a space at the end of the input it make the program look nicer!
LastName = input("Please enter your last name: ")
# In python an input is automatically a string unless you say othewise:
Age = int(input("Enter your age: ")) #the int() Make sure the input is an integer (so maths can be done on it etc.)
print(f"Your username has been generated: {FirstName}_{LastName}{Age}")

# In this Library, after every lesson I suggest you try to remake the program but with your own idea to make sure you understand,
# then refer back to the original program to compare if you need help.
# See you in the next lesson 05_if-else