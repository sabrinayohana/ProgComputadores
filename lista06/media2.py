def media_lista(lista):
    soma = sum(lista)  # Calcula a soma dos elementos da lista
    quantidade = len(lista)  # Conta quantos elementos existem na lista
    media = soma // quantidade  # Calcula a média aritmética como um inteiro
    return media

# Entrada de dados
n = int(input().strip())  # Lê o número de elementos na lista
lista = [int(input().strip()) for _ in range(n)]  # Lê cada elemento da lista

# Calcula a média
resultado = media_lista(lista)

# Exibe o resultado
print(resultado)
