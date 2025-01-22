a, b = map(int, input().split())  

resultado = []  
for i in range(a, b + 1, a):  
    resultado.append(str(i))  

print(" ".join(resultado))  
