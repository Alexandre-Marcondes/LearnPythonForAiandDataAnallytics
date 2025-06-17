### While loops

# i = 0

# while i < 3:
#   print("meow")
#   i += 1

### list is a data type.
### list of things in the real word or array.

for i in [0,1,2]:
  print(i)

for i in range(3):
  print("meow")

# pythonic way a "_" is a variable that you don't need to use just use "_"
for _ in range(9):
  print("meow")

## the "end" changes the behavior of the print function to scape the last new line 
print("meow\n" * 3, end="")

while True:
  n = int(input("What is n? " ))
  if n < 0:
    continue
  else:
    break


for _ in range(n):
  print("meow")

#### better way less lines 
while True:
  n = int(input("What is n? " ))
  if n > 0:
      break

for _ in range(n):
  print("meow")

