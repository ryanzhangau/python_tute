name = 'Brand'
age = 37

# Casting age to str, otherwise throw error
print('Hello, my name is ' + name + ' and I am ' + str(age))

# Arguments by position
print('Hello, my name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (python 3.6+)
print(f'Hello, my name is {name} and I am {age}')

# String methods
s = 'Hello World World'
alphanumeric = 'thisIsATest123'
alphabetic = 'ThisIsAlphabetic'
numeric = '12345'

print(s.capitalize())                   # Capitalize
print(s.upper())                        # Upper case
print(s.lower())                        # Lower case
print(s.swapcase())                     # swap case
print(len(s))                           # Get string length
print(s.replace('World', 'everyone'))   # Replace all instance
print(s.count('orld'))                  # Count sub string
print(s.startswith('He'))               # Start with sub string
print(s.endswith('World'))              # End with sub string
print(s.split())                        # Split string into a list
print(s.split('r'))                     # Split string by delimiter
print(alphanumeric.isalnum())           # is all alphanumeric
print(alphabetic.isalpha())             # is all alphabetic
print(numeric.isnumeric())              # is all numeric
