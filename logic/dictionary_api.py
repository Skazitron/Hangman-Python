import json
import requests


# this dictionary class trivializes getting multiple definitions or examples.

class dictionary:

    def1 = None
    example1 = None

    def __init__(self, word_id):
        super().__init__()
        self.jsonFile = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word_id.lower()).json()
        self.word1 = self.jsonFile[0]['meanings'][0]['definitions'][0]
        try:
            self.word2 = self.jsonFile[0]['meanings'][0]['definitions'][1]
        except IndexError:
            self.word2 = None    

    def getDef1(self):
        return self.word1['definition']
    
    def getExample1(self):
        return self.word1['example']


    