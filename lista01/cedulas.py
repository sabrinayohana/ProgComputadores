n = int(input())
print(n)

notas_100 = n // 100
n = n % 100

notas_50 = n // 50
n = n % 50

notas_20 = n // 20
n = n % 20

notas_10 = n // 10
n = n % 10

notas_5 = n // 5
n = n % 5

notas_2 = n // 2
n = n % 2

notas_1 = n // 1

print(f"{notas_100} nota(s) de R$ 100,00")
print(f"{notas_50} nota(s) de R$ 50,00")
print(f"{notas_20} nota(s) de R$ 20,00")
print(f"{notas_10} nota(s) de R$ 10,00")
print(f"{notas_5} nota(s) de R$ 5,00")
print(f"{notas_2} nota(s) de R$ 2,00")
print(f"{notas_1} nota(s) de R$ 1,00")
