alcool, gasolina, km_A, km_G = map(float, input().split())

rendimentoA = alcool / km_A
rendimentoG = gasolina / km_G

if rendimentoA < rendimentoG:
    print('A')
else:
    print('G')

