#!/usr/bin/env python3
import cgi
import cgitb
import os.path
import html
from polyglot.text import Text

#ブラウザのデバックを有効にする
cgitb.enable()

#全体の設定
FILE_LOG = "chat-log.txt"

#HTMLを画面に出力する
def print_html(body):
  #ヘッダを入力する
  print("Content-Type: text/html; charset=utf-8")
  print("")
  #HTMLを出力
  print("""
  <html><head><meta charset="utf-8">
  <title>To Analyze</title></head><body>
  <h1>To Analyze</h1>
  <div><form>
  入力してください: <input type="text" name="body" size="20">
  <input type="submit" value="解析">
  <input type="hidden" name="mode" value="write">
  </form></div><hr>
  {0}
  </body></html>
  """.format(body))

#画面に書き込みログを表示する
def mode_read(form):
  #ログを読み取る
  log = ""
  if os.path.exists(FILE_LOG):
    with open(FILE_LOG, "r", encoding='utf-8') as f:
      log = f.read()
  print_html(log)

#任意のURLにジャンプする
def jump(url):
  #ヘッダを出力する
  print("Status: 301 Moved Permanently")
  print("Location: " + url)
  print("")
  #HTMLを出力(ヘッダがうまく動かなくなった時の対策)
  print('<html><head>')
  print('<meta http-equiv="refresh" content="0;'+url+'">')
  print('</head><body>')
  print('<a href="'+url+'">jump</a></body></html>')


#解析結果の書き込み
def mode_write(form):
  #パラメータを取得
  body = form.getvalue("body", "")
  
  #HTMLに変換
  body = html.escape(body)

  #品詞リスト
  hinshi = {'ADJ' : "形容詞/", 'ADP' : "設置詞/", 'ADV' : "副詞/", 'AUX' : "助動詞/", 'CONJ' : "接続詞/", 'DET' : "限定詞/", 'INTJ' : "間投詞/", 'NOUN' : "名詞/", 'NUM' : "数値/", 'PART' : "助詞/", 'PRON' :"代名詞/", 'PROPN' : "固有名詞/", 'PUNCT' : "句読点/", 'SCONJ' : "連結詞/", 'SYM' : "シンボル/", 'VERB' : "動詞/", 'X' : "その他/"}
  
  #ファイルに保存
  with open(FILE_LOG, "a+", encoding='utf-8') as f:
    f.write("<p>{0}</p><hr>\n".format(body))
  #書き込み後にリダイレクトする
  jump('hinshi_test.py')

#メイン処理
def main():
  #フォームの値を取得
  form = cgi.FieldStorage()
  #modeパラメータを取得
  mode = form.getvalue("mode", "read")
  #modeの値によって処理を変更
  if mode == "read": mode_read(form)
  elif mode == "write": mode_write(form)
  else: mode_read(form)

if __name__ == "__main__": 
  main()