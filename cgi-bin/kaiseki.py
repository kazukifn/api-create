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
      print("{0:20s}{1}".format(token[0],"設置詞"))
    elif token[1] == "ADV":
      print("{0:20s}{1}".format(token[0],"副詞"))
    elif token[1] == "AUX":
      print("{0:20s}{1}".format(token[0],"助動詞"))
    elif token[1] == "CONJ":
      print("{0:20s}{1}".format(token[0],"接続詞"))
    elif token[1] == "DET":
      print("{0:20s}{1}".format(token[0],"限定詞"))
    elif token[1] == "ADP":
      print("{0:20s}{1}".format(token[0],"形容詞"))
    elif token[1] == "ADP":
      print("{0:20s}{1}".format(token[0],"形容詞"))
      
    else:
      print("<p>",token[1],"</p>")
      