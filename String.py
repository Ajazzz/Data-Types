


########
#Print the length of a string.

string = "Hello, world!"
print(len(string))

#######

#Count the number of occurrences of a substring in a string.

string = "Hello, world!"
substring = "l"
print(string.count(substring))

#######
#Convert a string to uppercase.

string = "Hello, world!"
print(string.upper())

#######

#Convert a string to lowercase.

string = "Hello, world!"
print(string.lower())

###########
#Replace all occurrences of a substring with another substring.

string = "Hello, world!"
substring = "l"
replacement = "x"
print(string.replace(substring, replacement))

#############

Split a string into a list of substrings.

string = "Hello, world!"
print(string.split())

###########

Join a list of substrings into a single string.

list_of_strings = ["Hello", "world", "!"]
delimiter = " "
print(delimiter.join(list_of_strings))

###########

Check if a string starts with a specific substring.

string = "Hello, world!"
substring = "H"
print(string.startswith(substring))

###########

Check if a string ends with a specific substring.

string = "Hello, world!"
substring = "d!"
print(string.endswith(substring))

###########

Reverse a string.

string = "Hello, world!"
print(string[::-1])

##########

Check if a string is a palindrome.

string = "racecar"
print(string == string[::-1])

###########

Remove all whitespace characters from a string.

string = "Hello,   world!  "
print(string.replace(" ", ""))

##############
Find the first occurrence of a substring in a string.

string = "Hello, world!"
substring = "world"
print(string.find(substring))

##########

Check if a string contains only alphanumeric characters.

string = "Hello123"
print(string.isalnum())

############
Check if a string contains only alphabetical characters.

string = "Hello"
print(string.isalpha())

##########

Use of a for loop to iterate over the characters in a string

my_string = "hello"
for character in my_string:
    print(character)
    
 
##############

Use of a for loop to iterate over a range of indices and access each character using indexing. 
Here is an example:

my_string = "hello"
for i in range(len(my_string)):
    print(my_string[i])

#########

String concatenation

String concatenation is the process of combining two or more strings together to create a single, longer string. 
In Python, you can use the + operator to concatenate strings. Here is an example:

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)


Example 2:

message = "Hello"
message += " world!"
print(message)

##########
Built-in string methods:

#upper(): Returns a string in all uppercase letters.
my_string = "hello"
print(my_string.upper())  # Output: "HELLO"

#lower(): Returns a string in all lowercase letters.
my_string = "Hello"
print(my_string.lower())  # Output: "hello"

# strip(): Removes leading and trailing whitespace from a string.
my_string = "   hello   "
print(my_string.strip())  # Output: "hello"

# split(): Splits a string into a list of substrings based on a delimiter.
my_string = "hello world"
print(my_string.split())  # Output: ["hello", "world"]

# replace(): Replaces all occurrences of a substring with another substring.
my_string = "hello world"
print(my_string.replace("world", "Python"))  # Output: "hello Python"

# find(): Returns the index of the first occurrence of a substring in a string, or -1 if the substring is not found.
my_string = "hello world"
print(my_string.find("world"))  # Output: 6


# count(): Returns the number of occurrences of a substring in a string.
my_string = "hello world"
print(my_string.count("l"))  # Output: 3











These are just a few examples of Python string problems.
There are many more ways to manipulate and work with strings in Python!

