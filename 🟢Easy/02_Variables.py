#Variables
#* Variables are the way we give a names to values (String, Integer, Float, Boolean)

#You can give a variable any name
FirstName = "Nathan" #try change this your name
Age = 17 
#Above with see FirstName (a string) and Age (integer) being assigned values

# When you see me use "->" in comments, this means this is the output
print(FirstName) #-> Nathan

#* We can do maths on Integers:
Age = Age + 1
#The above code increases the Age variable by 1, but this can be done simpler:
Age += 1

print("Your age in two years will be:") #we added 1 twice:
print(Age)


#* Floats & Boolean:
length = 3.05 #This is an example of a float because it isn't a whole number.
# We use Integers as well as floats to save memory on a computer (Integers use less memory than integers)
triangle = True #This is a boolean variable (it can either be True or False)

# Variables can be used in many ways, such as in loops, functions, and more.
#* Next lesson: 03_f-strings.py