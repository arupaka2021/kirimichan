#!/usr/share/nginx/.virtualenvs/env3.7/bin/python

import io, sys, os, json, codecs, random, datetime, cgi

# 文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

title_str = 'カロリー計算'

form = cgi.FieldStorage()
age = int(form["age"].value)
gender = form["gender"].value
katudou = form["katudou"].value

if age >= 18 and age < 30 :
    nenrei="18-29"

elif age >= 30 and age < 49 :
    nenrei="30-49"

elif age >= 30 and age < 49 :
    nenrei="50-69"

else:
    nenrei="70-120"

import calorie

cal=calorie[gender][nenrei][katudou]

print('''
Content-type: text/html

<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <title>あなたの戒名</title>
  </head>
  <body>
  <h2>おめでとうございます！戒名の取得に成功しました。</2>
  <h2>あなたの戒名は</h2>
   <h1><span style="color:blue;">{0}</span></h1>
  <h2>です！</h2>
</body>
</html>
'''[1:-1].format(cal))