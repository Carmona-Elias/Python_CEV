valorCasa = float(input('Qual e o valor do imovel que pretende adquirir? R$'))
salario = float(input('Quanto e que voce aufere por mes? R$'))
anos = int(input('Durante quantos anos pretende pagar o emprestimo? '))
prestacao = valorCasa / (anos * 12)
print(f'Para efectuar um emprestimo de R${valorCasa:.2f} em {anos} anos, a prestacao sera de R${prestacao:.2f}')
if prestacao > salario * 0.30:
    print(f'\033[1;31m Lamentamos informar que o seu emprestimo foi recusado. \033[m')
else:
    print(f'\033[1;32mParabens! O seu emprestimo foi aprovado!!\033[m')
