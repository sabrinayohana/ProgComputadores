def calcular_dias(c):
    dias = 0
    while c > 1:
        c /= 2
        dias += 1
    return dias

n = int(input())

for _ in range(n):
    c = float(input())
    print(f"{calcular_dias(c)} dias")
