n = str(input())
a = str()
for c in range(len(str(n))):
    if str(n)[c]=="1":
        a = a + "0"
    else:
        a = a + "1"
print(a)