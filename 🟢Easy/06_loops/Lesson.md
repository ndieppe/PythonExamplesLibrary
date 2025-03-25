# Python Loops - Beginner's Guide

## Introduction to Loops

Loops allow us to repeat a block of code multiple times. In Python, there are two main types of loops:

1. **Count-controlled loop**: The number of repetitions is predetermined (e.g., using a `for` loop).
2. **Condition-controlled loop**: The number of repetitions depends on a condition (e.g., using a `while` loop).

---

## For Loops

A `for` loop is used when we know how many times we want to execute a block of code.

```python
for x in range(6):  # Loops from 0 to 5 (6 is exclusive)
    print(x)  # Output: 0 1 2 3 4 5
```

We can also specify a starting and ending value:

```python
for x in range(1, 11):  # Loops from 1 to 10
    print(x, end=" ")  # Output: 1 2 3 4 5 6 7 8 9 10
```

_Note:_ Using `end=" "` prevents a new line from being formed after each print statement.

---

## While Loops

A `while` loop continues executing as long as its condition remains `True`.

### Example 1: Password Check (Using `if` statement)

```python
password = "Password7"
user_input = input("Please enter the password: ")
if user_input == password:
    print("Welcome!")
else:
    print("Password was incorrect")
```

### Example 2: Password Check (Using `while` loop)

```python
password = "Password7"
user_input = input("Please enter the password: ")
while user_input != password:  # Loop continues until the correct password is entered
    print("Password was incorrect, please try again: ")
    user_input = input("Please enter the password: ")
print("Welcome!")
```

### Example 3: Password Check with a Maximum of 5 Attempts

```python
password = "Password7"
user_input = input("Please enter the password: ")
attempts = 1  # Start attempt count at 1

while user_input != password and attempts < 5:  # Loop continues while attempts < 5
    print("Password was incorrect, please try again: ")
    user_input = input("Please enter the password: ")
    attempts += 1  # Increment attempt count

if user_input != password:
    print("Failed to enter")  # If max attempts reached, deny access
else:
    print("Welcome")  # If correct password entered, grant access
```

---

## Next Lesson: Collections in Python

In the next lesson, we will learn about **`07_collections`** in Python, such as lists, tuples, and dictionaries.

Happy coding! 🎉
