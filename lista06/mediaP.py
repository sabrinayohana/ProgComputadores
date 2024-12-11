def media_ponderada(v1, p1, v2, p2):
    media = (v1*p1 + v2*p2) / (p1 + p2)
    return media

v1, v2 = map (float, input().split())
p1, p2 = map (float, input().split())
resultado = media_ponderada(v1, p1, v2, p2)
print (resultado)