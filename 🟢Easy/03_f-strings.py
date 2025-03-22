# F-strings
#* In Python we can use F-strings to insert variables into strings in a readable way

# in lesson 2 you might remember we wrote this:
Age = 19
print("Your age in two years will be:") 
print(Age)

# Now using F-strings we can write this

print(f"Your age in two years will be: {Age}") #-> Your age in two years will be: 19


#* Lets make a simple program to make a print a username for someone:
FirstName = "Nathan"
LastName = "Dieppe"
Age = 17
print(f"Your new username is {FirstName}_{LastName}{Age}") #-> Your new username is Nathan_Dieppe17

#Now try the above with your own way of making a Username before joining us on lesson 4: Inputs