### LIST and list

students = ["Hermione", "Harry", "Ron", "Draco"]
for student in students:
    print(student)

houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
## len for length

for i in range(len(students)):
    print(i, students[i])

## dict for dictionary word and definition = Key Values pairs
## a dict is 2 dementional {}

students = [
  {"name": "Hermione",
  "house": "Gryffindor",
  "patronus": "Otter"
  },
  {"name": "Harry", 
  "house": "Gryffindor",
  "patronus": "Stag"
  },
  {"name": "Ron",
  "house": "Gryffindor", 
  "patronus": "Jack Russell Terrier"
  },
  {"name": "Draco",
  "house": "Slythering",
  "patronus": None
  }
]
  

for student in students:
  print(student["name"], student["house"], student["patronus"], sep=", ")