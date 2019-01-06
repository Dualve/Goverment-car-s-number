n,s = map(int,input().split())
cost = list(map(int,input().split()))
cost.sort()
counter = 0
for i in range(n):
    if s < cost[i]:
        break
    else:
        s -= cost[i]
        counter +=1
print(counter)
