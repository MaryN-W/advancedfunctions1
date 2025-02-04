# Lambda
# A one line, small anonymous function.
# Can take any number of arguments, but can only have one expression.
# Mainly used for short simple functions that you don’t need to define with def.

def add_ten(num):
    return num + 10 # the expression num + 10 can be as complicated as you want as long its a single expression e.g ternary, boolean 


add_ten_lambda = lambda num: num + 10 # we can assign a 
# lambda func into a var like any other var # return keyword not required, the body of lambda automatically return results
# put a lambda into a var to call it just like any other function

# print(add_ten(5))
print(add_ten_lambda(5))