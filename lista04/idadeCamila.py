idade1 = int(input())
idade2 = int(input())
idade3 = int(input())

if (idade1 >= idade2 >= idade3) or (idade1 <= idade2 <= idade3):
    print(idade2)
elif (idade2 >= idade1 >= idade3) or (idade2 <= idade1 <= idade3):
    print(idade1)
else:
    print(idade3)


