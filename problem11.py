students = [('Alice', 25), ('Bob', 20), ('Charlie', 23)]

# Sort by age (second element of tuple)
sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)