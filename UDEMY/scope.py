# Scope = what variables do I have access to?
# block scope
# Rules
# 1 - start with local
# 2 - parent local scope
# 3 - Global -whatever the file has
# 4 - built in python functions

# Pure Function
# 1 - give the same input will always return the same output
# 2 - a function should not produce any side affect <no print inside functions>
# PURE FUNCTION SAMPLE

# this is a self contained function obeys the rules above
# the print is not inside the function 
# the new_list variable is not global 

def multiply_by2(li):
  new_list = []
  for item in li:
    new_list.append(item * 2)
  return new_list

print(multiply_by2([1,2,3]))  
