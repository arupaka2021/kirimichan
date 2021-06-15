import requests
import json
import urllib
parameter1 = urllib.parse.quote("亀")
url = "https://ja.wikipedia.org/w/api.php?action=query&redirects&format=json&formatversion=2&prop=extracts&exintro&explaintext&titles="+parameter1
res= requests.get(url)
data = res.json()
print(data["query"]["pages"][0]["extract"])