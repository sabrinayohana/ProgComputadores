senha_correta = 9842
senha = int(input())

while senha != senha_correta:
    print("Senha Invalida!")
    senha = int(input()) 
print("Acesso Permitido.")
