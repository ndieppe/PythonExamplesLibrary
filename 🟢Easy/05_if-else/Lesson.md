# Understanding If-Else Statements in Python

## What Are Condition Statements?

Condition statements like `if` allow us to change the outcome of a program based on certain conditions.

## Example: Admin Checker

Here’s a simple example that checks if a user is an admin:

```python
Admin = True  # This is a boolean variable (True or False)
if Admin == True:  # The '==' operator checks if two values are equal
    print("Welcome")
else:
    print("Insufficient authority, Admin required.")
```

## Example: Password Checker

Now, let's try a program where the user inputs a password.

```python
password = "Password7"  # Do not use this as a real password!

# Prompt the user to enter a password
user_input = input("Please enter the password: ")

if user_input == password:
    print("Welcome!")
else:  # This runs if the input does not match the password
    print("Password was incorrect")
```

## Example: Grading System with `elif`

The `elif` statement allows us to check multiple conditions. Here’s a grading system example:

```python
score = int(input("Enter your test score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80: #elif is short hand for else-if
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

## Practice Exercise

Before moving to the next lesson, try creating your own programs using `if-else` and `elif` statements. Experiment with different conditions to reinforce your understanding.

---

\*\*Next Lesson: \*\***`06_loops`**
