numeros = []
qtd = 0

n = int(input('Número negativo para: '))
while n >= 0:
    if n > 9 and n < 100:
        numeros.append(n)
    n = int(input('Número negativo para: '))

numeros.reverse()
print(numeros)