from datetime import date
SomaMaior = SomaMenor = 0
for c in range(7):
    ano = int(input('Qual e o seu ano de nascimento? '))
    idade = date.today().year - ano
    if idade >= 21:
        SomaMaior += 1
    else:
        SomaMenor += 1
print(f'Ao todo {SomaMaior} pessoas sao maiores de idade e {SomaMenor} Menores.')
