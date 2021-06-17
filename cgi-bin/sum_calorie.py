#!/usr/share/nginx/.virtualenvs/env3.7/bin/python
import cgi, sys, io, cgitb, requests, urllib, menu, gazo 
from foods_search import get_calorie
from google_trans_new import google_translator

# エラーメッセージ表示
cgitb.enable()

# 文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()

translator = google_translator()

# 対象のフォーム変数名
params = ['calorie','menu1','menu2','menu3','menu4','menu5','other1','other2','other3','other4','other5',]

# 結果を受け取る辞書
r = {}
for p in params:
    if p in form:
        r[p] = form[p].value
    else:
        r[p] = ""

# 適正カロリーを変数に格納
calorie = int(r['calorie'])

# メニュー1のカロリーを変数に格納
if r['menu1'] == "other":
	menu1 = r['other1']
	menu1_en = translator.translate(menu1, lang_tgt='en')
	cal1 = int(get_calorie(menu1_en))

	# WikipediaAPIから画像取得
	parameter1 = urllib.parse.quote(menu1)
	url = "https://ja.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&prop=pageimages&piprop=original&titles="+parameter1
	res = requests.get(url)
	data = res.json()
	try:
		gazo1 = (data["query"]["pages"][0]["original"]["source"])
	except KeyError:
		gazo1 = "/image/noimage.jpg"
else:
	menu1 = r['menu1']
	cal1 = int(menu.menu1[menu1])
	gazo1 = "/image/" + gazo.menu1[menu1]

# メニュー2のカロリーを変数に格納
if r['menu2'] == "other":
	menu2 = r['other2']
	menu2_en = translator.translate(menu2, lang_tgt='en')
	cal2 = int(get_calorie(menu2_en))

	# WikipediaAPIから画像取得
	parameter1 = urllib.parse.quote(menu2)
	url = "https://ja.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&prop=pageimages&piprop=original&titles="+parameter1
	res= requests.get(url)
	data = res.json()
	try:
		gazo2 = (data["query"]["pages"][0]["original"]["source"])
	except KeyError:
		gazo2 = "/image/noimage.jpg"
else:
	menu2 = r['menu2']
	cal2 = int(menu.menu2[menu2])
	gazo2 = "/image/" + gazo.menu2[menu2]

# メニュー3のカロリーを変数に格納
if r['menu3'] == "other":
	menu3 = r['other3']
	menu3_en = translator.translate(menu3, lang_tgt='en')
	cal3 = int(get_calorie(menu3_en))

	# WikipediaAPIから画像取得
	parameter1 = urllib.parse.quote(menu3)
	url = "https://ja.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&prop=pageimages&piprop=original&titles="+parameter1
	res= requests.get(url)
	data = res.json()
	try:
		gazo3 = (data["query"]["pages"][0]["original"]["source"])
	except KeyError:
		gazo3 = "/image/noimage.jpg"
else:
	menu3 = r['menu3']
	cal3 = int(menu.menu3[menu3])
	gazo3 = "/image/" + gazo.menu3[menu3]

# メニュー4のカロリーを変数に格納
if r['menu4'] == "other":
	menu4 = r['other4']
	menu4_en = translator.translate(menu4, lang_tgt='en')
	cal4 = int(get_calorie(menu4_en))

	# WikipediaAPIから画像取得
	parameter1 = urllib.parse.quote(menu4)
	url = "https://ja.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&prop=pageimages&piprop=original&titles="+parameter1
	res= requests.get(url)
	data = res.json()
	try:
		gazo4 = (data["query"]["pages"][0]["original"]["source"])
	except KeyError:
		gazo4 = "/image/noimage.jpg"
else:
	menu4 = r['menu4']
	cal4 = int(menu.menu4[menu4])
	gazo4 = "/image/" + gazo.menu4[menu4]

# メニュー5のカロリーを変数に格納
if r['menu5'] == "other":
	menu5 = r['other5']
	menu5_en = translator.translate(menu5, lang_tgt='en')
	cal5 = int(get_calorie(menu5_en))

	# WikipediaAPIから画像取得
	parameter1 = urllib.parse.quote(menu5)
	url = "https://ja.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&prop=pageimages&piprop=original&titles="+parameter1
	res= requests.get(url)
	data = res.json()
	try:
		gazo5 = (data["query"]["pages"][0]["original"]["source"])
	except KeyError:
		gazo5 = "/image/noimage.jpg"
else:
	menu5 = r['menu5']
	cal5 = int(menu.menu5[menu5])
	gazo5 = "/image/" + gazo.menu5[menu5]

# カロリーの合計値を算出
sum_calorie = cal1 + cal2 + cal3 + cal4 + cal5

# アドバイスを変数に格納
if calorie == sum_calorie:
	advice = "ピッタリ賞です！100万円をあげたいです！"
elif calorie + 65 >= sum_calorie and calorie - 65 <= sum_calorie:
	advice = "適正カロリー範囲内で献立を作れました！すごい！<br>この調子で健康的な食生活を心がけましょう！"
elif calorie + 500 < sum_calorie:
	advice = "さすがに食べすぎです！<br>ヘルシーな献立に変更して再チャレンジしましょう！"
elif calorie - 500 > sum_calorie:
	advice = "カロリーがかなり足りていません！<br>力が出るような献立を意識して再チャレンジしましょう！"
elif calorie > sum_calorie:
	advice = "適正カロリーに達していません！<br>高カロリーのものを加えて再チャレンジしましょう！"
else:
	advice = "適正カロリーを超えています！<br>さらなる低カロリーを目指して再チャレンジしましょう！"

title_str = '結果'

print('''
Content-type: text/html

<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8">
	
	<link rel="stylesheet" href="../css/style.css">

    <title>{title}</title>
</head>

<body>
	<div class="content">
		<p>適正カロリーは{calorie}です。</p>
		<p>献立のカロリーは{sum_calorie}です。</p>
		<p>{advice}</p>
	</div>

	<div class="obon">
		<img src="{gazo1}" alt="主食の画像" title="{cal1}kcal" class="menu1">
		<img src="{gazo2}" alt="主菜の画像" title="{cal2}kcal" class="menu2">
		<img src="{gazo3}" alt="副菜の画像" title="{cal3}kcal" class="menu3">
		<img src="{gazo4}" alt="汁物の画像" title="{cal4}kcal" class="menu4">
		<img src="{gazo5}" alt="デザートの画像"  title="{cal5}kcal" class="menu5">
	</div>
	<div class="button-center">
		<button class="button-deco" type="button" onclick="location.pathname='../index.html'"> ホームへ戻る</button>
	</div>
</body>
</html>
'''[1:-1].format(title=title_str, calorie=calorie, sum_calorie=sum_calorie, advice=advice, gazo1=gazo1, gazo2=gazo2, gazo3=gazo3, gazo4=gazo4, gazo5=gazo5, cal1=cal1, cal2=cal2, cal3=cal3, cal4=cal4, cal5=cal5))