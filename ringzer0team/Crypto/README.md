<h1>File recovery</h1>
<p>Solution</p>

```bash
openssl rsautl -decrypt -in flag.enc -out flag.dec -inkey private.pem
```

<p>flag.dec : FLAG-vOAM5ZcReMNzJqOfxLauakHx</p>

======

<h1>Public key recovery</h1>
<p>Solution</p>

```bash
openssl rsa -in private.pem -pubout -out pubkey.pem
```

<p>flag.dec : FLAG-9869O2dQ43d1r116kfD0Sj5n</p>