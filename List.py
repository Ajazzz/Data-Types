## List:
# A list is a collection of items, which can be of different types such as strings, integers, or even other lists. 
# Lists are mutable, meaning you can change their contents.

#Lists are a fundamental data type in Python and have several important use cases:

#Collection of Data:
#Lists are used to store collections of data. They can store a mixture of data types, including strings, numbers, and even other lists. 
#This makes them versatile and useful for a wide range of applications.
#Mutable Data:
#Lists are mutable, meaning you can add, remove, or change their contents after they are created. 
#This makes them useful for situations where you need to modify the contents of a collection over time.

#Iteration and Indexing:
#Lists can be easily iterated over using loops, and individual elements can be accessed using indexing. 
#This makes them useful for situations where you need to perform operations on each element of a collection.

# Data Manipulation:
#Lists can be used to manipulate data by performing operations such as sorting, reversing, and filtering. 
#This makes them useful for data analysis and processing.

# In summary, lists are an important data type in Python because they allow you to store and manipulate collections of data, 
# they are mutable, and they support indexing, iteration, and data manipulation.

#Lists are a commonly used data type in Python, and there are a few common problems that can arise when working with them. 
#Here are some examples of list problems and solutions:

#Adding elements to a list: To add an element to a list, you can use the append() method. For example:

fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits) # Output: ['apple', 'banana', 'cherry', 'orange']


# insert: If we want to add an element at a specific location we need to use insert()
fruits = ['apple', 'banana', 'cherry']
fruits.insert(3,'mango')
print(fruits) # Output: ['apple','banana', 'cherry', 'mango']


#Removing elements from a list: To remove an element from a list, you can use the remove() method. For example:
fruits = ['apple', 'banana', 'cherry']
fruits.remove('banana')
print(fruits) # Output: ['apple', 'cherry']


#Remove an element at a specified index location.
fruits = ['apple', 'banana', 'cherry']
fruits.pop(2)
print(fruits) #Output: ['apple', 'banana']


#Sorting a list: To sort a list in ascending order, you can use the sort() method. For example:
numbers = [3, 5, 1, 4, 2]
numbers.sort()
print(numbers) # Output: [1, 2, 3, 4, 5]


#Reversing a list: To reverse the order of a list, you can use the reverse() method. For example:
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits) # Output: ['cherry', 'banana', 'apple']



#Accessing elements in a list: To access an element in a list, you can use the index of the element within square brackets. For example:
fruits = ['apple', 'banana', 'cherry']
print(fruits[0]) # Output: 'apple'



#Checking if an element is in a list: To check if an element is in a list, you can use the in keyword. For example:
fruits = ['apple', 'banana', 'cherry']
print('banana' in fruits) # Output: True
print('orange' in fruits) # Output: False


# Count() Methode returns the number of specified elements occurance.
fruits = ['apple', 'banana', 'cherry', 'apple']
fruits.count('apple')
print(fruits) # Output: 2


# Index() methode returns the index of the first element.
fruits=['apples','oranges','banana','mangoes','grapes','banana','strawberry']
fruits.index('banana')
print(fruits) # Output: 2


