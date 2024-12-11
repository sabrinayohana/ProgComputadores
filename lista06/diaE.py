def dia(dia, mes, ano):
    meses = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    
    if mes < 1 or mes > 12:
        return "Data Invalida"
    
    if mes == 2:  
        if dia < 1 or dia > 28:
            return "Data Invalida"
    elif mes in [4, 6, 9, 11]:  
        if dia < 1 or dia > 30:
            return "Data Invalida"
    else: 
        if dia < 1 or dia > 31:
            return "Data Invalida"

    dia_formatado = f"{dia:02d}"
    return f"{dia_formatado} de {meses[mes - 1]} de {ano}"

# Função para ler entradas do usuário
def ler_entradas():
    dia_input = int(input("Digite o dia: "))
    mes_input = int(input("Digite o mês: "))
    ano_input = int(input("Digite o ano: "))
    
    # Chamando a função dia com as entradas e mostrando o resultado
    print(dia(dia_input, mes_input, ano_input))

# Chamando a função para testar com entrada do usuário
ler_entradas()
