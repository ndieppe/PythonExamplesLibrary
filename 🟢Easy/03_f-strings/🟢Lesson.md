# **F-Strings in Python**

## **What Are F-Strings?**

F-strings (formatted string literals) allow us to insert variables into strings in a more readable and efficient way.

---

## **Using F-Strings vs. Traditional String Concatenation**

In Lesson 2, we wrote:

```python
Age = 19
print("Your age in two years will be:")
print(Age)
```

**Output:**

```
Your age in two years will be:
19
```

With **F-strings**, we can simplify this into a single line:

```python
print(f"Your age in two years will be: {Age}")
```

**Output:**

```
Your age in two years will be: 19
```

---

## **Generating a Username with F-Strings**

Let's create a simple program that generates a username:

```python
FirstName = "Nathan"
LastName = "Dieppe"
Age = 17
print(f"Your new username is {FirstName}_{LastName}{Age}")
```

**Output:**

```
Your new username is Nathan_Dieppe17
```

Now, try modifying the code `03_f-strings.py` to create your own unique username!

---

📌 **Next Lesson:** `04_Inputs` (Introduction to User Input)
