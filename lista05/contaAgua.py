consumo = int(input())  

valor_total = 7

if consumo > 10:  
    if consumo <= 30:  
        valor_total += (consumo - 10) * 1  
    elif consumo <= 100:  
        valor_total += (30 - 10) * 1  
        valor_total += (consumo - 30) * 2  
    else:  
        valor_total += (30 - 10) * 1  
        valor_total += (100 - 30) * 2  
        valor_total += (consumo - 100) * 5

print(valor_total)
