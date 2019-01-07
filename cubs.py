cub = int(input())
max_cub = 0

while True:
    max_cub += 1
    
    if cub < max_cub:
        break
    
    cub -= max_cub
    
print(max_cub - 1)
