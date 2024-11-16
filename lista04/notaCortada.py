b = int(input())
t = int(input())

altura = 70
comprimento = 160

if not (0 <= b <= comprimento and 0 <= t <= comprimento):
    print(0)  
else:
    nota = altura * comprimento
    lado_esquerdo = ((b + t) * altura) / 2
    lado_direito = nota - lado_esquerdo

    if lado_esquerdo > nota / 2:
        print(1)  
    elif lado_direito > nota / 2:
        print(2)  
    else:
        print(0)  
