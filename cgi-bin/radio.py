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
    <title>{title}</title>
</head>

<body>
<form action="sum_calorie.py" method="post">
	<p>メニュー1【必須】</p>
	<label><input type="radio" name="menu1" value="hakumai" required>白米</label><br>
	<label><input type="radio" name="menu1" value="genmai" required>玄米</label><br>
	<label><input type="radio" name="menu1" value="takenoko" required>たけのこご飯</label><br>
	<label><input type="radio" name="menu1" value="sekihan" required>赤飯</label><br>
	<label><input type="radio" name="menu1" value="safuran" required>サフランライス</label><br>
	<label><input type="radio" name="menu1" value="udon" required>うどん</label><br>
	<label><input type="radio" name="menu1" value="somen" required>冷やしそうめん</label><br>
	<label><input type="radio" name="menu1" value="other" required
				onclick="connecttext('text_menu1',this.checked);">その他</label>：
	<input type="text" name="othertext" id="text_menu1" value="">
</form>


<!-- ラジオボタンで「その他」が選択された場合のみテキストボックスへの入力を有効化する関数 -->

<script type="text/javascript">
function connecttext( textid, ischecked ) {
	if( ischecked ) {
		// チェックが入っていたら有効化
		document.getElementById(textid).disabled = false;
	}
	else {
		document.getElementById(textid).disabled = true;
	}
}
</script>

</body>
</html>
'''[1:-1].format(title=title_str))