a, b, c = map(int, input().split())

if a >= b and a >= c:
    hipotenusa = a
    cateto1, cateto2 = b, c
elif b >= a and b >= c:
    hipotenusa = b
    cateto1, cateto2 = a, c
else:
    hipotenusa = c
    cateto1, cateto2 = a, b



if cateto1 + cateto2 <= hipotenusa or a + b <= c or a + c <= b or b + c <= a:
    print('n')  
else:
   
    if cateto1**2 + cateto2**2 > hipotenusa**2:
        print('a')  
    elif cateto1**2 + cateto2**2 == hipotenusa**2:
        print('r')  
    else:
        print('o')  
