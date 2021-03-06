#!/usr/share/nginx/.virtualenvs/env3.7/bin/python
import cgi, sys, io

# 文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()

# menu1のカロリー取得
params = ['menu1','menu2','menu3','menu4','menu5',]
r = {}

for p in params:
    if p in form:
        r[p] = form[p].value
    else:
        r[p] = '(入力なし)'
import gazo      
menu1 = r['menu1']
gazo1=gazo.menu1[menu1]

menu2 = r['menu2']
gazo2=gazo.menu2[menu2]

menu3 = r['menu3']
gazo3=gazo.menu3[menu3]

menu4 = r['menu4']
gazo4=gazo.menu4[menu4]

menu5 = r['menu5']
gazo5=gazo.menu5[menu5]


title_str = 'カロリー合計'

print('''
Content-type: text/html

<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <link rel="stylesheet" href="/css/kondate.css">
</head>

<body>
<div class="class1">
<img src="/image/{gazo1}" alt="主食の画像" class="menu1">
<img src="/image/{gazo2}" alt="主菜の画像" class="menu2">
<img src="/image/{gazo3}" alt="副菜の画像" class="menu3">
<img src="/image/{gazo4}" alt="汁物の画像" class="menu4">
<img src="/image/{gazo5}" alt="デザートの画像" class="menu5">
</div>

</body>
</html>
'''[1:-1].format(title=title_str, gazo1=gazo1, gazo2=gazo2, gazo3=gazo3, gazo4=gazo4, gazo5=gazo5))