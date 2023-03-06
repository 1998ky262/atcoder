n,m=map(int,input().split(" "))
point = input().split(" ")
answer = input().split(" ")
score = int(0)
for b in range(len(answer)):
  score+=int(point[int(answer[b])-1])
print(score)
# リラックスして思考を整理すると、間違いに気づきます。
