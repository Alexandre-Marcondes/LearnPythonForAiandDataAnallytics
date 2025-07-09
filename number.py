# try:
#   x = int(input("Enter a number: "))
#   print(f"You entered: {x}")
# except ValueError:
#   print("That's not a valid number!")

# try:
#   x = int(input("Enter a number: "))
# except ValueError:
#   print("That's not a valid number!")
# else:
#   print(f"You entered: {x}")
def main():
  x = get_int()
  x = get_int2()
  print(f"You entered: {x}")



while True:
  try:
    x = int(input("Enter a number: "))
  except ValueError:
    print("That's not a valid number!")
  else:
    break

print(f"You entered: {x}")

## Shorter and the same result using a function
def get_int():
  while True:
    try:
      return int(input("Enter a number: "))
    except ValueError:
      print("That's not a valid number!")

def get_int2():
  while True:
    try:
      return int(input("Enter a number: "))
    except ValueError:
      pass # Ignore the error and continue the loop

main()

