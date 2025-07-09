some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]
duplicates = []
for leter in some_list:
    c = some_list.count(leter)
    if c > 1:
      if leter not in duplicates:
        duplicates.append(leter)
print(duplicates)  