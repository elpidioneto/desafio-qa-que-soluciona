
def beautiful_days(ini, end, k):
    beautiful_day_count = 0
    for day in range(ini, end+1):
        if((day - int(str(day)[::-1]))%k == 0):
            beautiful_day_count +=1
    
    return beautiful_day_count


### Teste 1: 
result = beautiful_days(20, 23, 6)
print(f"Teste 1: {result == 2}")

### Teste 2: 
result = beautiful_days(13, 45, 3)
print(f"Teste 2: {result == 33}")

### Teste 3: 
result = beautiful_days(1, 2000000, 2000000)
print(f"Teste 3: {result == 2998}")


### Teste 4: 
result = beautiful_days(1, 2000000, 23047885)
print(f"Teste 4: {result == 2998}")


