def highest_even(li):
  highest = 0
  even_high = []
  for even in li:
    if even % 2 == 0:
      highest = even
      even_high.append(highest)
      for high in even_high:
        if high > highest:
          highest = high
  return print(highest)        


highest_even([10, 2, 3, 4, 18, 11, 4])
# _______________________________________ #
# _______________________________________ #
# _Refactored code from above using max__ #

def highest_even_better(li):
  evens = []
  for even in li:
    if even % 2 == 0:
      evens.append(even)
  return print(max(evens))

highest_even_better([10, 2, 3, 4, 18, 11, 4])
