<h1>Basic - 150 (PHP_encrypt_1)</h1>
<p>Given an encrypted string:fR4aHWwuFCYYVydFRxMqHhhCKBseH1dbFygrRxIWJ1UYFhotFjA= and enc.php</p>
<p>Solution:<br/>
Guess it in each characters. (web150.py)</p>

---
<h1>Basic - 150 (QrCode)</h1>
<p>Given a qrcode<br/>
And i found that there has a zip file inside the image. And after i have decode the qrcode, i got a string "The password of the router is our flag". It seems the zip file contains the router password</p>

![text](http://i.imgur.com/97hdaMD.png)

<p>
After i extract all the file from image. I have got 2B6.zip, and it require the password to extract. My idea is try to bruteforce it.
</p>

![text](http://i.imgur.com/KUNOxtt.png)

<p>Finally i have got C8-E7-D8-E8-E5-88_handshake.cap and one text file. The text file contains an hint said that the first four characters is "ICSS" and the following four characters is upper alphanumeric and digit. After have some analysis on the .cap file, i have found four packet which seems like contains the router password.</p>

![text](http://i.imgur.com/ctry38w.png)

<p> Now, we can use aircrack-ng to bruteforce the router password.<br/>
First, we have to generate the password dictionary file.</p>

```python
from itertools import product
passwordList = product("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", repeat=4)
with open("password.lst","w") as file:
    for i in passwordList:
        file.write("ISCC" + ''.join(i) + "\n")
```

![text](http://i.imgur.com/K7W5sFW.png)

<p>Finally, we got the password ISCC16BA<p>