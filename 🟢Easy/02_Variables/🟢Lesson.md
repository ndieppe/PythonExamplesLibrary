# **Understanding Variables in Python**

## **What Are Variables?**

Variables are used to assign names to values, making it easier to store and manipulate data. These values can be of different types, including:

- **String** (text)
- **Integer** (whole numbers)
- **Float** (decimal numbers)
- **Boolean** (True/False)

---

## **Declaring Variables**

You can assign a value to a variable using the `=` operator.

```python
FirstName = "Nathan"  # Try changing this to your name
Age = 17  # Assigning an integer value
```

In the above example:

- `FirstName` is a **string** because it contains text.
- `Age` is an **integer** because it holds a whole number.

You can display the value of a variable using the `print()` function:

```python
print(FirstName)  # Output -> Nathan
```

---

## **Performing Math Operations on Integers**

Python allows you to modify integer variables using mathematical operations.

```python
Age = Age + 1  # Increasing Age by 1
```

A shorter way to do this is:

```python
Age += 1  # This does the same thing as Age = Age + 1
```

Now, let's print the updated value:

```python
print("Your age in two years will be:")  # We added 1 twice
print(Age)
```

---

## **Floats & Boolean Variables**

### **Float (Decimal Numbers)**

A **float** is a number that includes a decimal point.

```python
length = 3.05  # This is a float because it isn't a whole number.
```

Python distinguishes between integers and floats to optimize memory usage (integers use less memory than floats).

### **Boolean (True/False Values)**

A **boolean** variable can hold only two values: `True` or `False`.

```python
triangle = True  # This variable is a boolean (it can be True or False)
```

---

## **Why Use Variables?**

Variables allow us to store and manipulate data efficiently. They can be used in:

- Loops
- Functions
- Conditional statements
- And much more!

---

📌 **Next Lesson:** `03_f-strings` (Introduction to F-Strings)
