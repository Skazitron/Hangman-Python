import random as rand

def wordScrambler(difficulty):
    array = []
    resArray = []
    if difficulty == 'easy':
        for i in range(0,2):
            array.append(rand.randint(0,25))
    if difficulty == 'medium':
        for i in range(0,3):
            array.append(rand.randint(0,25))
    if difficulty == 'hard':
        for i in range(0,4):
            array.append(rand.randint(0,25))
    alphabetArray = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in array:
        resArray.append(alphabetArray[i])
    return resArray
