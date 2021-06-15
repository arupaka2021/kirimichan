import requests
import json
import urllib
parameter1 = urllib.parse.quote("ティラミス")
url = "https://ja.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&prop=pageimages&piprop=original&titles="+parameter1
res= requests.get(url)
data = res.json()
img_url = (data["query"]["pages"][0]["original"]["source"])

print('''
Content-Type: text/html

<html>
<head>
</head>
<body>
<img src="{gazou}" alt="画像" style="width:20%;height:40%;">
</body>
</html>
'''[1:-1].format(gazou=img_url))
