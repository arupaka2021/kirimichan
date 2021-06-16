import requests, urllib

parameter1 = urllib.parse.quote("ティラミス")
url = "https://ja.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&prop=pageimages&piprop=original&titles="+parameter1
res = requests.get(url)
data = res.json()

try:
    gazo1 = (data["query"]["pages"][0]["original"]["source"])
except KeyError:
    gazo1 = "/image/noimage.jpg"

print(gazo1)