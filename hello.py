# docs.python.org/3/library/function/print

name = input("what is your name? ")

#remove whitespace from str
# strip() is a str method
name = name.strip()

#Capitalization 
# capitalize is a str method 
name = name.capitalize()

#if name and last name title can help
name = name.title() # output Alex Marcondes

#chaning add many methods
name = name.strip().title() #As above but done in the same line

#It can be done when getting the imput like so
name = input("what is your name? ").strip().title()

# Split user's name into first name and last name

first, last = name.split(" ")

# all the same
print("hello there", name)
print("hello there "  + name)
print("hello there", first)

# "f" formats the string using the variable inside the quotes
print(f"hello there {name}")

# str = string type of data 
# when you pass values = parameters

# def = define it creates define a function

def hello(to): 
  print(f"Hello, {to}")

name = input("What is your name? ")
hello(name)


def hello(to="word"): 
  print(f"Hello, {to}")

name = input("What is your name? ")
hello()


# !IMPORTANT THE DEFINE MAIN CONVENTION 
"""+++++++++++++++++++++++++++++++++++++++"""
def main():
  name = input("What is your name? ")
  hello(name)

def hello(to="world"):
  print(f"Hello, {to}")  

main()
"""+++++++++++++++++++++++++++++++++++++++"""
# The above convetion to keep your code clear
# and not having to define all functions up top
# Create a main function

