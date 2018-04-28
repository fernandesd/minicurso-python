num = 'qualquer coisa'

while num != 'fim':
    num = input('Digite um número: ')
    if num == 'fim':
            break
    print ('O dobro de {} é {}.'.format(num, float(num) * 2))

print('Programa encerrado.')
