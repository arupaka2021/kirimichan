function connecttext(textid, ischecked) {
	if(ischecked == true) {
		document.getElementById(textid).disabled = false;
	}
	else {
		document.getElementById(textid).disabled = true;
	}
}