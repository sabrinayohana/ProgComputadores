def dia_da_semana(h, d):
    dias = ["Domingo", "Segunda-feira", "Terca-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]

    dia_atual = 0
    for dia in dias:
        if dia == h:
            break
        dia_atual += 1
    
    dia_evento = (dia_atual + d) % 7
    return dias[dia_evento]


#testando
h = input("Digite o dia da semana: ")  
d = int(input("Digite a quantidade de dias até o evento: "))  

print(dia_da_semana(h, d))

