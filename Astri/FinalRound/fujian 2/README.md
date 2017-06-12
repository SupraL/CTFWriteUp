<h1>fujian</h1>

```
python RsaCtfTool.py --publickey public.key --private

-----BEGIN RSA PRIVATE KEY-----
MIGqAgEAAiEA2Z6VIpam2WDfwlBKulRblELWCnuekwr/RRx47FXVVesCAwEAAQIg
BFR7cyy8NScQTLV8RyjWiZtExJlPricT1rWUvA9SKkECEQDj0hOwo8lVH5+x6418
Pa81AhEA9Il8qrqAI2vcG1k4XEv0nwIQCzQuobY8VYJboS1bZOvHrQIQJRmi32gy
Pq2DlGah5WbkswIRAJiTlYmnkZz69I90hqeNhGM=
-----END RSA PRIVATE KEY-----
```

```
openssl rsautl -decrypt -in encrypted.message1 -out plaintext -inkey private.key
openssl rsautl -decrypt -in encrypted.message2 -out plaintext2 -inkey private.key
openssl rsautl -decrypt -in encrypted.message3 -out plaintext3 -inkey private.key

cat plain* | tr -d "\n"
```