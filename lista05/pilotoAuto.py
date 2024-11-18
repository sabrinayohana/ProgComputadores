a = int (input())
b = int (input())
c = int (input())

acelerar = 1
desacelerar = -1
manter_velocidade = 0

if (b-a) < (c-b):
    print (acelerar)
elif (b-a)>(c-b):
    print (desacelerar)
elif (b-a) == (c-b):
    print(manter_velocidade)