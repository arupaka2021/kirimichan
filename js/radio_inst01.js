//ラジオボタンで「その他」が選択された場合のみテキストボックスへの入力を有効化する関数
//function connecttext(textid, ischecked) {{
//	if(ischecked == true) {{
//	   // チェックが入っていたら有効化
//		document.getElementById(textid).disabled = false;
//	}}
//	else {{
//	   // チェックが入っていなかったら無効化
//		document.getElementById(textid).disabled = true;
//	}}
//}}

$(function() {{
    console.log('Reached!');
    $('input[name="menu1"]').on('click', function() {{
        menu1_val = $('[name="menu1"]:checked').val();
        console.log(menu1_val);
        if ( menu1_val == 'other') {{
            $('#text_menu').prop("disabled", false);
        }}
        else {{
            $('#text_menu').prop("disabled", true);       
        }}
    }});
}});