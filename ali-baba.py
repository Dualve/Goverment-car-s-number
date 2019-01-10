n,m = map(int,input().split())
cost = list(map(int,input().split()))
cost.sort()
cost.reverse()
counter = 0
res = 0
while m > counter:
    if cost[counter] > 0:
        res += cost[counter]
        counter+=1
    else:
        break
print(res)
