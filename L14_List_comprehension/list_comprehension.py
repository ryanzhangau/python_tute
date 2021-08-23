# List comprehension gives an alternative way to construct list or dictionary based on the collections

prizes = [5, 10, 50, 100, 1000]

dbl_prizes = []

# use for
for prize in prizes:
    dbl_prizes.append(prize * 2)

print(dbl_prizes)

# comprehension method
dbl_prizes_comprehension = [prize*2 for prize in prizes]

print(dbl_prizes_comprehension)


# squaring numbers
numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squared_even_numbers = []
for num in numbs:
    if (num ** 2) % 2 == 0:
        squared_even_numbers.append(num ** 2)

print(squared_even_numbers)

# Comprehension method
squared_even_numbers_comprehension = [num ** 2 for num in numbs if (num ** 2) % 2 == 0]

print(squared_even_numbers_comprehension)