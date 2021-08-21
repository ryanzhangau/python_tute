# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# constructor
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

print(fruits, fruits2)

# Single value tuple needs trailing comma
# Otherwise python treats it as a string
singleElementTuple1 = ('Apples')
singleElementTuple2 = ('Apples',)
print(singleElementTuple1, type(singleElementTuple1))
print(singleElementTuple2, type(singleElementTuple2))

# Get a value
print(fruits[1])

# Tuple is immutable
# cannot do fruits[0] = 'something'


# Get length
print(len(fruits))

# Delete tuple
del fruits2
# print(fruits2)


# A Set is a collection which is unordered and unindex. No duplicate members
fruits_set = {'Apples', 'Oranges', 'Mango'}
print(fruits_set)

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')
print(fruits_set)

# Remove from set
fruits_set.remove('Grape')
print(fruits_set)

# Clear set
fruits_set.clear()
print(fruits_set)

# Delete set
del fruits_set
# print(fruits_set)

# Set union
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = set1 & set2
print(set3)

# set or
set4 = set1 | set2
print(set4)

# find element in set1 but not in set2
set5 = set1 - set2
print(set5)