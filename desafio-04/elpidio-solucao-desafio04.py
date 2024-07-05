def mediana(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 1 : 
        return arr[n // 2]
    else:
        med1 = arr[n // 2 - 1] 
        med2 = arr[n // 2]
        return(med1 + med2) // 2


def activity_notifications(despesas_diarias, 
                           dias_anteriores):
    notifications = 0
    init_max = (len(despesas_diarias)-1) - (dias_anteriores)
    for i in range(init_max):
        dia_hoje = dias_anteriores+i
        despesas_periodo = despesas_diarias[i:dias_anteriores+i]
        
        m = mediana(despesas_periodo)
        if(m*2 <= (despesas_diarias[dia_hoje])):
            notifications +=1
    return notifications


print(f"Teste 1: {activity_notifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5) == 2}")

print(f"Teste 2: {activity_notifications([1, 2, 3, 4, 4],4)== 0}")

print(f"Teste 3: {activity_notifications([10, 20, 30, 40, 50, 60, 70, 80, 90],5) == 1}")

print(f"Teste 4: {activity_notifications([1, 2, 100, 2, 2, 2, 2, 2],4) == 0}")