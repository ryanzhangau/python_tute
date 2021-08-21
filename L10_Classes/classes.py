# A class is like a blueprint for creating objects. An object has properties and methods
# (functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# Init use object
brad = User('Brad Traversy', 'brad@gmail.com', 37)

print(type(brad))


# access properties
print(brad.age)
print(brad.greeting())
print(brad.greeting())
brad.has_birthday()
print(brad.greeting())


# Extend class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

    def set_balance(self, balance):
        self.balance = balance

janet = Customer('Janet', 'janet@gmail.com', 25)

janet.set_balance(500)
print(janet.greeting())
