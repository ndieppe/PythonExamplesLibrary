#There is many ways to do collections in python:
#* collection = single "variable" used to store multiple value
#*    list = [] ordered and changeable. Duplicated OK
#*     set = {} unordered and immutable, but ADD/REMOVE OK. NO duplicates
#*   Tuple = () ordered and NOT changeable. Duplicated OK. FASTER  
#*      2D = all arrays in a two Dimension array must be the same length. 


#! Lists:
#lists start 0-indexed, this means the first tiem has a position value of 0
fruits = ["Apple", "banana", "orange"]
print(fruits) #-> ['Apple', 'banana', 'orange'] (prints list)
print(*fruits) #-> Apple, banana orange (prints them without "decoration" by using *)
print(fruits[0]) #-> Apple (this is at 0 index)
print(fruits[0:2]) #-> ['Apple', 'banana'] (prints 0, and 1st index, remeber python doesn't do the last value written)
for x in fruits:
    print(x) #-> prints the fruit on different lines

#* Getting infomation from the lists:
print(len(fruits)) #-> 3 (this is how many items in the list)
print("Apple" in fruits) #-> True (this returns boolean, look at 02_variables if you need reminder on boolean)
print(fruits.index("Apple")) #-> 0
print(fruits.count("banana")) #-> 1 (it is only in the list once)

#* Changing the list
fruits[0] = "pineapple"
print(fruits) #-> ['pineapple', 'banana', 'orange']
fruits.append("apple")
print(fruits) #-> ['pineapple', 'banana', 'orange', 'apple']
fruits.sort()
print(fruits) #-> ['pineapple', 'banana', 'orange', 'apple']
fruits.remove("banana")
print(fruits) #-> ['apple', 'orange', 'pineapple']
fruits.insert(0,"banana")
print(fruits) #-> ['banana', 'apple', 'orange', 'pineapple']
fruits.reverse()
print(fruits) #-> ['pineapple', 'orange', 'apple', 'banana']
fruits.clear()
print(fruits) #-> []


#! Sets
vegs = {"carrot", "spinach", "brocoli", "peas"}
print(vegs) #-> {'carrot', 'spinach', 'peas', 'brocoli'} (gives different order each time)

# to learn more try them yourself, so try with the functions above what works on a tuples (remember defenition of tuple above)

#!Two dimensional lists (we are not going to use this at all for the rest of this section):
#* examples of one dimensional lists:
fruits = ["apple", "banana", "pear", "coconut"]
vegetables = ["carrot", "brocoli", "peas"]
meats = ["chicken", "beef", "Dog"]
print(fruits)
print(vegetables)
print(meats)
#* 2D list:
groceries = [fruits, vegetables, meats]
print(groceries) #-> [['apple', 'banana', 'pear', 'coconut'], ['carrot', 'brocoli', 'peas'], ['chicken', 'beef', 'Dog']]
print(groceries[0]) #-> ['apple', 'banana', 'pear', 'coconut']
print(groceries[2][2]) #-> Dog