from math import sqrt
pit = []
pit_cord = []
x_s,y_s = map(int,input().split())
way_s = 0
x_d,y_d = map(int,input().split())
way_d = 0
number = int(input())
for i in range(number):
    pit_cord = []
    pit_cord = list(map(int,input().split()))
    pit.append(pit_cord)

for i in range(len(pit)):
    way_s = sqrt(pow(pit[i][0] - x_s,2)+pow(pit[i][1] - y_s,2))
    way_d = sqrt(pow(pit[i][0] - x_d,2)+pow(pit[i][1] - y_d,2))

    if way_d/2 >= way_s:
        print(i+1)
        break

else:
    print("NO")
