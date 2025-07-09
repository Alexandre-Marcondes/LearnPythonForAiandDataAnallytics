# *args and **kwargs
# IMPORTANT Rule for params
# RULE: params, *args, default parameters, **kwargs

def super_func(*args):
  print(*args) # this prints all the arguments pass by the function
  print(args) # this creates a tupple of the arguments
  return print(sum(args))

super_func(1,2,3,4,5,6) # output should be 1 2 3 4 5 6 and 21

## **kwargs

def fun_func(*args, **kwargs):
 # print(**kwargs) # CANNOT print the **kwargs should use below
  print(kwargs) # print the the key value pair
  total = 0
  for items in kwargs.values():
    total += items
  return sum(args) + total

print(fun_func(1,2,3,4,5, num1=5, num2=10, num3=15))