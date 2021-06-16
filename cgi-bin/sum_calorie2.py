#!/usr/share/nginx/.virtualenvs/env3.7/bin/python
import cgi, sys, io, cgitb, menu, gazo 
from foods_search import get_calorie

cgitb.enable()

# 文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()

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
	cal1 = int(get_calorie(menu1))
else:
	menu1 = r['menu1']
	cal1 = int(menu.menu1[menu1])

# メニュー2のカロリーを変数に格納
if r['menu2'] == "other":
	menu2 = r['other2']
	cal2 = int(get_calorie(menu2))
else:
	menu2 = r['menu2']
	cal2 = int(menu.menu2[menu2])

# メニュー3のカロリーを変数に格納
if r['menu3'] == "other":
	menu3 = r['other3']
	cal3 = int(get_calorie(menu3))
else:
	menu3 = r['menu3']
	cal3 = int(menu.menu3[menu3])

# メニュー4のカロリーを変数に格納
if r['menu4'] == "other":
	menu4 = r['other4']
	cal4 = int(get_calorie(menu4))
else:
	menu4 = r['menu4']
	cal4 = int(menu.menu4[menu4])

# メニュー5のカロリーを変数に格納
if r['menu5'] == "other":
	menu5 = r['other5']
	cal5 = int(get_calorie(menu5))
else:
	menu5 = r['menu5']
	cal5 = int(menu.menu5[menu5])

# カロリーの合計値を算出
sum_calorie = cal1 + cal2 + cal3 + cal4 + cal5

# アドバイスを変数に格納
if calorie == sum_calorie:
	advice = "ピッタリ賞です！100万円をあげたいです！"
elif calorie > sum_calorie:
	advice = "さらに高カロリーな献立を目指して再チャレンジしましょう！"
else:
	advice = "さらに低カロリーな献立を目指して再チャレンジしましょう！"

# 画像を変数に格納
gazo1 = gazo.menu1[menu1]
gazo2 = gazo.menu2[menu2]
gazo3 = gazo.menu3[menu3]
gazo4 = gazo.menu4[menu4]
gazo5 = gazo.menu5[menu5]

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
		<img src="/image/{gazo1}" alt="主食の画像" class="menu1">
		<img src="/image/{gazo2}" alt="主菜の画像" class="menu2">
		<img src="/image/{gazo3}" alt="副菜の画像" class="menu3">
		<img src="/image/{gazo4}" alt="汁物の画像" class="menu4">
		<img src="/image/{gazo5}" alt="デザートの画像" class="menu5">
	</div>
</body>
</html>
'''[1:-1].format(title=title_str, calorie=calorie, sum_calorie=sum_calorie, advice=advice, gazo1=gazo1, gazo2=gazo2, gazo3=gazo3, gazo4=gazo4, gazo5=gazo5))