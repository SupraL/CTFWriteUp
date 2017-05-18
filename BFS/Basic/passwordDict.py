from itertools import product
passwordList = product("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", repeat=4)
with open("password.lst","w") as file:
    for i in passwordList:
        file.write("ISCC" + ''.join(i) + "\n")
