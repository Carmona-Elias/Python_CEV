frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
# inverso = ''
# for l in range(len(junto) - 1, -1, -1):
#     inverso += junto[l]
print(f'O inverso de {frase} e {inverso},logo, ', end='')
if junto == inverso:
    print('Temos um PALINDROMO.')
else:
    print('Nao e um PALINDROMO.')


