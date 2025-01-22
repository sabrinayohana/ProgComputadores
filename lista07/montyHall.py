n = int(input())
vitorias = 0

for _ in range(n):
    porta_com_carro = int(input())
    if porta_com_carro != 1:
        vitorias += 1

print(vitorias)
