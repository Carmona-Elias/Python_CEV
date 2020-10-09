frase = str(input('Digite uma frase: ')).strip().upper()

print(f'A letra "A" aparece {frase.count("A")} vez(es) na sua frase.')
print(f'A letra "A" aparece pela primeira vez na posicao {frase.find("A")}')
print(f'A letra "A" aparece pela ultima vez na posicao {frase.rfind("A")}')

