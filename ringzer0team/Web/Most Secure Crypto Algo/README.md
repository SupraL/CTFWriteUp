<h1>Most Secure Crypto Algo</h1>
<p>Given an javascript</p>

```javascript
$(".c_submit").click(function(event) {
				event.preventDefault();
				var k = CryptoJS.SHA256("\x93\x39\x02\x49\x83\x02\x82\xf3\x23\xf8\xd3\x13\x37");
				var u = $("#cuser").val();
				var p = $("#cpass").val();
				var t = true;
			
				if(u == "\x68\x34\x78\x30\x72") {
					if(!CryptoJS.AES.encrypt(p, CryptoJS.enc.Hex.parse(k.toString().substring(0,32)), { iv: CryptoJS.enc.Hex.parse(k.toString().substring(32,64)) }) == "ob1xQz5ms9hRkPTx+ZHbVg==") {
						t = false;
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



<p>Based on the code, we know that:<br/>
u = h4x0r
key = CryptoJS.enc.Hex.parse(k.toString().substring(0,32)).toString() //d8439507642eb76a4050adb27891d38a<br/>
iv = CryptoJS.enc.Hex.parse(k.toString().substring(32,64)).toString() //01fdb35ac5309d45a99f89c0a4ca0db6<br/>
encrypted = "ob1xQz5ms9hRkPTx+ZHbVg=="</p>

![text](http://i.imgur.com/i6pTVU4.png)


<p>So the password is PassW0RD!289%!*</p>