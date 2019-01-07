number = int(input())
pieces = 1

for i in range(number):

    if number == 0:
        break
    elif number == 1:
        pieces +=1
        break
    else:
        pieces += number-i

print(pieces)
