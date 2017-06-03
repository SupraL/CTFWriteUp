import uncompyle
import base64
"""with open("uncompiled file.py", "wb") as fileobj:
    uncompyle.uncompyle_file("Py.pyc", fileobj)"""

enc_flag = "XlNkVmtUI1MgXWBZXCFeKY+AaXNt"
enc_flag = base64.b64decode(enc_flag)
flag = ""
for char in enc_flag:
    flag = flag + chr(((ord(char)-16)^32))
print flag
