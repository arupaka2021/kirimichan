#!/usr/share/nginx/.virtualenvs/env3.7/bin/python

import io, sys, os, json, codecs, random, datetime, cgi

import cgitb
cgitb.enable()

# 文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

title_str = 'カロリー計算'

age = 25
gender = "女性"
katudou = "高"

'''
form = cgi.FieldStorage()
age = int(form["age"].value)
gender = form["gender"].value
katudou = form["katudou"].value
'''

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

title_str = 'ラジオボタン'

form = cgi.FieldStorage()
print('''
Content-type: text/html

<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="utf-8">
        <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
        <script src="../js/radio_inst01.js"></script>
        <title>献立を作ろう！</title>
    </head>

<body>

<h2>あなたの１食当たりの適正カロリーは<span style="color:blue;">{0}</span>です！</h2>
<p>適正カロリーを参考に献立を考えましょう。</p>

<form action="sum_calorie3.py" method="post">
<div class="content">
	<h2>主食【必須】</h2>
	<label><input type="radio" name="menu1" value="白米" required>白米</label><br>
	<label><input type="radio" name="menu1" value="玄米" required>玄米</label><br>
	<label><input type="radio" name="menu1" value="たけのこご飯" required>たけのこご飯</label><br>
	<label><input type="radio" name="menu1" value="赤飯" required>赤飯</label><br>
	<label><input type="radio" name="menu1" value="サフランライス" required>サフランライス</label><br>
	<label><input type="radio" name="menu1" value="うどん" required>うどん</label><br>
	<label><input type="radio" name="menu1" value="そうめん" required>そうめん</label><br>
	<label><input type="radio" name="menu1" value="other" required>その他</label>：
	<input type="text" name="other1" id="text_menu" value="" disabled>
</div>

<div class="content">
	<h2>主菜【必須】</h2>
	<label><input type="radio" name="menu2" value="鮭の塩焼き" required>鮭の塩焼き</label><br>
	<label><input type="radio" name="menu2" value="豚の生姜焼き" required>豚の生姜焼き</label><br>
	<label><input type="radio" name="menu2" value="アジフライ" required>アジフライ</label><br>
	<label><input type="radio" name="menu2" value="ハンバーグ" required>ハンバーグ</label><br>
	<label><input type="radio" name="menu2" value="餃子" required>餃子</label><br>
	<label><input type="radio" name="menu2" value="えび天" required>えび天</label><br>
	<label><input type="radio" name="menu2" value="唐揚げ" required>唐揚げ</label><br>
	<label><input type="radio" name="menu2" value="other" required
				onclick="connecttext('text_menu',this.checked);">その他</label>：
	<input type="text" name="other2" id="text_menu" value="">
</div>

<div class="content">
	<h2>副菜【必須】</h2>
	<label><input type="radio" name="menu3" value="ほうれん草のおひたし" required>ほうれん草のおひたし</label><br>
	<label><input type="radio" name="menu3" value="ひじきの煮物" required>ひじきの煮物</label><br>
	<label><input type="radio" name="menu3" value="肉じゃが" required>肉じゃが</label><br>
	<label><input type="radio" name="menu3" value="茄子の揚げびたし" required>茄子の揚げびたし</label><br>
	<label><input type="radio" name="menu3" value="冷ややっこ" required>冷ややっこ</label><br>
	<label><input type="radio" name="menu3" value="冷やしトマト" required>冷やしトマト</label><br>
	<label><input type="radio" name="menu3" value="ポテトサラダ" required>ポテトサラダ</label><br>
	<label><input type="radio" name="menu3" value="other" required
				onclick="connecttext('text_menu',this.checked);">その他</label>：
	<input type="text" name="other3" id="text_menu" value="">
</div>

<div class="content">
	<h2>汁物【必須】</h2>
	<label><input type="radio" name="menu4" value="味噌汁" required>味噌汁</label><br>
	<label><input type="radio" name="menu4" value="わかめスープ" required>わかめスープ</label><br>
	<label><input type="radio" name="menu4" value="ミネストローネ" required>ミネストローネ</label><br>
	<label><input type="radio" name="menu4" value="ビーフシチュー" required>ビーフシチュー</label><br>
	<label><input type="radio" name="menu4" value="カレー" required>カレー</label><br>
	<label><input type="radio" name="menu4" value="コーンスープ" required>コーンスープ</label><br>
	<label><input type="radio" name="menu4" value="コンソメスープ" required>コンソメスープ</label><br>
	<label><input type="radio" name="menu4" value="other" required
				onclick="connecttext('text_menu',this.checked);">その他</label>：
	<input type="text" name="other4" id="text_menu" value="">
</div>

<div class="content">
	<h2>デザート【必須】</h2>
	<label><input type="radio" name="menu5" value="プリン" required>プリン</label><br>
	<label><input type="radio" name="menu5" value="ヨーグルト" required>ヨーグルト</label><br>
	<label><input type="radio" name="menu5" value="ショートケーキ" required>ショートケーキ</label><br>
	<label><input type="radio" name="menu5" value="シュークリーム" required>シュークリーム</label><br>
	<label><input type="radio" name="menu5" value="りんご" required>りんご</label><br>
	<label><input type="radio" name="menu5" value="みかん" required>みかん</label><br>
	<label><input type="radio" name="menu5" value="コーヒーゼリー" required>コーヒーゼリー</label><br>
	<label><input type="radio" name="menu5" value="other" required
				onclick="connecttext('text_menu',this.checked);">その他</label>：
	<input type="text" name="other5" id="text_menu" value="">
</div>

	<div class="control">
    <button type="submit"> 決定</button>
	</div>
</form>

</body>


</html>
'''[1:-1].format(calorie))