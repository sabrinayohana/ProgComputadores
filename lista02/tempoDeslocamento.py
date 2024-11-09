distancia_cidades = int(input())
velocidade = int(input())
tempo_gasto = distancia_cidades / velocidade

horas = int(tempo_gasto)
minutos = int((tempo_gasto - horas) * 60)


print(f"{horas:02}:{minutos:02}")

