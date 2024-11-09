nota_maxima, nota_aluno = map (float, input().split())
nota_normalizada = (nota_aluno/nota_maxima)*100
print(int(nota_normalizada))