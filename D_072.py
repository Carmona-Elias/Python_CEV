nr = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezasseis', 'Dezassete', 'Dezoito', 'Dezanove', 'Vinte')
while True:
    usuario = int(input('Digite um numero entre [0 - 20]: '))
    if not 0 <= usuario <= 20:
        print('Valor invalido. Tente Novamente.')
        usuario = int(input('Digite um numero entre [0 - 20]: '))
    print(f'Voce digitou o nr {nr[usuario]}')
    usuario = str(input('Quer continuar [S/ N]: ')).strip().upper()[0]
    if usuario in 'N':
        break
print('Programa Terminado com sucesso!!')
