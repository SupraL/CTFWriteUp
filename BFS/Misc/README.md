<h1>Misc - 100</h1>
<p>Given an pcap file , and i found that there has some FTP transmission there. Finally i have found that:</p>
<p>A zip file contains key.txt</p>
(http://i.imgur.com/Nx3O3UQ.png)

<p>Public key file</p>
![text](http://i.imgur.com/AB7GPMo.png)

<p>Private key file</p>
![text](http://i.imgur.com/Lino5F6.png)

<p>It seems key.txt are encrypted. So, we try to decrypt it with private key</p>
```
openssl rsautl -decrypt -in C:\Users\Admin\Desktop\key.txt -out plaintext -inkey C:\Users\Admin\Desktop\privateKey.bin
```

![text](http://i.imgur.com/19HESo1.png)