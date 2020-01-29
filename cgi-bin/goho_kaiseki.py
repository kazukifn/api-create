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
    <link href="../css/style_sheet.css" rel="stylesheet" type="text/css" />
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
  <link href="../css/style_sheet.css" rel="stylesheet" type="text/css" />
  <div >
  <table>
  <tr>
  """)
  t = 0
  s = 0
  for token in tokens.pos_tags: 
    
    if token[1] != 'VERB' and t == 0 and token[1] != 'PRON':  #動詞ではないかつtは0回目かつ代名詞でない
      print("<td class=\"sample1\">{0}</td>".format(token[0]))
    elif token[1] == 'PRON':                                  #代名詞である
      if s == 0:
        print("<td class=\"sample1\">{0}</td>".format(token[0])) #代名詞の主語
        s += 1
      else:
        print("<td class=\"sample2\">{0}</td>".format(token[0])) #主語以外の代名詞
    elif token[1] == 'VERB':                                  #動詞である
      print("<td class=\"sample3\">{0}</td>".format(token[0]))
      t += 1
    elif token[1] == 'SYM':                                    #ピリオド,カンマ
      print("<td>{0}</td>".format(token[0]))
      t = 0                                                    #tの値をリセット　初めのループに戻す
      s = 0
    else:
      print("<td class=\"sample4\">{0}</td>".format(token[0]))    #その他は全て黄色

  print("""
  </tr>
  </table>
  </div>
  <p><img src="/image/aaa.png" height="70" width="300" alt="説明"></p>
  """)