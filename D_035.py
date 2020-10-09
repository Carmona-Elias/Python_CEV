print('-=-'*20)
print('Analisador de Triangulo')
print('-=-'*20)
r1 = int(input('Digite o primeiro comprimento: '))
r2 = int(input('Digite o segundo comprimento: '))
r3 = int(input('Digite o terceiro comprimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmenntos acima podem formar um triangulo!')
else:
    print('Os segmentos acima NAO podem formar um triangulo!')

