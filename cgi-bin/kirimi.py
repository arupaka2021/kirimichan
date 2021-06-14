#!/usr/share/nginx/.virtualenvs/env3.7/bin/python

import io, sys, os, json, codecs, random, datetime, cgi

import cgitb
cgitb.enable()

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

elif age >= 50 and age < 69 :
    nenrei="50-69"

else:
    nenrei="70-120"

import calorie
cal=calorie.calorie[gender][nenrei][katudou]

print('''
Content-type: text/html

<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="utf-8">
        <title>献立を作ろう！</title>
    </head>

<main>
    <section>
        <form action="/cgi-bin/kirimi.py" method="post">
        <!-- ここから以下３行を各Pythonファイルに入れることで次々とデータを渡せます -->
        <input type="hidden" name="cal" value="{cal}"/>
        </form>
    </section>
</main>
<body>

<h2>あなたの適正カロリーは</h2>
<h1><span style="color:blue;">{0}</span></h1>
<h2>です！</h2>
</body>
</html>
'''[1:-1].format(cal))