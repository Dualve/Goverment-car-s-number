array = [[],[],[],[]]
array[0] = str(input())
array[1] = str(input())
array[2] = str(input())
array[3] = str(input())

flag = False

for i in range(4):
    for j in range(4):
        print(array[i][j], end = " ")
    print("\n")

for i in range(3):
    for j in range(3):
        
        if array[i][j] == array[i][j+1]:
            if array[i+1][j] == array[i+1][j+1] and array[i+1][j] == array[i][j]:
                print("No")
                flag = True
                break

    if flag:
        break
else:
    print("Yes")
