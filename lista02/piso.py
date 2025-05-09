comprimento = int(input())
largura = int(input())
 
piso1 = comprimento * largura + (comprimento - 1) * (largura - 1)
piso2 = (2 * comprimento - 2) + (2 * largura - 2)
 
print(piso1)
print(piso2)
