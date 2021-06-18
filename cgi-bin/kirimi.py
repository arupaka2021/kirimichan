#!/usr/share/nginx/.virtualenvs/env3.7/bin/python

import io, sys, cgi, cgitb
import good_calorie

# エラーメッセージ表示
cgitb.enable()

# 文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

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

cal = int(good_calorie.calorie[gender][nenrei][katudou])
calo = cal /3
calorie = round(calo) 

title_str = '献立作成'

print('''
Content-type: text/html

<!DOCTYPE html>
<html lang="ja">
<head>
	<meta charset="utf-8">

	<link rel="stylesheet" href="../css/style2.css">

	<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
	<script src="../js/radio.js"></script>

	<title>{title}</title>
</head>

<body>
	<div class="content">
	<h2>あなたの１食当たりの適正カロリーは<span style="color:blue;">{calorie}</span>kcalです！</h2>
	<p>適正カロリーを参考に献立を考えましょう。</p>
	</div>

	<form action="sum_calorie.py" method="post">
		<input type="hidden" name="calorie" value="{calorie}">
		<div class="content">
			<p>主食【必須】</p>
			<label><input type="radio" name="menu1" value="白米" required>白米</label><br>
			<label><input type="radio" name="menu1" value="玄米" required>玄米</label><br>
			<label><input type="radio" name="menu1" value="たけのこご飯" required>たけのこご飯</label><br>
			<label><input type="radio" name="menu1" value="赤飯" required>赤飯</label><br>
			<label><input type="radio" name="menu1" value="サフランライス" required>サフランライス</label><br>
			<label><input type="radio" name="menu1" value="うどん" required>うどん</label><br>
			<label><input type="radio" name="menu1" value="そうめん" required>そうめん</label><br>
			<label><input type="radio" name="menu1" value="other" required>その他（10字以内）：</label>
			<input type="text" name="other1" id="text_menu1" value="" maxlength=10 disabled>
			<label><input type="radio" name="menu1" value="なし" required>無し</label><br>
		</div>

		<div class="content">
			<p>主菜【必須】</p>
			<label><input type="radio" name="menu2" value="鮭の塩焼き" required>鮭の塩焼き</label><br>
			<label><input type="radio" name="menu2" value="豚の生姜焼き" required>豚の生姜焼き</label><br>
			<label><input type="radio" name="menu2" value="アジフライ" required>アジフライ</label><br>
			<label><input type="radio" name="menu2" value="ハンバーグ" required>ハンバーグ</label><br>
			<label><input type="radio" name="menu2" value="餃子" required>餃子</label><br>
			<label><input type="radio" name="menu2" value="えび天" required>えび天</label><br>
			<label><input type="radio" name="menu2" value="唐揚げ" required>唐揚げ</label><br>
			<label><input type="radio" name="menu2" value="other" required>その他（10字以内）：</label>
			<input type="text" name="other2" id="text_menu2" value="" maxlength=10 disabled>
			<label><input type="radio" name="menu2" value="なし" required>無し</label><br>
		</div>

		<div class="content">
			<p>副菜【必須】</p>
			<label><input type="radio" name="menu3" value="ほうれん草のおひたし" required>ほうれん草のおひたし</label><br>
			<label><input type="radio" name="menu3" value="ひじきの煮物" required>ひじきの煮物</label><br>
			<label><input type="radio" name="menu3" value="肉じゃが" required>肉じゃが</label><br>
			<label><input type="radio" name="menu3" value="茄子の揚げびたし" required>茄子の揚げびたし</label><br>
			<label><input type="radio" name="menu3" value="冷ややっこ" required>冷ややっこ</label><br>
			<label><input type="radio" name="menu3" value="冷やしトマト" required>冷やしトマト</label><br>
			<label><input type="radio" name="menu3" value="ポテトサラダ" required>ポテトサラダ</label><br>
			<label><input type="radio" name="menu3" value="other" required>その他（10字以内）：</label>
			<input type="text" name="other3" id="text_menu3" value="" maxlength=10 disabled>
			<label><input type="radio" name="menu3" value="なし" required>無し</label><br>
		</div>

		<div class="content">
			<p>汁物【必須】</p>
			<label><input type="radio" name="menu4" value="味噌汁" required>味噌汁</label><br>
			<label><input type="radio" name="menu4" value="わかめスープ" required>わかめスープ</label><br>
			<label><input type="radio" name="menu4" value="ミネストローネ" required>ミネストローネ</label><br>
			<label><input type="radio" name="menu4" value="ビーフシチュー" required>ビーフシチュー</label><br>
			<label><input type="radio" name="menu4" value="カレー" required>カレー</label><br>
			<label><input type="radio" name="menu4" value="コーンスープ" required>コーンスープ</label><br>
			<label><input type="radio" name="menu4" value="コンソメスープ" required>コンソメスープ</label><br>
			<label><input type="radio" name="menu4" value="other" required>その他（10字以内）：</label>
			<input type="text" name="other4" id="text_menu4" value="" maxlength=10 disabled>
			<label><input type="radio" name="menu4" value="なし" required>無し</label><br>
		</div>

		<div class="content">
			<p>デザート【必須】</p>
			<label><input type="radio" name="menu5" value="プリン" required>プリン</label><br>
			<label><input type="radio" name="menu5" value="ヨーグルト" required>ヨーグルト</label><br>
			<label><input type="radio" name="menu5" value="ショートケーキ" required>ショートケーキ</label><br>
			<label><input type="radio" name="menu5" value="シュークリーム" required>シュークリーム</label><br>
			<label><input type="radio" name="menu5" value="りんご" required>りんご</label><br>
			<label><input type="radio" name="menu5" value="みかん" required>みかん</label><br>
			<label><input type="radio" name="menu5" value="コーヒーゼリー" required>コーヒーゼリー</label><br>
			<label><input type="radio" name="menu5" value="other" required>その他（10字以内）：</label>
			<input type="text" name="other5" id="text_menu5" value="" maxlength=10 disabled>
			<label><input type="radio" name="menu5" value="なし" required>無し</label><br>
		</div>

		<div class="button-center">
			<button class="button-deco" type="submit"> 決定</button>
		</div>
	</form>
</body>
</html>
'''[1:-1].format(title=title_str, calorie=calorie))