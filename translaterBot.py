import requests
import json
from pprint import  pprint as print


app_id = "<df95206c>"
app_key = "<3367172fedcd8c2aee0a1f7b56341b1d>"
language = "en-gb"
word_id = "apple"
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
r = requests.get(url, headers={"app_id": <df95206c>, "app_key": <3367172fedcd8c2aee0a1f7b56341b1d>})
print(r.status_code)
res=r.json()