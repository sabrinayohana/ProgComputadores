def lista_troca_menor_primeiro(lista):
    menor_num = lista.index(min(lista))
    if menor_num == 0:
        return 0

    lista[0], lista[menor_num] = lista[menor_num], lista[0]
    return 1

n = int(input())  
lista = list(map(int, input().split()))  


trocas = lista_troca_menor_primeiro(lista)
print(trocas)
print(" ".join(map(str, lista)))
