a = int(input())
b = input().split(" ")
pp = 0
confirm = 1
while confirm == 1:
  confirm = 0
  for count in range(a):
    if int(b[count-1])%2 == 1:
      confirm = 0
      break
    else:
      b[count-1]=int(b[count-1])/2
      confirm = 1
  if confirm == 1:
    pp+=1
print(pp)
# 簡単な問題なのにめっちゃ長くてくさ
