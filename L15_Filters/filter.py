grades = ['A', 'B', 'F', 'C', 'F', 'A']


# filter way
def remove_fails(grade):
    return grade is not 'F'


filtered_grades = list(filter(remove_fails, grades))

print(filtered_grades)

# simple for method
filtered_grades_simple_for = []
for grade in grades:
    if grade is not 'F':
        filtered_grades_simple_for.append(grade)
print(filtered_grades_simple_for)


# Comprehension method

filtered_grades_comprehension = [grade for grade in grades if grade is not 'F']

print(filtered_grades_comprehension)
