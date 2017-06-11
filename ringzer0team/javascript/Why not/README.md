<h1>Why not</h1>
<p>Given an javascript</p>

```javascript
// Look's like weak JavaScript auth script :)
			$(".c_submit").click(function(event) {
				event.preventDefault();
				var k = new Array(176,214,205,246,264,255,227,237,242,244,265,270,283);
				var u = $("#cuser").val();
				var p = $("#cpass").val();
				var t = true;
			
				if(u == "administrator") {
					for(i = 0; i < u.length; i++) {
						if((u.charCodeAt(i) + p.charCodeAt(i) + i * 10) != k[i]) {
							$("#cresponse").html("<div class='alert alert-danger'>Wrong password sorry.</div>");
							t = false;
							break;
						}
					}
				} else {
					$("#cresponse").html("<div class='alert alert-danger'>Wrong password sorry.</div>");
					t = false;
				}
				if(t) {
					if(document.location.href.indexOf("?p=") == -1) {
						document.location = document.location.href + "?p=" + p;
               			}
				}
			});

```

<p>Solution</p>

```python
for i in range(len(k)):
	for j in range(48,127):
		if ord(u[i]) + ord(chr(j)) + i * 10 == k[i]:
			password = password + chr(j)
	print password
```

<p>Output:<br/>
O
Oh
OhL
OhLo
OhLor
OhLord
OhLord4
OhLord43
OhLord430
OhLord4309
OhLord43091
OhLord430911
OhLord4309111
</p>
