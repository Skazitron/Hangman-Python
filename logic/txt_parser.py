from random import randint
import linecache

def numberMan(difficult):
    #the dictionary makes lookup for the number of words easy
    
    numberBoy = {
        "hard" : 39303,
        "easy" : 8774,
        "medium" : 21635
    }

    return randint(0, numberBoy[difficult])

# I don't know why I made another function.
# I guess it makes reading it easier?

def wordSelector(difficult):

    random_num = numberMan(difficult)
    word = linecache.getline('./wordlist/%s.txt' %difficult, random_num)
    
    return word
