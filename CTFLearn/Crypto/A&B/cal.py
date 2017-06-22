#A&B = (A+B)/2
flag = "8&4,(19&3)&13,2&0,9&5,60&-20,9&7,10&8,(30&20)&13, 11&7,30&8,8&-2,29&7,68&-18,26&6,(30&-6)&28,25&5"


def cal(eq):
    if "(" in eq:
        arr = eq.replace("(","").replace(")&","@").split("@")
        return cal(str(cal(arr[0])) + "&" + arr[1])
    else:
        num = eq.split("&")
        return (int(num[0]) + int(num[1]))/2

dictWord = "abcdefghijklmnopqrstuvwxyz"
eqArray = flag.split(",")
output = ""
for eq in eqArray:
    output = output + dictWord[cal(eq)-1]

print output
