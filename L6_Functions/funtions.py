# A function is a block of code which only runs when it is called. In Python,
# we do not use curly brackets, we use indentation with tabs or spaces

# Create function
def sayHello(name='Sam'):
    print(f'Hello {name}')

sayHello('John Doe')
sayHello()

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

print(f'total value is: {getSum(3, 4)}')

# A lambda function is a smal anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Very similar to JS arrow function

getLambdaSum = lambda num1, num2: num1 + num2

print(f'total value is : {getLambdaSum(10, 3)}')