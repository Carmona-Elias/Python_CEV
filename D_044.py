preco = float(input('Digite o preco do produto R$'))
condicaoPagamento = int(input('Qual e a condicao de pagamento? \n'
                              '[ 1 ] Dinheiro/ Cheque\n'
                              '[ 2 ] Cartao\n'
                              '[ 3 ] 2x Cartao\n'
                              '[ 4 ] 3x ou Mais no Cartao\n'
                              'Sua opcao: '))
if condicaoPagamento == 4:
    totparcelas = int(input('Quantas parceas? '))
print(f'Sua compra de R${preco:.2f} ', end='')
if condicaoPagamento == 1:
    print(f'vai custar {preco - preco*0.10}')
elif condicaoPagamento == 2:
    print(f'vai custar {preco - preco*0.05}')
elif condicaoPagamento == 3:
    parcela = preco / 2
    print(f'sera parcelada em 2x de R${parcela} ')
elif condicaoPagamento == 4:
    total = preco + preco*0.20
    parcela = total/totparcelas
    print(f'sera parcelada em {totparcelas}x de R${parcela:.2f} com juros e vai custar R${total} no final. ')
