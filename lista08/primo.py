def eh_primo(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def proximo_primo(n):
    num = n + 1
    while not eh_primo(num):
        num += 1
    return num

n = int(input())
print(proximo_primo(n))
