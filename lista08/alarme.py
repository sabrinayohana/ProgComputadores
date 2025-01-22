while True:
    H1, M1, H2, M2 = map(int, input().split())
    if H1 == 0 and M1 == 0 and H2 == 0 and M2 == 0:
        break
    
    minutos_inicio = H1 * 60 + M1
    minutos_fim = H2 * 60 + M2
    
    if minutos_fim <= minutos_inicio:
        minutos_fim += 24 * 60
    
    print(minutos_fim - minutos_inicio)
