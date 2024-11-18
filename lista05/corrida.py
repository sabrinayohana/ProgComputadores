num1, distancia1, km1 = map(int, input().split())
num2, distancia2, km2 = map(int, input().split())

velocidade1 = km1 / 3.6
velocidade2 = km2 / 3.6

tempo1 = distancia1 / velocidade1
tempo2 = distancia2 / velocidade2

if tempo1 < tempo2:
    print(num1)
else:
    print(num2)