"""
Python Program to Demonstrate Concatenation

Concatenation means joining two or more strings together.
It is commonly used when working with text data.
"""

#*  Basic string concatenation using the + operator
string1 = "Hello"
string2 = "World"
print(string1 + string2) #-> HelloWorld

#* Using the + operator to join two strings
concatenated_string = string1 + " " + string2  # Adding a space in between
print("Concatenated String:", concatenated_string) #-> Hello World (you can also add variables like this without f-strings)

#* Concatenation using the += operator (In-place addition)
string3 = "Python"
string3 += " is fun!"  # Equivalent to string3 = string3 + " is fun!"
print("Using += for concatenation:", string3) #-> Using += for concatenation: Python is fun!

#* Concatenation with numbers (TypeError demonstration)
number = 10
# Uncommenting the below line will cause an error because int and str cannot be directly concatenated
# error_string = "Number: " + number  # TypeError

#* Correct way: Convert number to a string using str()
correct_string = "Number: " + str(number) #this is called casting (mentioned in 04_Inputs.)
print(correct_string) #-> Number: 10

#* Using join() method for concatenation (efficient for multiple strings)
words = ["Python", "is", "powerful"]
joined_string = " ".join(words)  # Joins list elements with a space in between
print("Using join() method:", joined_string) #-> Using join() method: Python is powerful


#* Concatenation using f-strings (Python 3.6+) (from lesson 03_f-strings)
name = "Alice"
age = 25
formatted_string = f"My name is {name} and I am {age} years old."
print("Using f-strings:", formatted_string) #-> Using f-strings: My name is Alice and I am 25 years old.

# Concatenation using format() method
formatted_string2 = "My name is {} and I am {} years old.".format(name, age)
print("Using format() method:", formatted_string2) #-> Using format() method: My name is Alice and I am 25 years old.

# Demonstrating concatenation in loops
sentence = ""
words_list = ["Learning", "Python", "is", "awesome!"]
for word in words_list:
    sentence += word + " "  # Adding each word followed by a space
print("Concatenation in a loop:", sentence.strip())  #-> Concatenation in a loop: Learning Python is awesome! 
#(strip() removes extra trailing space))
