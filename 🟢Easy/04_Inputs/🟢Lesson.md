# Introduction to User Input in Python

## Basic Syntax

In Python, you can take user input using the `input()` function:

```python
variable = input("Your prompt message here")
```

## Remaking the Last Lesson's Program

In the previous lesson, we created a program that generated a username using predefined variables:

```python
FirstName = "Nathan"
LastName = "Dieppe"
Age = 17
print(f"Your new username is {FirstName}_{LastName}{Age}")
```

Now, let's modify it so the user can enter their own information.

## Taking User Input

Here’s how we can improve our program by allowing user input:

```python
FirstName = input("Please enter your first name: ")  # Top tip: Adding a space at the end makes it look nicer!
LastName = input("Please enter your last name: ")

# In Python, input() returns a string by default.
# To ensure 'Age' is treated as a number, we use int() to convert it.
Age = int(input("Enter your age: "))  # Converts input into an integer

print(f"Your username has been generated: {FirstName}_{LastName}{Age}")
```

## Practice Exercise

After every lesson, try modifying the program with your own ideas to reinforce learning. Once you’ve written your version, compare it with the original to see if you got it right.

---

**Next Lesson: `05_if-else`**
