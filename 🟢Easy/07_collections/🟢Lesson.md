# Introduction to Collections in Python

## What are Collections?

In Python, collections allow us to store multiple values in a single variable. There are different types of collections, each with its own properties:

- **List (`[]`)** - Ordered, changeable, allows duplicates.
- **Set (`{}`)** - Unordered, immutable (but can add/remove items), no duplicates.
- **Tuple (`()`)** - Ordered, immutable, allows duplicates, faster than lists.
- **2D Lists** - Lists of lists, where each internal list must be of the same length.

---

## Lists

Lists are **0-indexed**, meaning the first item is at position `0`.

```python
fruits = ["Apple", "banana", "orange"]
print(fruits)  # ['Apple', 'banana', 'orange']
print(*fruits)  # Apple banana orange
print(fruits[0])  # Apple
print(fruits[0:2])  # ['Apple', 'banana']

for x in fruits:
    print(x)  # Prints each fruit on a new line
```

### Getting Information from Lists

```python
print(len(fruits))  # 3 (Number of items in the list)
print("Apple" in fruits)  # True (Boolean check for existence)
print(fruits.index("Apple"))  # 0 (Index of "Apple")
print(fruits.count("banana"))  # 1 (Count occurrences of "banana")
```

### Modifying Lists

```python
fruits[0] = "pineapple"
print(fruits)  # ['pineapple', 'banana', 'orange']

fruits.append("apple")
print(fruits)  # ['pineapple', 'banana', 'orange', 'apple']

fruits.sort()
print(fruits)  # ['apple', 'banana', 'orange', 'pineapple']

fruits.remove("banana")
print(fruits)  # ['apple', 'orange', 'pineapple']

fruits.insert(0, "banana")
print(fruits)  # ['banana', 'apple', 'orange', 'pineapple']

fruits.reverse()
print(fruits)  # ['pineapple', 'orange', 'apple', 'banana']

fruits.clear()
print(fruits)  # [] (Empty list)
```

---

## Sets

Sets are **unordered** and **do not allow duplicate values**.

```python
vegs = {"carrot", "spinach", "broccoli", "peas"}
print(vegs)  # Output order may vary
```

Try applying list functions to sets and see what works!

---

## Two-Dimensional Lists

### One-Dimensional Lists:

```python
fruits = ["apple", "banana", "pear", "coconut"]
vegetables = ["carrot", "broccoli", "peas"]
meats = ["chicken", "beef", "pork"]
```

### 2D List:

```python
groceries = [fruits, vegetables, meats]
print(groceries)  # [['apple', 'banana', 'pear', 'coconut'], ['carrot', 'broccoli', 'peas'], ['chicken', 'beef', 'pork']]
print(groceries[0])  # ['apple', 'banana', 'pear', 'coconut']
print(groceries[2][2])  # pork
```

2D lists are useful, but we won’t be using them much in this section.

---

### Next Lesson: **`08_maths`**
