#!/usr/share/nginx/.virtualenvs/env3.7/bin/python
import cgi, sys, io
import get_food_data as dat

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

foods = dat.fs.foods_search(r['search_food'])

if __name__ == '__main__':
    food_list = []

    for food in foods:
        food_list.append([food['food_name'], food['food_description']])

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
    <p></p>
</body>
</html>
'''[1:-1].format(title=title))