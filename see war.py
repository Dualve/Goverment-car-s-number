import copy

n,m = map(int,input().split())
main_field = []
counter = 0
error = 0

for _ in range(n):
    raw = []
    raw = list(input())
    main_field.append(raw)

for i in range(n):
    for j in range(m):
        if main_field[i][j] == ".":
            main_field[i][j] = 1
        elif main_field[i][j] == "*":
            main_field[i][j] = 0

help_field = copy.deepcopy(main_field)

for i in range(n):
    for j in range(m):
        if not main_field[i][j]:
            if i != 0:  
                help_field[i-1][j] = 0
            if i != n-1:  
                help_field[i+1][j] = 0
            if j != m-1:
                help_field[i][j+1] = 0
            if j != 0:
                help_field[i][j-1] = 0

for i in range(n):
    for j in range(m):
        if main_field[i][j] and main_field[i][j] == help_field[i][j]:
            counter+=1

print(counter)
