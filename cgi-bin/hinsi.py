# -*- coding:utf-8 -*-

from polyglot.text import Text

t = "I'm absolutely crazy about it"
tokens = Text(t)
for token in tokens.pos_tags:
    print("{0:20s}{1}".format(token[0], token[1]))
   
   #連想配列