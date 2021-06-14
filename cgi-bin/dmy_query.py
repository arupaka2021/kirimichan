#!/usr/share/nginx/.virtualenvs/env3.7/bin/python

import io, sys, os, json, codecs, random, datetime, cgi
import psycopg2, pypg
from psycopg2.extras import DictCursor

# 文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

title_str = '検索結果'

form = cgi.FieldStorage()

# 対象のフォーム変数名
params = ['fname',]

# 結果を受け取る辞書
r = {}

for p in params:
    if p in form:
        r[p] = form[p].value
    else:
        r[p] = ''

print('''
Content-type: text/html

<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>{title}</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">
  </head>
  <body>
  <h1 style="color:blue">{title}</h1>
  <table class="table">
  <tr><th>ID</th><th>氏名</th></tr>
'''[1:-1].format(title=title_str))

# データベース接続部分
db = pypg.dmy()
sql = "SELECT id, lname||fname AS fullname FROM dmy WHERE fname LIKE '%{}%' ORDER BY id".format(r['fname'])
cur = db.conn.cursor(cursor_factory=DictCursor)
cur.execute(sql)
rows = cur.fetchall()
cur.close()

for row in rows:
    print('  <tr><td>{}</td><td>{}</td></tr>'.format(row['id'], row['fullname']))

print('''
  </table>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.5/js/bootstrap.js"></script>
  </body>
</html>
'''[1:-1])
