num = input('Digite um número: ')
floatnum = float(num)
...
if floatnum > 0:
    resultado = 'maior que zero'
else:
    if floatnum < 0:
        resultado = 'menor que zero'
    else:
        resultado = 'zero'
...

if floatnum > 0:
    resultado = 'maior que zero'
elif floatnum < 0:
    resultado = 'menor que zero'
else:
    resultado = ' igual a zero seu ótário!'

print('{} é {}'.format(floatnum, resultado))
