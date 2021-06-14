#!/usr/share/nginx/.virtualenvs/env3.7/bin/python

import io, sys, os, json, codecs, random, datetime, cgi

import cgitb
cgitb.enable()
print('''
Content-type: text/html

<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="utf-8">
        <title>献立を作ろう！</title>
    </head>

    <body>

<h2>成功！</h2>
</body>
</html>
'''[1:-1].format(1))
