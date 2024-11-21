andar1 = int(input())  
andar2 = int(input())  
andar3 = int(input()) 

tempo_a1 = (andar1 * 0 + andar2 * 1 + andar3 * 2) * 2  
tempo_a2 = (andar1 * 1 + andar2 * 0 + andar3 * 1) * 2  
tempo_a3 = (andar1 * 2 + andar2 * 1 + andar3 * 0) * 2  

if tempo_a1 <= tempo_a2 and tempo_a1 <= tempo_a3:
    menor_tempo = tempo_a1
elif tempo_a2 <= tempo_a1 and tempo_a2 <= tempo_a3:
    menor_tempo = tempo_a2
else:
    menor_tempo = tempo_a3

print(menor_tempo)
