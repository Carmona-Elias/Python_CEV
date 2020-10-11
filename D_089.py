Aluno = []
Resultados = []
Nome = []
opcao = 0
while True:
    nome = str(input('Nome do aluno: ')).strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    Aluno.append([nome, [nota1, nota2], media])
    usuario = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while usuario not in 'SN':
        print('Opaco Inavlida. Tente Novamente.')
        usuario = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if usuario in 'N':
        break
print('-=-'*10)
print(f'{"No.":<4} {"NOME":<10} {"MEDIA":>8}')
print('-'*30)
for pos, estudante in enumerate(Aluno):
    print(f'{pos:<4} {estudante[0]:<10}  {estudante[2]:>8.1f}')
while opcao != 999:
    opcao = int(input('Digite o No. para ver os dados do estudante. [999 para sair]: '))
    for pos, estudante in enumerate(Aluno):
        if opcao == pos:
            print(f'As notas do(a) {estudante[0]} sao {estudante[1][0]} e {estudante[1][1]}')
            break
    print('-'*25)
print('Fim do Programa')

