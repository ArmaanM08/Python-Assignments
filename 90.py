people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30}
]

# Sort by age
sorted_people = sorted(people, key=lambda person: person["age"])

print(sorted_people)

[{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}]

sorted_people_desc = sorted(people, key=lambda person: person["age"], reverse=True)
print(sorted_people_desc)