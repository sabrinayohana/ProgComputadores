c = int(input())
caixas = [int(input()) for _ in range(c)]
saldo = 100
maior_saldo = saldo

for valor in caixas:
    saldo += valor  
    if saldo > maior_saldo:
        maior_saldo = saldo

print(maior_saldo)
