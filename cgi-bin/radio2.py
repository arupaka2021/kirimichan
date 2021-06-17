#!/usr/share/nginx/.virtualenvs/env3.7/bin/python

import io, sys, os, json, codecs, random, datetime, cgi, cgitb

cgitb.enable()

# 文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print('''
Content-type: text/html

<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>おすすめの本紹介</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="ここにサイト説明を入れます">
<meta name="keywords" content="キーワード１,キーワード２,キーワード３,キーワード４,キーワード５">
<link rel="stylesheet" href="css/style.css">
<link rel="stylesheet" href="css/style-opening.css">
<script src="js/fixmenu_pagetop.js"></script>
<script src="js/openclose.js"></script>
<!--[if lt IE 9]>
<script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
<![endif]-->
</head>

<body>

<div id="container">

<header>



<h1 id="logo"><a href="index.html"><img src="images/logo.png" alt="ヒエダの自己紹介ページ"></a></h1>

<!--PC用（801px以上端末）メニュー-->
<nav id="menubar">
<ul>
<li><a href="index.html">Home</a></li>
<li><a href="about.html">About</a></li>


</ul>
</nav>

</header>

<div id="contents">

<section class="inner first">

<h2>おすすめの本紹介</h2>
<p><span class="color1">気分に合わせておすすめの本を紹介します</span><br>
<p>どんな本を読みたいですか？</p>

  <script>
function CheckData() {
    if (document.getElementById("number").value == "") {
    alert('数字を入力して下さい（半角）');
    return false;
    }
    else {
    n = document.getElementById("number").value;
    if (n == 1) {

        document.getElementById("result").value = 'オスカー・ワイルド『サロメ』';
    
    }
    else if(n == 2){
        document.getElementById("result").value = 'エドワード・ゴーリー『弦のないハープ』';
    }

   else if(n == 3){
        document.getElementById("result").value = '『新明解国語辞典』';
    }
    else if(n == 3){
        document.getElementById("result").value = '高村幸太郎『智恵子抄』';
    }
    else{ document.getElementById("result").value = '親鸞『教行信証』';

    } 
    return true;
    }
}
</script>
</head>

<body>
    <h1>あなたへのおすすめは？</h1>
    数字を入力して下さい（半角）<input type="text" id="number">
<button type="button" onclick="CheckData()">CHECK！</button>
<div>結果は…<input type="text" id="result" style="width:400px;">がおすすめです！</div>
</body>

</section>
<div style="width: 500px; height: auto; display: block; margin: auto;">
<a href = "about3.html"><img src="images/sinran.jpg"alt=""></a>
</div>


<footer>
<small>Copyright&copy; <a href="index.html">ヒエダの自己紹介ページ</a> All Rights Reserved.</small>
<span class="pr">《<a href="https://template-party.com/" target="_blank">Web Design:Template-Party</a>》</span>
</footer>

</div>
<!--/#contents-->

</div>
<!--/#container-->

<!--オープニングアニメーション-->
<aside id="mainimg">
<img src="images/1.png" alt="" class="photo photo1">
<img src="images/1.png" alt="" class="photo photo2">
<img src="images/1.png" alt="" class="photo photo3">
<img src="images/1.png" alt="" class="photo photo4">
<img src="images/1.png" alt="" class="photo photo5">
<img src="images/1.png" alt="" class="photo photo6">
<img src="images/1.png" alt="" class="photo photo7">
<img src="images/1.png" alt="" class="photo photo8">
<img src="images/1.png" alt="" class="photo photo9">
</aside>

<!--小さな端末用（800px以下端末）メニュー-->
<nav id="menubar-s">
<ul>
<li><a href="index.html">Home</a></li>
<li><a href="about.html">About</a></li>

</ul>
</nav>

<!--ページの上部に戻る「↑」ボタン-->
<p class="nav-fix-pos-pagetop"><a href="#">↑</a></p>

<!--メニュー開閉ボタン-->
<div id="menubar_hdr" class="close"></div>

<!--メニューの開閉処理条件設定　800px以下-->
<script>
if (OCwindowWidth() <= 800) {
	open_close("menubar_hdr", "menubar-s");
}
</script>

</body>
</html>
'''[1:-1].format(title=))