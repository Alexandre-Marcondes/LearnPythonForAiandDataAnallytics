# This is a conditional class

x = int(input("what is x? "))
y = int(input("what is y? "))

if x < y:
  print("x is less than y")
if x > y:
  print("x is greater than y")
if x == y:
  print("x is equal to y")


if x < y:
  print("x is less than y")
elif x > y:
  print("x is greater than y")
else:
  print("x is equal to y")
  
# or
if x  < y or x > y:
  print("x is not equal to y")
else:
  print("x is equal to y")


# simpler
if x != y:
  print("x is not equal to y")
else:
  print("x is equal to y")

# And && 
