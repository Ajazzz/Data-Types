# A tuple is an ordered collection of items that cannot be modified once created.
# A tuple is similar to a list, but it is immutable, meaning you cannot change its contents once it has been created.

# Tuples are an important data type in Python, and they have several use cases:

#Immutable Data:
#Tuples are immutable, meaning once you create a tuple, you cannot change its contents. 
#This can be useful when you want to ensure that your data remains unchanged throughout your program. 
#For example, if you have a set of constants in your program that should not be changed, you can store them in a tuple.

#Multiple Return Values:
#Functions in Python can return multiple values, which are automatically packed into a tuple. 
#This allows you to easily return multiple values from a function and use them elsewhere in your program.

# Example:

def get_name_and_age():
    name = 'John'
    age = 30
    return name, age

name, age = get_name_and_age()
print(name) # Output: 'John'
print(age) # Output: 30

#Efficient Data Structures:
#Tuples are more memory-efficient than lists because they are smaller in size. 
#This can be useful when you have a large dataset and want to optimize memory usage.

#Sequence Unpacking:
#You can use tuple unpacking to assign the values in a tuple to separate variables. 
#This can be useful when you want to assign multiple values to multiple variables in a single line of code.

#Example:

coordinates = (10, 20)
x, y = coordinates
print(x) # Output: 10
print(y) # Output: 20

#In summary, tuples are important in Python because they provide an immutable data structure, 
#allow for multiple return values, are memory-efficient, and allow for sequence unpacking.




# Creating a tuple
my_tuple = (1, 2, 3)

# Accessing items in a tuple
print(my_tuple[0])  # prints 1

# Iterating over a tuple
for item in my_tuple:
    print(item)
    
numbers = (1, 2, 3)
print(numbers[0]) # Output: 1  
