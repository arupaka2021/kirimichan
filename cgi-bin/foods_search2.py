#!/usr/share/nginx/.virtualenvs/env3.7/bin/python
import cgi, sys, io, cgitb, re
import get_food_data as dat

# エラーメッセージ表示
cgitb.enable()

# 文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()

# 対象のフォーム変数名
params = ['search_food',]

# 結果を受け取る辞書
r = {}

for p in params:
    if p in form:
        r[p] = form[p].value
    else:
        r[p] = '(入力なし)'

# APIから結果を取得
foods = dat.fs.foods_search(r['search_food'])

# 取得したデータをリストに格納
if __name__ == '__main__':
    food_list = []

    for food in foods:
        food_list.append([food['food_description']])

# リストに格納した情報のうち、カロリーのみ取得
res1 = re.sub(r".*Calories", "Calories", food_list[0][0]) #グラム情報の削除
res2s = res1.split('|') #'|'で区切られた文字列を要素とするリストの作成
res3s = re.sub(r'\D', '', res2s[0]) #カロリーの数値のみ抽出

title = '食べ物の検索結果'

print('''
Content-type: text/html

<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>{title}</title>
</head>

<body>
<p>{calorie}</p>
</body>
</html>
'''[1:-1].format(title=title, calorie=res3s))