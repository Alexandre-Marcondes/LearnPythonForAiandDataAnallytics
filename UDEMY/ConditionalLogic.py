# Ternary Operator
# shortcut
# conditional expression
condition = False

# condition_if_true if condition else condition_if_false

is_friend = True
print("evaluating is_friend with true")
print("using ternary operators")
print("such as")
print("if he is friend say hello IF contition (is_friend = True) else Nothing happen cause is TRUE")
print("Hello") if is_friend else print("no Friend")
print("evaluating is_friend with false")
is_friend = False
print("if he is friend say hello IF contition (is_friend = False) else This will happen to say no Friend")
print("Hello") if is_friend else print("no Friend")

print("_____________________________")
print("_____________EXERCISE ________________")
is_magician = False
is_expert = True

if is_magician and is_expert:
  print("You are a master magician")
elif is_magician or is_expert:
  print("at least you're getting there")
elif not(is_magician):
  print("You need magic powers")
else:
  print("this is likely to hit")

print("Outside the if elif statement")
print("_____________________________")
print("_____________EXERCISE  Picture________________")

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for row in picture:
  for pixel in row:
    if pixel == 1:
      print("*", end='')
    else: 
      print(" ", end='')
  print()

#### IMPORTANT ########
 ## Code Convention
  # Clean
  # Readability
  # Predicability
  # Do not repeat yourself (DRY)

# Above code reformated with clean code
print("_____________________________")
fill = "*"
empty = " "
for row in picture:
  for pixel in row:
    if pixel: # no need to check for 1 because is either True = 1 or False = 0
      print(fill, end='')
    else: 
      print(empty, end='')
  print()
