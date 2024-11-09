comprimento_estrada, distância_entre_pedagios = map(int, input().split())  
custo_percuso, valor_pedagio = map(int, input().split()) 

custo_por_km = comprimento_estrada * custo_percuso

quantidade_pedagios = comprimento_estrada // distância_entre_pedagios
custo_pedagios = quantidade_pedagios * valor_pedagio

custo_total = custo_por_km + custo_pedagios
print(custo_total)
