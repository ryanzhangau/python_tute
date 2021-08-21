# A Dictionary is a collecton which is unordered, mutable and indexed. No duplicate members

# Create dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

print(person, type(person))


# Use constructor
person2 = dict(first_name='Sara', last_name='Williams')
print(person2, type(person2))

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '12345656'

print(person)

# get dictionary keys
print(person.keys(), type(person.keys()))

# Get dictionary items
print(person.items(), type(person.items()))

# Copy dictionary
person3 = person.copy()
person3['city'] = 'Boston'
print(person3)

# Remove item
del(person['age'])
print(person)

person.pop('phone')
print(person)

# Get length
print(len(person3))

# Clear
person.clear()
print(person)

# List of dictionary
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25},
]
print(people)

# Get value from list of dictionary
print(people[0]['name'])