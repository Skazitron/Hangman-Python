from txt_parser import wordSelector
from dictionary_api import dictionary

usrIn = (input("What's difficulty do you want? (Easy, Medium, Hard): ")).lower()

while usrIn not in ['easy', 'medium', 'hard']:
    
    if usrIn == 'q': break

    usrIn = input("Please enter a valid difficulty: ")

userWord = wordSelector(usrIn)

print(userWord)

try:
    var1 = dictionary(userWord)
    print(var1.getDef1())
    print(var1.getExample1())

except IndexError:
    print("Not Found. Sorry :(")
except KeyError:
    print("Not Found. Sorry :(")