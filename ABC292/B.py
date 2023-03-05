people_in_team , event_counter = map(int,input().split(" "))
member = []
for c in range(people_in_team):
    member.append(0)
for c in range(event_counter):
    a,b=map(int,input().split(" "))
    if a==1:
        member[b-1]+=1
    elif a==2:
        member[b-1]+=2
    else:
        if member[b-1]<2:
            print("No")
        else:
            print("Yes")