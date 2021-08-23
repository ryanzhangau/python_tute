# Python has functions creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.txt', 'w')

# Get file information
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and Javascript')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')

myFile.write(' I also like PHP')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)

# Read line by line
myFile = open('myfile.txt') # open file with readonly permission
for line in myFile:
    print(line)
    # remove space
    print(line.rstrip())

# Alternative way
myFile.seek(0) # move cursor to very beginning
lines = myFile.readlines()
print(lines)

# sometimes we can forget to close file after opening it
# this method does not need file.close()

with open('myfile.txt') as myFile:
    lines = myFile.readlines()

