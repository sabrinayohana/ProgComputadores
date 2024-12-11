def media_lista(lista):
    soma = sum (lista)
    quantidade = len (lista)
    media = soma//quantidade
    return media

lista = list(map(int, input().split()))
resultado = media_lista(lista)
print (resultado)