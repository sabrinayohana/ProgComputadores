capacidade_cabine = int (input())
total_alunos = int (input())

maximo_viagem = capacidade_cabine - 1
viagens = (total_alunos + maximo_viagem - 1) // maximo_viagem

print(viagens)