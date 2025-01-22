caso = 1
while True:
    try:
        n = int(input())  
        oleosidade = list(map(float, input().split()))  
        teclas = sorted(enumerate(oleosidade), key=lambda x: (-x[1], x[0]))
        senha = ''.join(str(teclas[i][0]) for i in range(n))

        print(f"Caso {caso}: {senha}")
        caso += 1
    except EOFError:
        break  
