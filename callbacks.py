# Callbacks are functions that are passed to another function as an argument and executed later # a function calling another function
# Executed after the main function completes its task
# Separation of concerns -> main function (greet) doesn’t need to know what cb does

# importing modules only when we need them, avoid slowing down the intepreter 
# Module -> a file containing Python code (functions, classes, or variables) that can be reused in other programs

import time # standard python library module

def greet(name, cb): # function takes two parameters, cb -> a function that will be called inside greet -> arbitrary 
    print(f'Hello, {name}') # calls say_bye() which prints 'Bye!!'
    # time.sleep(3) # sleep function from import time module # delays execution for a given no of secs # delays "continuing main" by 3 secs
    cb() # -> Executes say_bye()   

def say_bye():
    print('Bye!!')

def shout():
    for i in range(5):
        print('How is Python?!')

# Main
greet('Wangari', say_bye) # calling greet with a callback # cb = say_bye
greet('Tabitha', shout) # You can pass in a different function every time you call greet that does something different when greet finishes
    

print('Contuining main ...') # Executes as greet() completes

# # Fetching user data from a database and want a notification once it's done
# def fetch_data(user, callback):
#     print(f'Fetching data for {user}...')
#     callback()

# def notify():
#     print('Data retrieved successfully!')

# fetch_data('Alice', notify)

