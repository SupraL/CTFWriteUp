<h1>Py - 150</h1>
<p>Given an compiled python file. (Py.pyc).</p>
<h3>0x1 Decompile it</h3>

```python
with open("uncompiled file.py", "wb") as fileobj:
	uncompyle.uncompyle_file("Py.pyc", fileobj)
```

<p>We get</p>

```python
#Embedded file name: 1.py
import base64

def encode(message):
    s = ''
    for i in message:
        x = ord(i) ^ 32
        x = x + 16
        s += chr(x)

    return base64.b64encode(s)


correct = 'XlNkVmtUI1MgXWBZXCFeKY+AaXNt'
flag = ''
print 'Input flag:'
flag = raw_input()
if encode(flag) == correct:
    print 'correct'
else:
    print 'wrong'
```

<h3>0x2 Reverse the decode algo</h3>
```python
import base64

enc_flag = "XlNkVmtUI1MgXWBZXCFeKY+AaXNt"
enc_flag = base64.b64decode(enc_flag)
flag = ""
for char in enc_flag:
    flag = flag + chr(((ord(char)-16)^32))
print flag
```