import requests

enc_flag = "fR4aHWwuFCYYVydFRxMqHhhCKBseH1dbFygrRxIWJ1UYFhotFjA="
flag = "Flag:{asdqwdfasfdawfefqwdqwdadwqadawd}"
for i in range(32,127):
    r = requests.get("http://localhost/enc.php?word=" + flag + chr(i))
    #print enc_flag[len(flag)+2:len(flag)+2+1] + ":" + r.text[-1:]
    print r.text + ":" + chr(i)
