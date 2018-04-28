def somar(a, b):
    total = a + b
    return total

def somar_elementos(lista):
    total = 0
    for elem in lista:
        total += elem
    return total

print(somar(3, 6))

print(somar_elementos([1, 4, 7]))
