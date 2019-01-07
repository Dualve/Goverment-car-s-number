number_e_list = list("2.7182818284590452353602875")

exp = int(input())

if exp == 25:
    print("".join(number_e_list))
elif exp == 0:
    print(3)
else:
    if int(number_e_list[exp+2]) >= 5:
          number_e_list[exp+1] = str(int(number_e_list[exp+1])+1)
    print("".join(number_e_list[:exp+2]))


