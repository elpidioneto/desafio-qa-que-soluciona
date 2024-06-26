try:
    degraus = int(input("digite o número de degraus desejado: "))
    for i in range(1,degraus + 1):
        espaco = degraus - i
        print(" " * espaco, "#" * i)
except:
    print("valor informado deve ser númerico refaça a operação")
