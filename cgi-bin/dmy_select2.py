#!/usr/share/nginx/.virtualenvs/env3.7/bin/python

import io, sys, os, json, codecs, random, datetime, pypg
import psycopg2
from psycopg2.extras import DictCursor

# 文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 現在時間を取得
now = datetime.datetime.now()
now_str = now.strftime('%Y年%m月%d日 %H:%M:%S')

title_str = 'データベースから取得して表示するプログラム'

css_array = ['#FF0000','#009900','#0000FF']
array_num = random.randint(0,2)

print('''
Content-type: text/html

<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <title>{title}</title>
    <style type="text/css">
	table {{border: 1px solid #999999;}}
	th,td {{border: 1px solid #999999;text-align:center;}}
    </style>
  </head>
  <body>
  <h1 style="color:{css}">{title}</h1>
  <h2>現在日時：{now}</h2>
  <table>
    <tr><th>ID</th><th>氏名</th><th>誕生日</th><th>出身地</th><th>カレーの食べ方</th></tr>
'''[1:-1].format(css=css_array[array_num],title=title_str,now=now_str))

# データベース接続部分
db = pypg.dmy()
sql = "SELECT id, lname||fname AS fullname, birth, pref, curry FROM dmy WHERE blood = 'AB型' AND CAST(birth AS VARCHAR(12)) LIKE '1967%' ORDER BY id"
cur = db.conn.cursor(cursor_factory=DictCursor)
cur.execute(sql)
rows = cur.fetchall()
cur.close()

for r in rows:
    print('    <tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(r['id'], r['birth'], r['pref'], r['fullname'], r['curry']))

print('''
  </table>
  </body>
</html>
'''[1:-1].format(css=css_array[array_num],title=title_str,now=now_str))

