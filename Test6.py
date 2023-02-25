a = str(input())
b = ""
for c in range(0,len(a)):
  if a[c]=="0":
    b=b+"1"
  else a[c]=="1":
    b=b+"0"
print(b)
