from txt_parser import wordSelector
from oxford_api import definition

usrIn = (input("What's difficulty do you want? (Easy, Medium, Hard): ")).lower()

while usrIn not in ['easy', 'medium', 'hard']:
    
    if usrIn == 'q': break

    usrIn = input("Please enter a valid difficulty: ")

userWord = wordSelector(usrIn)

print(userWord)
try:
    definition(userWord)
except KeyError:
    print("Word cannot be found in dictionary")
