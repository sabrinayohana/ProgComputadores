a1, a2, a3, a4 = map(int, input().split())

areas = sorted([a1, a2, a3, a4])

if areas[0] * areas[3] == areas[1] * areas[2]:
    print('S')
else:
    print('N')
