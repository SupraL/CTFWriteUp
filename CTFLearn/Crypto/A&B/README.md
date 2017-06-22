<h1>A&B</h1>

<h3>Question</h3>
<p>If A&B=(A+B)/2, what does this equal?

```
8&4,(19&3)&13,2&0,9&5{60&-20,9&7,10&8,(30&20)&13, 11&7,30&8,8&-2,29&7,68&-18,26&6,(30&-6)&28,25&5}
```

Convert it into letters once you find it.</p>

<h3>Solution</h3>

```python
#A&B = (A+B)/2
flag = "8&4,(19&3)&13,2&0,9&5,60&-20,9&7,10&8,(30&20)&13, 11&7,30&8,8&-2,29&7,68&-18,26&6,(30&-6)&28,25&5"


def cal(eq):
    if "(" in eq:
        eq = eq.replace("(","").replace(")&","@")
        arr = eq.split("@")
        ans1 = cal(arr[0])
        ans2 = cal(str(ans1) + "&" + arr[1])
        return ans2
    else:
        num = eq.split("&")
        ans = (int(num[0]) + int(num[1]))/2
        return ans

#8&4 = (8+4)/2 = 6 = f , and so on.
dictWord = "abcdefghijklmnopqrstuvwxyz"
eqArray = flag.split(",")
output = ""
for eq in eqArray:
    output = output + dictWord[cal(eq)-1]

print output
```