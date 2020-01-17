#!/usr/bin/env python3
#解析を行うプログラム

import cgi
from polyglot.text import Text

#ヘッダの出力
print("Content-Type: text/html; charset=utf-8")
print("")

#送信されたフォームデータを取得する
form = cgi.FieldStorage()

#フォームにtのデータが含まれるか？
if (not 't' in form) :
  #含まれないのでフォームを表示
  print("""
    <meta http-equiv="content-type" charset="utf-8">
    <form>
    <input type="text" name="t"> 
    <input type="submit" value="解析">
    </form>
  """)

else:
  #フォームの値を取得して解析結果を表示
  t = form.getvalue("t", "0")
  tokens = Text(t)
  for token in tokens.pos_tags:
    
    if token[1] == "ADJ":
      print("{0:20s}{1}".format(token[0],"形容詞"))
    elif token[1] == "ADP":
      print("""
        <meta http-equiv="content-type" charset="utf-8">
        <p>設置詞</p>
        """)
    elif token[1] == "ADV":
      print("""
        <meta http-equiv="content-type" charset="utf-8">
        <p></p>
        """)
    elif token[1] == "AUX":
      print("""
        <meta http-equiv="content-type" charset="utf-8">
        <p>形容詞</p>
        """)
    elif token[1] == "PRON":
      print("""
        <meta http-equiv="content-type" charset="utf-8">
        <p>代名詞</p>
        """)

    elif token[1] == "SCONJ":
      print("""
        <meta http-equiv="content-type" charset="utf-8">
        <p>従属接続詞</p>
        """)
    
    elif token[1] == "VERB":
      print("""
        <meta http-equiv="content-type" charset="utf-8">
        <p>動詞</p>
        """)



    else:
      print("<p>",token[1],"</p>")
      