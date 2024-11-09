nome = input ()
salario_fixo = float (input())
total_de_vendas = float (input())
comissao = (total_de_vendas/100) * 15
total_a_receber = salario_fixo + comissao
print (nome)
print ("R$ {:.2f}".format(total_a_receber)) 