# A module is basically a file containing a set of functions to include in your application.
# There are core python modules, modules you can install using the pip package manager (including Django) as well as customer modules

# import from core modules
import datetime
from datetime import date
import time

# pip module
# from camelcase import CamelCase

# custom module
from validator import validate_email

today = datetime.date.today()
thisDay = date.today()
timeStamp = time.time()

print(today)
print(thisDay)
print(timeStamp)


# c = CamelCase()
# print(c.hump('hello there world'))

email = 'test@test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is invalid')
