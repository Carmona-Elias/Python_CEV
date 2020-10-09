salario = float(input('Digite o salario actual: '))
print(f'O seu salario e de {salario}')
if salario <= 1250:
    SalarioActual = ((salario*0.15) + salario)
else:
    SalarioActual = ((salario*0.10) + salario)
print(f'Com aumento o seu salario vale R$ {SalarioActual:.2f}')
