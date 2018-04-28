#! usr/bin/python3

#msg = 'Sua idade é '
nome = input('Qual é o seu nome? ')
b = input('Digite ano em que você nasceu: ')
idade = 2018 - int(b)
#print(msg + str(idade))
print('Olá, {}! Sua idade é {}'.format(nome, idade) + ' anos')
