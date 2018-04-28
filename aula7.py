palavra = 'qualquer coisa'
lista = []
while palavra != 'fim':
    palavra = input('Digite uma palavra: ')
    if palavra == 'fim':
            break
    lista.append(palavra)
print(lista)        
