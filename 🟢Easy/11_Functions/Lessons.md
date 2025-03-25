# Functions and Procedures in Python

## Introduction

In Python:

- A **function** is a block of code that performs a task and returns a value.
- A **procedure** is a block of code that performs a task but does **not** return a value (in Python, procedures are just functions without a `return` statement).

## Understanding Functions and Procedures

### Example 1: A Procedure

A **procedure** executes a task without returning a value.

```python
def greet_user(name):
    """
    This is a procedure because it does not return a value.
    It simply prints a greeting message.
    """
    print(f"Hello, {name}! Welcome to learning functions and procedures in Python.")
```

#### Usage:

```python
greet_user("John")
```

**Output:**

```
Hello, John! Welcome to learning functions and procedures in Python.
```

### Example 2: A Function

A **function** executes a task and returns a value.

```python
def add_numbers(a, b):
    """
    This is a function because it performs a task AND returns a value.
    It takes two numbers as arguments and returns their sum.
    """
    return a + b
```

#### Usage:

```python
result = add_numbers(10, 5)
print(f"Returned sum: {result}")
```

**Output:**

```
Returned sum: 15
```

### Example 3: A Procedure Calling a Function

A **procedure** can also call a function to perform a task without returning a value.

```python
def print_sum(a, b):
    """
    This is a procedure because it performs a task (printing) but does not return a value.
    """
    sum_result = add_numbers(a, b)  # Calling a function inside a procedure
    print(f"The sum of {a} and {b} is: {sum_result}")
```

#### Usage:

```python
print_sum(7, 3)
```

**Output:**

```
The sum of 7 and 3 is: 10
```

## Running the Program

To execute these functions and procedures in a script, use:

```python
if __name__ == "__main__":
    # Calling the procedure to greet the user
    greet_user("Alice")

    # Calling the function and storing its return value
    result = add_numbers(10, 5)
    print(f"Returned sum: {result}")

    # Calling the procedure that prints the sum
    print_sum(7, 3)
```

## **Top Tip:**

Always use `if __name__ == "__main__":` to prevent code from running when importing functions from this file.

---

🎉 **Congratulations!** This is the last lesson in the **Easy** section. Next, go to the **Easy Projects** folder and start building projects—you'll learn even more along the way! 🚀
