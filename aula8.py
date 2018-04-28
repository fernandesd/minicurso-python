chave = 'qualquer coisa'
dicio= []
while chave != 'fim':
    chave = input('Digite uma chave: ')
    if chave == 'fim':
            break
    valor = input(' Digite um valor')
    dicio[chave] = valor
print(dicio)
