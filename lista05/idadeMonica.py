idadeMonica = int (input())
idadeFilho1 = int (input())
idadeFilho2 = int (input())

idadeFilho3 = idadeMonica - (idadeFilho1 + idadeFilho2)

maisVelho = max(idadeFilho1, idadeFilho2, idadeFilho3)
print(maisVelho)