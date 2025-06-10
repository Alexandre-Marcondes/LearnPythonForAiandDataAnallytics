def main():
  x = int(input("What's x? "))
  if isEven(x):
    print("Even")
  else:
    print("Odd")

def isEven(y):
    if y % 2 == 0:
      return True
    else:
      return False
    
main()

# pythonic way of the above function
# the return would look like this 
""" 
return True if n % 2 == 0 else False
"""
# even smaller 
""" 
return n % 2 == 0
"""
