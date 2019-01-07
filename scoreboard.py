n,m = map(int,input().split())
main_array = []
color_array = []
flag = False

for i in range(n):
    array =[]
    array = list(input())
    color_array.append(array)

for i in range(n):
    array =[]
    array = list(map(int,input().split()))
    main_array.append(array)

for i in range(n):
    for j in range(m):
        
        if color_array[i][j] == "R":
            if main_array[i][j] == 4 or main_array[i][j] == 5 or main_array[i][j] == 6 or main_array[i][j] == 7:
                continue
            else:
                flag = True
                break
        elif color_array[i][j] == "G":
            if main_array[i][j] == 2 or main_array[i][j] == 3 or main_array[i][j] == 6 or main_array[i][j] == 7:
                continue
            else:
                flag = True
                break
        elif color_array[i][j] == "B":
            if main_array[i][j] == 1 or main_array[i][j] == 3 or main_array[i][j] == 5 or main_array[i][j] == 7:
                continue
            else:
                flag = True
                break
        else:
            continue

    if flag:
        print("NO")
        break
    
else:
    print("YES")
