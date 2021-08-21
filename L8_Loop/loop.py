# A for loop is used for iteration over a sequence (thant is either a list, a tuple, a dictionary, a set, or a string).
people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person in people:
    print(f'Current person: {person}')
print('--------------------------------')

# Break
for person in people:
    if person == 'Sara':
        break
    print(f'Current person: {person}')
print('--------------------------------')

# Continue
for person in people:
    if person == 'Sara':
        continue
    print(f'Current person: {person}')
print('--------------------------------')

# Range
for i in range(len(people)):
    print(people[i])
print('--------------------------------')

for i in range(0, 11):
    print(f'Number: {i}')
print('--------------------------------')

# While loops excute a set of statements as long as a condition is true.
count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1