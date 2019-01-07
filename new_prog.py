amount =  int(input())
factories = list(map(int,input().split()))
peicent = list(map(int,input().split()))
earn = []
earn_reserv = []

for i in range(amount):
    earn_1_fac = 0

    if peicent[i] == 0:
        earn_1_fac = 0
    else:
        earn_1_fac = factories[i]*peicent[i]/100
    earn.append(earn_1_fac)
earn_reserv = earn.copy()

for j in range(0,amount-1):
    for i in range(0,amount-1-j):
        if earn[i] < earn[i+1]:
            earn[i], earn[i+1] = earn[i+1], earn[i]



print(earn_reserv.index(earn[0])+1)

