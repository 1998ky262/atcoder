a = input()
b = map(int,input.split(" "))
pp = 0
confirm = 0
while confirm == 1:
  confirm = 0
  for count of range(a):
    if b[count-1]%2 == 1:
      confirm = 0
      break
    else:
      b[count-1]=b[count-1]/2
      confirm = 1
  if confirm == 1:
    pp+=1
print(pp)
