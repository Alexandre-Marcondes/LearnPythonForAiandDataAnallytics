# Functions
# Pure Function
# 1 - give the same input will always return the same output
# 2 - a function should not produce any side affect <no print inside functions>
# PURE FUNCTION SAMPLE

# this is a self contained function obeys the rules above
# the print is not inside the function 
# the new_list variable is not global 
li = [1,2,3,4]
def multiply_by2(li):
  new_list = []
  for item in li:
    new_list.append(item * 2)
  return new_list

print(multiply_by2([1,2,3]))  

print("#________________________#")

# define = def

def say_hello():
  print("hello")

say_hello()

# Arguments Vs parameters

# parameters is what you use to define the functions
def say_hello(parameters):
  print("hello")

# arguments values we provide to a function
say_hello('arguments')

# default parameters
def say_hello(name="Vader", emoji=":)"):
  print(f"hello {name}, {emoji}")

# when you call a function without an argument the function will use the defaul parameters.
say_hello()

print("#####################")
# Return

def sum(num1, num2):
  total = num1 + num2
  return print(total) # use return to show the print where the function is been called

sum(5,9)
print("#####################")
print("#####################")
print("#___Map, filter, zip, reduce_____________________#")
### 
### map, filter, zip, and reduce
print("#________________________#")
print(multiply_by2([1,2,3]))  
print("#####################")

def multiply_by2(item):
  return item * 2

print("#____ Here since we are passing a list ____________________#")
print("# ____the function does not do math on list so it repeates the list as many times____")
print( "# ____ as it is been multiplied ___ ")
print(multiply_by2([1,2,3]))  
print("#####################")
print("#####################")

print("#____________MAP____________#")
print(list(map(multiply_by2, li)))


print("#____________FILTER____________#")

# filtering some of the results.
def only_odd(item):
  return item % 2 != 0

print(list(filter(only_odd, li)))
print("#####################")
print("#####################")

print("#____________ZIP____________#")
# zip needs two item to zip them together
# needs 2 lists
my_list = li
your_list = [10, 20, 30, 40, 50]

print(list(zip(my_list, your_list)))
print(li)
print(my_list)
print(your_list)

new_zipped = list(zip(my_list, your_list))
print(new_zipped)
print("#####################")

print("#____________REDUCE____________#")
def accumulator(acc, item):
  print(f"acc = {acc} , and item = {item}")
  return acc + item

from functools import reduce # reduce is one of those tools it has to be imported from functools

print(li)
reduced_num = reduce(accumulator, li, 0)
print(reduced_num)

print("#####################")

print("#____________Comprehension____________#")
print(" comprehensions is the same for list and set")
print(" for list use list = [instructions loop here]")
print(" for set use set = {instructions loop here }")

print("#______list______Comprehension____________#")

my_char_list = [char for char in "hello world"]
print(my_char_list)

my_nums2 = [num for num in range(0, 11)]
print(my_nums2)

my_doubles_of_nums2 = [num for num in map(multiply_by2, range(0, 11))]
print(my_doubles_of_nums2)

print("#########SAME RESULT BELOW ############")
print("but the variable can be an expression like num * 2")
print(''' So all these can be
my_doubles_of_nums2 = [num for num in map(multiply_by2, range(0, 11))]
print(my_doubles_of_nums2)
      
 ''')
print(''' Just this:
      ## my_list3 = [num * 2 for num in range(0, 11)]
      # resulting on this:
      #  ''')
my_list3 = [num * 2 for num in range(0, 11)]
print(my_list3)

my_list4 = [num * 2 for num in range(0, 11) if num % 2 == 0]
print(my_list4)

my_test_case = [
  num * 50 for num in range(1,101) if num > 89
  ] # the if first and if that condition works then apply the multiplication

print(my_test_case)
print("#####################")
print("#####################")

print("#______DICTIONARY______Comprehension____________#")
#needs a dict to start
simple_dict = { "a": 1, "b": 2, "c": 3 }

my_dict = {key: value**2 for key, value in simple_dict.items() } 
print(my_dict)

# can also use if
my_dict2 = {key: value**2 for key, value in simple_dict.items() if value % 2 !=0 } 
print(my_dict2)

print("#####################")
print("#####################")
print("____ NESTING _____")
print('''
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
''')

some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)

print("#####################")