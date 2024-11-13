consumo = int(input())  
distancia = int(input())  
tanque = int(input()) 

litros_necessarios = distancia / consumo
litros_comprar = litros_necessarios - tanque

if litros_comprar < 0:
    litros_comprar = 0.0

print(f"{litros_comprar:.1f}")
