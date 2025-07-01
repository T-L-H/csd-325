import requests
import json
response = requests.get("https://official-joke-api.appspot.com/random_joke")

def jprint(obj):  
    text = json.dumps(obj, sort_keys=True, indent=4) 
    print(text) 

jprint(response.json())