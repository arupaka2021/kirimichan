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