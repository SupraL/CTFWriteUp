# -*- coding:utf8 -*-
from base64 import *

"""s=open('flag.jpg','rb').read()
s='-'.join(map(b16encode,list(s)))
s=map(''.join,zip(*(s.split('-'))))
with open('first','wb') as f:
    f.write(b16decode(s[0]))
with open('second','wb') as f:
    f.write(b16decode(s[1]))"""

"""s = open("second","rb").read()
with open('flag2','wb') as f:
	f.write(b16encode(s))"""
def unzip(iterable):
    return zip(*iterable)

a = open("flag","rb").read()
b = open("flag2","rb").read()
c = ""
for i in range(len(a)):
	asd = str(a[i]) + str(b[i])
	c = c + asd
with open('flag.bin','wb') as f:
	f.write(c)