n = int(input())
numeros = list(map(int, input().split()))

media = sum(numeros) / n

mediaBaixa = 0
naMedia_ou_acima = 0

for numero in numeros:
    if numero < media:
        mediaBaixa += 1
    else:
        naMedia_ou_acima += 1

print(f"{media:.1f}")
print(mediaBaixa)
print(naMedia_ou_acima)
