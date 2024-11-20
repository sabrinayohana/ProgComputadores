qtndFrango, qntdBife, qntdMassa = map(int, input().split())
pedidosF, pedidosB, pedidosM = map(int, input().split())

if pedidosF > qtndFrango:
    faltamFrango = pedidosF - qtndFrango
else:
    faltamFrango = 0

if pedidosB > qntdBife:
    faltamBife = pedidosB - qntdBife
else:
    faltamBife = 0

if pedidosM > qntdMassa:
    faltamMassa = pedidosM - qntdMassa
else:
    faltamMassa = 0

naoAtendidos = faltamFrango + faltamBife + faltamMassa

print(naoAtendidos)
