# Teaching python
# data types
#Fundamentyal data typs
int 
float
bool
str
list
tuple
set
dict
None # the absence of values
complex # is a type for number is equivalent to a real number



# Classes -> custom types

# Speialized Data Types
# packages and Modules or extensions

type(9) # output <class "int"

#math functions
# round (num, ) 
print(round(3.5))
print(abs(-20))

# Don't read the dictionary

# Operator precedence
# _____________
#()
# **
# * and /
# + and - 
#______________
print((5 + 4) * 10 / 2)
print(f"guess: = 45")

print(((5 + 4) * 10) / 2)
print(f"guess: = 45")

print((5 + 4) * (10 / 2))
print(f"guess: = 45")

print(5 + (4 * 10) / 2)
print(f"guess: = 25")

print(5 + 4 * 10 // 2)
print(f"guess: = 25")

print("_______________________")

# VARIABLES RULES
# snake_case
# Start with lowercase or underscore
# Letters, numbers, underscores
# Case sensitive
# Don't overwrite keywords.

# CONSTANTS
# they are usually in CAPITAL case
PI = 3.14

# expressions = a piece of code that produces a value
user_age = 100 / 2 # where 100 / 2 is the expression

# Stetament = a entire line of code
user_age = 100 / 2 # where "user_age = 100 / 2" is the statement

# augmented assignment operator
some_value = 5
some_value += 2 # output is 7 

#Strings = str
"hello word" #is a type of string
print(type("Hello word"))

print("_______________________")

# ''' three single quotes to multiline strings. '''
print(
'''
|||
O o
(__)
'''
)

print("_______________________")

# string concatenation
print("hello" + " There")

#type Conversion

# escape Sequence
# "\" just the next character
weather = "It\'s \"kind of \" sunny \"sunny"
print(weather)

# "\t" Creates a tab space
weather = "\t It\'s \"kind of \" sunny \"sunny"
print(weather)

# "\n" Creates a new line
weather = "\t It\'s \"kind of \n sunny"
print(weather)

# Formatted Strings
name = "Alex"
age = 55
print(f"Hello {name} you are {age} years old")

#older formate of the above string
print('Hello {}. You are {} years old'.format(name, age))


# String manipulation
# [start: stop] start is inclusive and stop exclusive
print("_______________________")
selfish = '01234567'
print(selfish[0:2]) # output 01

# [start: stop; stepover]
print("_______________________")
print("stepover using 2")
selfish = '01234567'
print(selfish[0:8:2]) # output 0246

print("_______________________")

# !IMPORTANT 
# Using string manipulation to reverse the string 
print("_______________________")
print("reverse")
print("[::-1] syntex to reverse the string")
selfish = '01234567'
print(selfish[::-1]) # output 0246

print("_______________________")

# Immutability = string cannot be change
# the idea that you can chnge the string 
# but you cannot change an index of the string

print("If the string: variable = 123")
print("You cannot change variable[2] = 0 ")
print("This above is an error")
print("if you do variable = 0")
print("the above is good but now variable is just 0 and not 123")

print("_______________________")


## len()
# String Methods

print("# the .len() example")
variable = "Hello"
print("In a variable we have the 'hello' string")
print("using variable.len() we get")
print(len(variable))

print("# lets learn string methods")
print("# W3 schools good resource")
quote = "to be or not to be"
print('method: upper')
print("quote.upper()")
print(quote.upper())
print("_______________________")

print('method: capitalize')
print("quote.capitalize()")
print(quote.capitalize())

print("_______________________")

print('method: title')
print("quote.title()")
print(quote.title())

print("_______________________")

print('method: replace (replace, changer)')
print("quote.replace('be', me)")
new_quote = print(quote.replace('be', 'me'))

print(new_quote)

# booleans
# can be True or False
# is_cool

print("Boolean is_true: True or False")
print("1 is True and 0 is False")


print("_______________________")


# little test script in python
# make password (******)
# give length
# greet
print("_______________________")
print("_______________________")


name = input("Enter Name: ")
password = input("Enter password: ")
size = len(password)
newpass = password.replace(password, "*" * size)

print(f"Hello, {name}, your password {newpass} is {size} characters long")


print("_______________________")
print("_______________________")

# list and LISTS 
# LISTS are mutable. unlike strings list can be changed with index[0] = something new
# Data Structure
li = ["alex", "Jon", "Dave"]
li2 = li[0:2]

# list Slicing
# With list slicing we are creating a new copy of the list
# The list itself won't change
# Slicing does create a new copy of the list 
print(f"li = {li}")
print(f"We slice li like so: li2 = li[0:2] so just {li[0:2]}")
print(f"Then the li2 = : {li2} and \n li = : {li}")
print("Slicing works in list the same as strings")
print(li[::2]) #output should be ["alex", "Dave"]
print(f"Here it it: {li[::2]}")

#!!! IMPORTANT !!!
# to make a copy of the list use [:]
# other wise if this is the case:
# li2 = li this is a pointer to the list and if "li2" gets change so will "li"
# if
# li2 = li[:] now li2 is a copy of "li" but changes to li2 will not change li
print("_______________________")
print("________MATRIX_______________")

# Matrix is a way to describ a 2 dimensional list

matrix = [
  [1,2,3],
  [2,4,6],
  [7,11,13]
]
print("________MATRIX_______________")
print(f"Matix equal to: {matrix}")

print(f"Accessing the number 4 of the above")
print(f''' looks like this:
      matrix[1][1]: {matrix[1][1]}
      number: 4 = matrix[1][1]: {matrix[1][1]}
 ''')
print("________MATRIX_______________")

print("Actions on lists")
print("len()")
print(f"len of list matrix is: {len(matrix)}")
print(f"list methods append() = adding") #it does not produce a result 
print(f"So matrix.append([20,21,22]): {matrix.append([20,21,22]) }") 
print(f"now the list is: {matrix}") 

# !!!! IMPORTANT !!!
# if you assign append() you don't get a result it only changes the list
# so below the assignment the variable would be None
# variable = matrix.append([30, 31, 35])
# variable is None and matrix has the appended list [30, 31, 35]

print('''
# !!!! IMPORTANT !!!
# if you assign append() you don't get a result it only changes the list
# so below the assignment the variable would be None
# variable = matrix.append([30, 31, 35])
# variable is None and matrix has the appended list [30, 31, 35]
''')
variable = matrix.append([30, 31, 35])
print(" we did these in code line above variable = matrix.append([30, 31, 35])")
print(f"This is variable: {variable} right after")
print(f"and here is the matrix: {matrix}")

print("insert() gets and index and a object value")
print("Like this matrix.insert(1, [0,0,0])")

matrix.insert(1, [0,0,0])
print(f" the above will create a new matrix like so: {matrix}")
print("But can't be assigned works like append()")

print("List removing = pop()")
print(f"matix.pop() removes the last list of number")
matrix.pop()
print(f"so using pop this is what the list looks like {matrix}")
print(f"pop(1) using index remove the 2nd item in the list")


print("_______________________")
print("REVOVE = remove()")
print("remove() takes a value and removes from the list")
print(f"So remove([0,0,0]) is used to remove that value from the list")
matrix.remove([0,0,0])
print(f"After using remove([0,0,0])")
print(f"Matrix: {matrix}")
print("_______________________")

print("Clear = clear() empties the entire list")

print("index(Value to look for, start, end)")
print(f"matrix.index([7,11,13]) equal output: {matrix.index([7,11,13])}") #output 2

#keywords
# in use for finding 
# "x" in letters

# count

print("sort places in alphabetic order")
print("sorted makes a copy of the list and alphabetic order muttable")
print("copy just makes a copy but does not sort")
print("reverse() it reverses the list")
print("range(starts, stop)") #get range(1, 100)
print(range(1,100))

print("using range with list ")
print("Creates a list that size. ")
print("list(range(1,100))")
print("OUTPUT THE ABOVE")
print(list(range(1, 100)))

print("_______________________")
alphabet = ["a", "b", "c", "d", "e"]
print(".join()")
print("use a empty string like below")
print(" ' '.join([list here]) ")
print(f"output of alphabet:  {' '.join(alphabet) }")

print("_______________________")

#list unpacking
print("List unpacking")
print("when you have a list")
print(" list = [apple, corn, orange ]")
print(" use unpack to get a variable to each item in the list or tupple")
print("a, b, c = list ")
print("output:")
slist = ["apple", "corn", "orange"]
a, b, c = slist
print(a)
print(b)
print(c)


print("_______________________")

print("Using the *other ")
print("a, *other = list")
a, *other = slist
print(f" a: {a}")
print(f"*other: {other}")


print("_______________________")

# !important None
print("None is the absence of a value")
print("print(None) produces the value below: ")
print(None)


print("_______________________")
print("dict as in dictionary")
# Dictionary
# in other language might be called a hash table, map table, objects.
# dict -  data type as well as a data structure
# Key Value types
print(''' Here is a sample dict:
dictionary = {
      'a': 1,
      'b': 2,
      'c': "car"
      'Key': "Value" 
}
''')
dictionary = {
  'a' : 1,
  'b' : 2,
  'c' : "car",
  'Key': "Value"
} 
print("whole dictionaty using") 
print("print(dictionary)")  
print(dictionary)
print("just the keys need use for loop")
print(" for d in dictionary: print(d)")
for d in dictionary:
  print(d)
print("_______________________")
print(dictionary)
print("to print the value need to use a for loop")
print(" for d in dictionary: print(dictionary[d])")
for d in dictionary:
  print(dictionary[d])
print("_______________________")

# Understanding data structures
print("understanding Data Structure")

print("_______________________")
print(" the get mehtod on dict ")
print(" use like so: user.get('key', replacement if not exists)")
print(f"Our dictionary now: {dictionary} ")
print("using .get() like so dictionary.get('d','new thing')")
print(dictionary.get('d', "new thing"))
print("is it muttable: ")
print("Does it updatate dictionary ")
print("Dictionary now:")
print(dictionary)
print("dictionary2 = dictionary.get('d', 'new thing')")
dictionary2 = dictionary.get('d', 'new thing')
print(dictionary2)

print("_______________________")

# tuple
# tupples are immutable lists
print('tupples are immutable lists')
my_tuple = (1,2,3,4,5)

# set
# set 
print('sets are unordered collections of unique items ')
my_set = {1, 2, 3, 4, 5, 5, 2}
print("my_set looks like this: my_set = {1, 2, 3, 4, 5, 5, 2} ")
print("but printing my_set get us this:")
print(f" only returs the values that are unique ${my_set}")
