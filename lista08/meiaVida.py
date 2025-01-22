def calcular_tempo(s, mi):
    tempo_total = 0  
    massa = mi  
    
    while massa >= 0.5:
        massa /= 2
        tempo_total += s
    
    dias = tempo_total // 86400
    horas = (tempo_total % 86400) // 3600
    minutos = (tempo_total % 3600) // 60
    segundos = tempo_total % 60
    
    print(f"{dias} dias {horas:02}:{minutos:02}:{segundos:02}")

s, mi = map(int, input().split())
calcular_tempo(s, mi)
