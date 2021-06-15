#!/usr/share/nginx/.virtualenvs/env3.7/bin/python

import io, sys, cgi, cgitb

# エラーメッセージ表示
cgitb.enable()

# 文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

title_str = 'ラジオボタン'

form = cgi.FieldStorage()

print('''
Content-type: text/html

<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8">
	<script scr="../js/radio.js"></script>
    <title>{title}</title>
</head>

<body>
<form action="sum_calorie.py" method="post">
<div class="content">
	<p>主食【必須】</p>
	<label><input type="radio" name="menu1" value="白米" required>白米</label><br>
	<label><input type="radio" name="menu1" value="玄米" required>玄米</label><br>
	<label><input type="radio" name="menu1" value="たけのこご飯" required>たけのこご飯</label><br>
	<label><input type="radio" name="menu1" value="赤飯" required>赤飯</label><br>
	<label><input type="radio" name="menu1" value="サフランライス" required>サフランライス</label><br>
	<label><input type="radio" name="menu1" value="うどん" required>うどん</label><br>
	<label><input type="radio" name="menu1" value="そうめん" required>そうめん</label><br>
	<label><input type="radio" name="menu1" value="other" required
				onclick="connecttext('text_menu1',this.checked);">その他</label>：
	<input type="text" name="othertext" id="text_menu1" value="">
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
	<label><input type="radio" name="menu2" value="other" required
				onclick="connecttext('text_menu1',this.checked);">その他</label>：
	<input type="text" name="othertext" id="text_menu1" value="">
</div>

<div class="content">
	<p>副菜【必須】</p>
	<label><input type="radio" name="menu3" value="hakumai" required>ほうれん草のおひたし</label><br>
	<label><input type="radio" name="menu3" value="genmai" required>ひじきの煮物</label><br>
	<label><input type="radio" name="menu3" value="takenoko" required>肉じゃが</label><br>
	<label><input type="radio" name="menu3" value="sekihan" required>茄子の揚げびたし</label><br>
	<label><input type="radio" name="menu3" value="safuran" required>冷ややっこ</label><br>
	<label><input type="radio" name="menu3" value="udon" required>冷やしトマト</label><br>
	<label><input type="radio" name="menu3" value="somen" required>ポテトサラダ</label><br>
	<label><input type="radio" name="menu3" value="other" required
				onclick="connecttext('text_menu1',this.checked);">その他</label>：
	<input type="text" name="othertext" id="text_menu1" value="">
</div>

<div class="content">
	<p>汁物【必須】</p>
	<label><input type="radio" name="menu4" value="genmai" required>味噌汁</label><br>
	<label><input type="radio" name="menu4" value="takenoko" required>わかめスープ</label><br>
	<label><input type="radio" name="menu4" value="sekihan" required>ミネストローネ</label><br>
	<label><input type="radio" name="menu4" value="safuran" required>ビーフシチュー</label><br>
	<label><input type="radio" name="menu4" value="udon" required>カレー</label><br>
	<label><input type="radio" name="menu4" value="somen" required>コーンスープ</label><br>
	<label><input type="radio" name="menu4" value="hakumai" required>コンソメスープ</label><br>
	<label><input type="radio" name="menu4" value="other" required
				onclick="connecttext('text_menu1',this.checked);">その他</label>：
	<input type="text" name="othertext" id="text_menu1" value="">
</div>

<div class="content">
	<p>デザート【必須】</p>
	<label><input type="radio" name="menu5" value="hakumai" required>プリン</label><br>
	<label><input type="radio" name="menu5" value="genmai" required>ヨーグルト</label><br>
	<label><input type="radio" name="menu5" value="takenoko" required>ショートケーキ</label><br>
	<label><input type="radio" name="menu5" value="sekihan" required>シュークリーム</label><br>
	<label><input type="radio" name="menu5" value="safuran" required>りんご</label><br>
	<label><input type="radio" name="menu5" value="udon" required>みかん</label><br>
	<label><input type="radio" name="menu5" value="somen" required>コーヒーゼリー</label><br>
	<label><input type="radio" name="menu5" value="other" required
				onclick="connecttext('text_menu1',this.checked);">その他</label>：
	<input type="text" name="othertext" id="text_menu1" value="">
</div>

	<div class="control">
    <button type="submit"> 決定</button>
	</div>
</form>


</body>


</html>
'''[1:-1].format(title=title_str))