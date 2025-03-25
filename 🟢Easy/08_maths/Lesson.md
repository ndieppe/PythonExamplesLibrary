# Maths or Math (It is Definitely Called Maths)

## Importing the Math Module

In Python, we can use code that others have written to help us with programming. One such module is `math`, which provides useful mathematical functions and constants.

```python
import math  # This is importing code someone else made to help us program

print(math.pi)  # -> 3.141592653589793
print(math.e)   # -> 2.718281828459045
```

For the rest of this lesson, we won't use the `math` module.

---

## Basic Arithmetic Operations

Python allows us to perform basic mathematical operations such as addition, subtraction, multiplication, and division.

### Addition

```python
print(5 + 10)  # -> 15
```

We can also use variables:

```python
age = 17
FutureYears = 5
FutureAge = age + FutureYears
print(FutureAge)  # -> 22
```

### Subtraction

```python
print(10 - 5)  # -> 5
```

Example with variables:

```python
CurrentYear = 2025
Age = 17
BirthYear = CurrentYear - Age
print(f"You were born in {BirthYear}")  # -> You were born in 2008
```

### Multiplication

```python
print(10 * 5)  # -> 50
print(f"Ten multiplied by 5 = {10 * 5}")
```

### Division

Python provides different ways to divide numbers:

#### Integer Division (Floor Division)

```python
number = 10
number //= 3  # (This is same as number = number // 3)
print(number)  # -> 3
```

#### Division with Decimals

```python
number = 10
number /= 3  # (This is same as number = number / 3)
print(number)  # -> 3.333333333333
```

#### Modulus (Finding Remainder)

We can use the modulus operator `%` to get the remainder after division. This is useful for checking if a number is even or odd.

```python
number = 10
number %= 3  # (This is same as number = number % 3)
print(number)  # -> 1
```

---

## Exponents (Indices)

In Python, we use `**` for exponentiation.

```python
print(2 ** 4)  # -> 16
print(3 ** 2)  # -> 9
print(9 ** 0.5)  # -> 3.0 (turned into float)
```

---

## Conclusion

This lesson will help you with making the **Calculator Project** after you have completed the lessons. Good luck!

### Next Lesson: `09_concatenation.py`
