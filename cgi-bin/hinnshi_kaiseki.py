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
    <link href="../css/stylesheet.css" rel="stylesheet" type="text/css" />
    <title>To Analyze</title>
    <div>
    <h1>To Analyze</h1>
    </div>
    <div>
    <form>
    <input type="text" name="t"  class="sample1" value=""> 
    <input type="submit" class="sample2" value="解析">
    </form>
    </div>
  """)

else:
  #フォームの値を取得して解析結果を表示
  t = form.getvalue("t", "0")
  tokens = Text(t)
  hinshi = {'ADJ' : "形容詞/", 'ADP' : "設置詞/", 'ADV' : "副詞/", 'AUX' : "助動詞/", 'CONJ' : "接続詞/", 'DET' : "限定詞/", 'INTJ' : "間投詞/", 'NOUN' : "名詞/", 'NUM' : "数値/", 'PART' : "助詞/", 'PRON' :"代名詞/", 'PROPN' : "固有名詞/", 'PUNCT' : "句読点/", 'SCONJ' : "連結詞/", 'SYM' : "シンボル/", 'VERB' : "動詞/", 'X' : "その他/"}
  print("""
  <meta http-equiv="content-type" charset="utf-8">
  <link href="../css/stylesheet.css" rel="stylesheet" type="text/css" />
  <div >
  <table>
  <tr>
  """)
  
  for token in tokens.pos_tags:
    
    print("<td>{0}</td>".format(token[0]))
  print("</tr>")
  print("<tr>")
  for token in tokens.pos_tags:
    print("<td>{0}</td>".format(hinshi[token[1]]))
  print("""
  </tr>
  </table>
  </div>
  """)