#!/usr/share/nginx/.virtualenvs/env3.7/bin/python

import io, sys, os, json, codecs, random, datetime
import getjson

# 文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 現在時間を取得
now = datetime.datetime.now()
now_str = now.strftime('%Y年%m月%d日 %H:%M:%S')

title_str = 'サーバのIP取得'

css_array = ['#FF0000','#009900','#0000FF']
array_num = random.randint(0,2)

JSONURL = 'http://httpbin.org/ip'

res = getjson.getjson(JSONURL)

ip = res['origin']

print('''
Content-type: text/html

<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <title>{title}</title>
  </head>
  <body>
  <h1 style="color:{css}">{title}</h1>
  <h2>このサーバのIPアドレス：{ip}</h2>
  </body>
</html>
'''[1:-1].format(css=css_array[array_num],title=title_str,ip=ip))
