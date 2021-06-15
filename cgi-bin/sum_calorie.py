#!/usr/share/nginx/.virtualenvs/env3.7/bin/python
import cgi, sys, io, menu
from foods_search import get_calorie

# 文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()

# 対象のフォーム変数名
params = ['menu1','menu2','menu3','menu4','menu5','ohter1','ohter2','ohter3','ohter4','ohter5',]

# 結果を受け取る辞書
r = {}

for p in params:
    if p in form:
        r[p] = form[p].value
    else:
        r[p] = ""

# メニュー1のカロリーを出す
if r['menu1'] == "ohter":
	cal1 = get_calorie(r['other1'])
else:
	menu1 = r['menu1']
	cal1 = int(menu.menu1[menu1])

# メニュー2のカロリーを出す
if r['menu2'] == "ohter":
	cal2 = get_calorie(r['other2'])
else:
	menu2 = r['menu2']
	cal2 = int(menu.menu2[menu])

# メニュー3のカロリーを出す
if r['menu3'] == "ohter":
	cal3 = get_calorie(r['other3'])
else:
	menu3 = r['menu3']
	cal3 = int(menu.menu3[menu3])

# メニュー1のカロリーを出す
if r['menu4'] == "ohter":
	cal4 = get_calorie(r['other4'])
else:
	menu4 = r['menu4']
	cal4 = int(menu.menu4[menu4])

# メニュー5のカロリーを出す
if r['menu5'] == "ohter":
	cal5 = get_calorie(r['other5'])
else:
	menu5 = r['menu5']
	cal5 = int(menu.menu5[menu5])

# カロリーの合計値を算出
sum_calorie = cal1 + cal2 + cal3 + cal4 + cal5

title_str = 'カロリー合計'

print('''
Content-type: text/html

<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <title>{title}</title>
</head>

<body>
	<p>{sum_calorie}</p>
</body>
</html>
'''[1:-1].format(title=title_str, sum_calorie=sum_calorie))