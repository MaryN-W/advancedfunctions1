

def greet(name, cb):  
    print(f'Hello, {name}') 
    cb()

# def say_bye():
#     print('Bye!!')

# say_bye = lambda: print('Bye!!') # Changing say_bye into a lambda

# Main

# greet('Wangari', say_bye)
greet('Wangari', lambda: print('Bye!!')) # # passing and declaring a lambda at the same time instead of creating the var say_bye = lambda: print('Bye!!') above




