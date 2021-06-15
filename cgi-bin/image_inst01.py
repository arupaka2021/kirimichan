#!/usr/share/nginx/.virtualenvs/env3.7/bin/python
import cv2, cgi, sys, io, os, cgitb, datetime

cgitb.enable()

# 文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()
FORM_NAME = 'food_img'

if FORM_NAME in form:
    fileitem = form[FORM_NAME]

    # ファイル名はアップロード時の時間から自動生成する（既存画像ファイルと重複するのを避けるため）
    now = datetime.datetime.now()
    file_path, file_ext = os.path.splitext(os.path.basename(fileitem.filename))
    fname = '../image/img' + now.strftime('%Y%m%d%H%M%S') + file_ext

    #with open(os.path.join('..\\image\\', form["food_img"].value + os.path.basename(fileitem.filename)), 'wb') as fout:
    #fname = 'image/'+os.path.basename(fileitem.filename)
    with open(fname, 'wb') as fout:
        fout.write(fileitem.file.read())
        fout.close()

    '''
    ##### img = cv2.imread("C:/Users/Owner/Downloads/shiru1.jpeg")
    # 「upload_img.html」から受け取った画像データ「food_img」を読み込み、img変数に格納
    img = cv2.imread(r['food_img'])

    # img変数に格納した画像データを指定したディレクトリに出力
    img_name = "sample1.jpeg"
    cv2.imwrite("../image/{img_name}".format(img_name="img_name"), img)
    '''

    print('''
Content-type: text/html

<html lang="ja">
<head>
    <meta charset="utf-8">
    <title>画像アップロード完了</title>
</head>

<body>
<h1>画像を{fname}の名前で保存しました。</h1>
</body>
</html>
'''[1:-1].format(fname=fname))

else:
    print('''
Content-Type: text/html

<html>
<head></head>
<body>
<h1>Error</h1>
<pre>{}</pre>
</body>
</html>
'''[1:-1].format(type(form)))