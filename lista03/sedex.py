diametro_da_bola = int(input())
altura, largura, profundidade = map(int, input().split())

if diametro_da_bola <= altura and diametro_da_bola <= largura and diametro_da_bola <= profundidade:
    print('S')
else:
    print('N')
