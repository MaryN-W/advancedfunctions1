# Higher-order functions -> contains other functions as a parameter or returns a function as an output
#hof - wrapper - wraps a function in some additional functionality which may take place before the original
# function is called or after its called

# numbers = [5, 9, 5, 8, 9]

# a function to square the numbers
# def squares(nums):
#     result = [] # Create an empty list to store squared values
#     for n in nums: # Loop through each number in nums
#         result.append(n ** 2) # Each number n is squared (n ** 2) and added to the result list

#     return result # Return the list of squared numbers

# print(squares(numbers)) # Calling the Function (squares(numbers)) -> The list numbers = [5, 9, 5, 8, 9] is passed to squares(), then
# # printing the result


# numbers = [5, 7, 2, 3]

# # Builds a new list with the result of
# # calling cb on each item in the list
# # higher-order functions and callbacks

# def with_list(nums, cb): # with_list(nums, cb) is a higher-order function because it takes another function (cb) as an argument
#     result = []
#     for n in nums:
#         result.append(cb(n)) # cb(n) is a callback function that is applied to each element in nums
# # A callback function is a function that is passed as an argument to 
# # another function and is “called back” at some convenient time
#     return result

# def square(n):
#     return n * n # square(n) takes a number and raises it to the power of itself (n^n)

# def cube(n):
#     return n ** 3 # cube(n) takes a number and raises it to the power of 3 (n³)

# # Main
# print(with_list(numbers, cube)) # numbers is passed as the list of numbers
# # square is passed as the callback function (cb)
# # The function applies square(n) to each number in numbers and returns the modified list

# my not so readable code example how callback functions work above replica
# turns out its such a common thing to do that this function is built-in, its called 
# map (where we have with_list) and order of parameters in (numbers, square) is function first, then the iterable (cube, numbers)
numbers = [5, 7, 2, 3] # this can be strings etc

# def my_numbers(nos, understand):
#     result = []
#     for d in nos:
#         result.append(understand(d))

#     return result

# def square(d):
#     return d * d

# def cube(d):
#     return d ** 3

# # print(my_numbers(numbers, cube))
print(list(map(lambda x: x ** 2, numbers))) # Instead of pre-defined function you can pass a lambda instead for same results, and map the built-in func

evens = filter(lambda x: x % 2 == 0, numbers) # filter even numbers output 2, the only even in the list
# Lambda function -> If x is even, it returns True, meaning the number will be included in evens.
# If x is odd, it returns False, so the number will be excluded
# filter() does not return a list directly. It returns a filter object (iterator).
# To see the results, you need to convert it into a list
# in python, 2 != [2], the latter is a list that happens to contain an integer, so filter as above
print(list(evens))

# Same filtering logic using a regular function with filter()
# def is_even(x):
#     return x % 2 == 0

# numbers = [5, 7, 2, 3]

# # Use filter() with the is_even function
# evens = filter(is_even, numbers)

# # Convert to list to see the result
# print(list(evens))  # Output: [10, 2, 4]