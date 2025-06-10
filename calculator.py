# int is a datatype as well as a function. 

x = int(input("what's your number? "))
y = int(input("what's your number to add? "))
print(x + y)

# float is a number with a decimal point <floating value>

x = float(input("what's your number? "))
y = float(input("what's your number to add? "))
z = round(x + y)


# specified that we want to format the number with 1,000
#using f + ":,"
print(f"{z:,}")

z = x / y

# using f and ".2f to get only 2 decimals in a float "
# the above division sample 2/3 = 0.66666666666 using the below format 0.67
print(f"{z:.2f}")

# The RETURN value
"""+++++++++++++++++++++++++++++++++++++++"""
def main():
  x = int(input("What is your x? "))
  print(f"x square is {square(x)}")
  print(f"x cube is {cube(x)}")


def square(n):
  return(n * n)  

# another way is to the power = pow
# def square(n)
 #return pow(n, 2) or any power like cube(3)

def cube(n):
  return pow(n, 3)

main()
"""+++++++++++++++++++++++++++++++++++++++"""
