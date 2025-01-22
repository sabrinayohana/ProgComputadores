n = int(input())
sequencia = [int(input()) for _ in range(n)]

marcados = 1 
ultimo_marcado = sequencia[0]

for i in range(1, n):
    if sequencia[i] != ultimo_marcado:
        marcados += 1
        ultimo_marcado = sequencia[i]
        
print(marcados)
