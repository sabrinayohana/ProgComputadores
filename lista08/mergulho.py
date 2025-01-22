N, R = map(int, input().split())

retornaram = set(map(int, input().split()))
todos_voluntarios = set(range(1, N + 1))
nao_retornaram = sorted(todos_voluntarios - retornaram)

if nao_retornaram:
    print(" ".join(map(str, nao_retornaram)) + " ")
else:
    print("*")
