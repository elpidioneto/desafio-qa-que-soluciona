def escadaria(n):

    try:
        degraus = int(n)
        for i in range(1,degraus + 1):
            print(" " * (degraus - i), "#" * i)
    except:
        print("valor informado deve ser númerico refaça a operação")
        escadaria(input("Digite o número de degraus "))

escadaria(input("Digite o número de degraus "))
