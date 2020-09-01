import json
import pprint
import requests
app_id  = "b1c33bef"
app_key  = "da40b82cd9a26e65fed0d8e56e7dc242"
endpoint = "entries"


def definition(word_id):

    url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + "en-us" + "/" + word_id.lower()

    r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})
    pprint.pprint(r.json()['results'])

definition(input("testing: "))
