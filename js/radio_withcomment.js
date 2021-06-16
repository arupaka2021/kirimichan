//ラジオボタンで「その他」が選択された場合のみテキストボックスへの入力を有効化する関数
function connecttext(textid, ischecked) {
	if(ischecked == true) {
	   // チェックが入っていたら有効化
		document.getElementById(textid).disabled = false;
	}
	else {
	   // チェックが入っていなかったら無効化
		document.getElementById(textid).disabled = true;
	}
}