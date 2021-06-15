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
cal=int(calorie.calorie[gender][nenrei][katudou])
calo = cal /3
calorie = round(calo) 
print('''
Content-type: text/html

<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="utf-8">
        <title>献立を作ろう！</title>
    </head>



<body>

<h2>あなたの１食当たりの適正カロリーは<span style="color:blue;">{0}</span>です！</h2>
<p>適正カロリーを参考に献立を考えましょう。</p>

<h1>主食</h1>
</body>

<main>
    <section>
    <form action="kimiri2.py" method="post">

    <button class="btn">次へ</button>
    </form>
    </section>
</main>
</html>
'''[1:-1].format(calorie))