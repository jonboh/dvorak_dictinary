#!/usr/bin/env python
import sys

words = list()
with open('corpus.txt', "r") as f:
    words = list(f)
    words = list(map(lambda e: e.split('\t')[1].strip(), words))


def dvorak(level):
    if level == 0:
        return {'a','o','e','u','h','t','n','s'}
    elif level == 1:
        return dvorak(0).union({'i','d'})
    elif level == 2:
        return dvorak(1).union({'p','y','f','g'})
    elif level == 3:
        return dvorak(2).union({'k','x','b','m'})
    elif level == 4:
        return dvorak(3).union({'c','r','l','w'})
    elif level == 5:
        return dvorak(4).union({'q','j','v','z'})
    else:
        raise RuntimeError('Incorrect Level')


def isvalid(allowed_letters, word):
    for letter in word:
        if letter not in allowed_letters:
            return False
    return True

count = int(sys.argv[1])
level = int(sys.argv[2])
delimiter = sys.argv[3]
if delimiter == 'space':
    delimiter = ' '
else:
    delimiter = '\n'

allowed_letters = dvorak(level)
filtered_words = list()
for word in words:
    if isvalid(allowed_letters, word):
        filtered_words.append(word)
    if count == len(filtered_words):
        break

for word in filtered_words:
    print(word, end=delimiter)
