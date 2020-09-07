import json
from pprint import pprint
import requests


# this dictionary class trivializes getting multiple definitions or examples.

class dictionary:

    def1 = None
    example1 = None
    def2 = None
    example2 = None

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

    def getDef2(self):
        if self.word2:
            self.def2 = self.word2['definition']
    
    def getExample2(self):
        if self.word2:
            self.def2 = self.word2['example']
    


    