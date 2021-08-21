x = 10
y = 5

# Comparison Operators
if x > y:
    print(f'{x} is greater than {y}')

if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{x} is less than {y}')


if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{x} is less than {y}')

# Logical operators ( and, or, not ) - Use to combine conditional statements
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and {y} is less than or equal to 10')

if x > 2 or x <= 10:
    print(f'{x} is greater than 2 and {y} is less than or equal to 10')

if not(x == y):
    print(f'{x} is not equal to {y}')

# Membership operators ( not, not in ) - Membership operators are used to test if a sequence is presented in an object
number = [1, 2, 3, 4, 5]
x = 4

if x in number:
    print(f'{x} in number list')

x = 12
if x not in number:
    print(f'{x} is not in number list')

# Identity Operators ( is, is not ) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location

# is
x = 3
y = 3
if x is y:
    print(f'x: {x} is y: {y}')

x = 3
y = 4
if x is not y:
    print(f'x: {x} is not y: {y}')
