valor_item = int(input())
quantidade_itens = int(input())
valor_pago = int(input())

valor_total = valor_item * quantidade_itens
troco = valor_pago - valor_total

print("A pagar:", valor_total)
print("Troco  :", troco) 