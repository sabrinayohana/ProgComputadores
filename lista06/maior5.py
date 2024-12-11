def maior5 (a, b, c, d, e):
   return max(a, b, c, d, e)
    
#testando
a, b, c, d, e = map(int, input().split())
total = maior5 (a, b, c, d, e)
print (total)