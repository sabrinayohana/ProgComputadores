n = int(input())
numeros = list(map(int, input().split()))

media = sum(numeros) / n
abaixo = []
acima_ou_igual = []

for numero in numeros:
    if numero < media:
        abaixo.append(numero)
    else:
        acima_ou_igual.append(numero)

print(f"{media:.1f}")
print(len(abaixo), " ".join(map(str, abaixo)))
print(len(acima_ou_igual), " ".join(map(str, acima_ou_igual)))
