# JSON is commonly use with data APIs. Here how we can parse JSON ino a Python dictionary

import json

# Sample JSON

userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse to dictionary
user = json.loads(userJSON)

print(user)
print(user['first_name'])

# Dictionary to JSON

car = {'make': 'Ford', 'model': 'Msutang', 'Year': 1970}

carJson = json.dumps(car)

print(carJson)