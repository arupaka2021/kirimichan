#!/usr/share/nginx/.virtualenvs/env3.7/bin/python
import cgi, sys, io
from foods_search import get_calorie

# 文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()

# 対象のフォーム変数名
params = ['othertext',]

# 結果を受け取る辞書
r = {}

for p in params:
    if p in form:
        r[p] = form[p].value
    else:
        r[p] = '(入力なし)'

sum_calorie = get_calorie(r['othertext'])

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