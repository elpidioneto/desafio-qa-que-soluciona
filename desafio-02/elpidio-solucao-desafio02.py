def countingValleys(caminho):
    vales = 0
    no_vale = False
    trecho = 0

    for direcao in caminho:
        if(direcao == "U"):
            trecho += 1
        elif(direcao == "D"):
            trecho -= 1
        
        if(trecho < 0):
            no_vale = True

        elif(no_vale and trecho == 0):
            vales += 1
            no_vale = False


    return vales

### Teste 1: 
count = countingValleys("DDUUDDUDUUUD")
print(f"Teste 1 {count == 2}")

### Teste 2: 
count = countingValleys("UDUUUDUDDD")
print(f"Teste 2 {count == 0}")

### Teste 3: 
count = countingValleys("DUDUDUDUDUDUDU")
print(f"Teste 3 {count == 7}")

### Teste 4: 
count = countingValleys("DDUUUUDDDUUUDDDU")
print(f"Teste 4 {count == 3}")