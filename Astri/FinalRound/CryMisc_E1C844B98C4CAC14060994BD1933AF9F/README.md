<h3>0x1 Plaintext attack crypto.zip by jiami.py</h3>
```
pkcrack -c "jiami.py" -p jiami.py -d o.zip -P jiami.zip -C crypto.zip
```

<h3>0x2 Weak public key attack</h3>

```python
n = 0x48D6B5DAB6617F21B39AB2F7B14969A7337247CABB417B900AE1D986DB47D971 //32945885482421841602167475970472000545315534895409154025267147105384142461297
```

Factordb get pq

```python
p=177334994338425644535647498913444186659
q=185783328357334813222812664416930395483
```

use rsatools get d and c

```
python rsatools -p 177334994338425644535647498913444186659 -q 185783328357334813222812664416930395483 -o pri.key
```

Output:

```
n = 48d6b5dab6617f21b39ab2f7b14969a7337247cabb417b900ae1d986db47d971
e = 65537 (0x10001)
d = 2f7162ac1dc52d688732c9455a7d85ca0761c897e756fe70e5302449304e150d
p = 177334994338425644535647498913444186659 (0x85697a42942a9e8e1a20679ebdc6ca23)
q = 185783328357334813222812664416930395483 (0x8bc4914953b87cd37a10e46a0594755b)

c = 068C2E12FADEBBD344E82FA9E1EAC0F0BDE5AECBD7840F18352CF761F872233D
```

decrypt:

```python
import binascii
n = 0x48d6b5dab6617f21b39ab2f7b14969a7337247cabb417b900ae1d986db47d971
d = 0x2f7162ac1dc52d688732c9455a7d85ca0761c897e756fe70e5302449304e150d
c = 0x068C2E12FADEBBD344E82FA9E1EAC0F0BDE5AECBD7840F18352CF761F872233D
m = hex(pow(c,d,n)).rstrip("L")
print binascii.unhexlify(m[2:])
```

output:
copy__white__key

It seems is the aes key. So, we can use this key to decrypt the AES.encrypt
We can use this website for decrypt the file (http://aes.online-domain-tools.com/)

3. Image analysis
Given the encrypt.py, first, second

```python
from base64 import *

s=open('flag.jpg','rb').read()
s='-'.join(map(b16encode,list(s)))
s=map(''.join,zip(*(s.split('-'))))
with open('first','wb') as f:
    f.write(b16decode(s[0]))
with open('second','wb') as f:
    f.write(b16decode(s[1]))

s = open("second","rb").read()
with open('flag2','wb') as f:
	f.write(b16encode(s))
```

After have some analysis, the script are used to split the image file to two file. So, i have write the script to get the image back.

```python
a = open("flag","rb").read()
b = open("flag2","rb").read()
c = ""
for i in range(len(a)):
	asd = str(a[i]) + str(b[i])
	c = c + asd
with open('flag.jpg','wb') as f:
	f.write(c)
```

4. Image in image
After we get the image, i have found that there has an image inside the image. I have use 010editor to extract the image out.
After have some analysis the image, i have found that there has an photoshop file inside the image. We can extract the file in 0x1DD8. And we have to extract the background to png file and use the stegsolve to solve get the qrcode. Scan the qrcodde, we can get the flag.