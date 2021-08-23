# Map takes a list and function to modify the item within the list and return a new list
from random import shuffle

data = ['beetroot', 'carrots', 'potatoes']

anagrams = []


def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)


anagrams = map(jumble, data)

print(list(anagrams))

# list comprehension
print([jumble(word) for word in data])
