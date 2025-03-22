#loops
#* In python there is two ways to do a loop
# A count controlled loop, is when the amount of repetitions is decided by a number, in python we use the for loop
# A condition controlled loop, this is when the amount of repetitions is decided by a condition, in python we use the while loop

#* For loops
for x in range(6): #? Note: this means all the values bettwen (0-5)
    print(x) #-> This outputs 0 to 5

for x in range(1,11): #this means it starts at 1 and ends at 10
    print(x, end= " ") #->1 2 3 4 5 6 7 8 9 10
#using end= " " we can prevent a new line being formed

#* While loop
#last lesson we built this program:
password = "Password7" 
user_input = input("Please enter the password: ")
if user_input == password: 
    print("Welcome!")
else: 
    print("Password was incorrect")

#* Now let's rebuild it with a while loop so as to allow re-attempts:
password = "Password7" 
user_input = input("Please enter the password: ")
while user_input != password: # "!=" means not equal to, this while loop we continue until they get the password right
    print("Password was incorrect, please try again: ")
    user_input = input("Please enter the password: ") #here they get to re-enter the password
    
print("Welcome!") #This will only run if they manage to get password right



#*Now let's rebuild the program but with max attempts of 5:
password = "Password7"
user_input = input("Please enter the password: ")
attempts = 1     #                    "<" means less than or equal to
while user_input != password and attempts < 5: #the "and" statement means that user != password, as well as attempts <= to 5
    print("Password was incorrect, please try again: ")
    user_input = input("Please enter the password: ")
    attempts += 1 #adds 1 to the input
#at this point they could have got out of the while statement through either getting it right or by having too many attempts so we must check:
if user_input != password:
    print("Failed to enter")
else:
    print("Welcome") 
