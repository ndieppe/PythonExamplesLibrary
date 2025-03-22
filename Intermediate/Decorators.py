import time
import random
#Decorator Examples (the last one includes decorator factories and error handling)
#! Example 1:
#* An execution time logger:

def time_logger(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end-start} seconds")
        print(f"Result: {result}")
        return result
    return wrapper

@time_logger
def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

if __name__ == "__main__":
    sum_of_squares(100000)



#* Example 2:
#! Access control
user_role = "admin"  # Change this to "guest" or other roles

def requires_permission(func):
    def wrapper(*args, **kwargs):
        if user_role == "admin": #hard coded requirement
            return func(*args, **kwargs)
        else:
            print("Access Denied: Insufficient Permissions") #never runs delete_user()
    return wrapper

@requires_permission
def delete_user(username):
    print(f"User {username} has been deleted.")

if __name__ == "__main__":
    delete_user("john_doe")

#* Final Example
#! Retry decorator
def retry(max_attempts=5): #this is known as the decorator factory (allowing decorators to accept functions)
    def decorator(func): #this is the decorator function
        def wrapper(*args, **kwargs): #this is the wrapper
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except ValueError as error:
                    attempts += 1
                    print(f"attempt {attempts} failed.")
                if attempts == max_attempts:
                    print(f"Function failed after {max_attempts} due to {error}")
                    raise
                time.sleep(1) #so you can see better the re-attempts
        return wrapper
    return(decorator)


@retry(max_attempts=5)
def unstable_function():
    if random.random() < 0.5:  # 50% chance of failure
        raise ValueError("Random failure occurred!")
    print("Function executed successfully!")

if __name__ == "__main__":
    unstable_function()

