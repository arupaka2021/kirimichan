$(function() {{
    console.log('Reached!');
    $('input[name="menu1"]').on('click', function() {{
        menu1_val = $('[name="menu1"]:checked').val();
        console.log(menu1_val);
        if ( menu1_val == 'other') {{
            $('#text_menu1').prop("disabled", false);
        }}
        else {{
            $('#text_menu1').prop("disabled", true);       
        }}
    }});

	$('input[name="menu2"]').on('click', function() {{
        menu2_val = $('[name="menu2"]:checked').val();
        console.log(menu2_val);
        if ( menu2_val == 'other') {{
            $('#text_menu2').prop("disabled", false);
        }}
        else {{
            $('#text_menu2').prop("disabled", true);       
        }}
    }});

	$('input[name="menu3"]').on('click', function() {{
        menu3_val = $('[name="menu3"]:checked').val();
        console.log(menu3_val);
        if ( menu3_val == 'other') {{
            $('#text_menu3').prop("disabled", false);
        }}
        else {{
            $('#text_menu3').prop("disabled", true);       
        }}
    }});

    $('input[name="menu4"]').on('click', function() {{
        menu4_val = $('[name="menu4"]:checked').val();
        console.log(menu4_val);
        if ( menu4_val == 'other') {{
            $('#text_menu4').prop("disabled", false);
        }}
        else {{
            $('#text_menu4').prop("disabled", true);       
        }}
    }});

    $('input[name="menu5"]').on('click', function() {{
        menu5_val = $('[name="menu5"]:checked').val();
        console.log(menu5_val);
        if ( menu5_val == 'other') {{
            $('#text_menu5').prop("disabled", false);
        }}
        else {{
            $('#text_menu5').prop("disabled", true);       
        }}
    }});
}});