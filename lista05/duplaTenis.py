a = int(input())
b = int(input())
c = int(input())
d = int(input())

soma_total = a + b + c + d
menor_diferenca = 100000 

combinacoes = [(a, b), (a, c), (a, d), (b, c), (b, d), (c, d)]

for time1 in combinacoes:
    nivel_time1 = time1[0] + time1[1]
    nivel_time2 = soma_total - nivel_time1
   
    if nivel_time1 > nivel_time2:
        diferenca = nivel_time1 - nivel_time2
    else:
        diferenca = nivel_time2 - nivel_time1

    if diferenca < menor_diferenca:
        menor_diferenca = diferenca
        
print(menor_diferenca)


