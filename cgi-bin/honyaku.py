#!/usr/share/nginx/.virtualenvs/env3.7/bin/python
import cgi, sys, io, menu, cgitb
from foods_search import get_calorie

cgitb.enable()

# 文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from google_trans_new import google_translator  

translator = google_translator()  
translate_text = translator.translate('鳳凰',lang_tgt='en')  


print('''
Content-type: text/html

<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <title>翻訳するよ</title>
</head>

<body>
<p>{honyaku}</p>
</div>

</body>
</html>
'''[1:-1].format(honyaku=translate_text))
