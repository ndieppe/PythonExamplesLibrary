#maths or math (it is definitely called maths)
import math #this is importing code someone else made to help us program

print(math.pi) #-> 3.141592653589793
print(math.e) #-> 2.718281828459045

#for the rest of this lesson we won't use the math module

#! addition
print(5+10) #-> 15
age = 17
FutureYears = 5
FutureAge = age + FutureYears
print(FutureAge) #-> 12

#Above can be done on all other operators:
#! Subtraction
print(10-5) #-> 5
CurrentYear = 2025
Age = 17
BirthYear = CurrentYear - Age
print(f"You were born in {BirthYear}") #-> You were born in 2008

#! Multiplication
print(10*5) #-> 50
print(f"ten multiplied by 5 = {10*5}")


#! Division:

#* integer division:
number = 10
number //= 3 #(This is same as number = number // 3)
print(number) #-> 3

#* division with decimal numbers:
number = 10
number /= 3 #(This is same as number = number / 3)
print(number) #-> 3.333333333333

#* get remainder(MOD) (can be used to find if even or odd):
number = 10
number %= 3 #(This is same as number = number % 3)
print(number) #-> 1

#!Indicies
print(2**4) #->16
print(3**2) #->9
print(9**0.5) #->3.0 (turned into float)