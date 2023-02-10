import math

# solução do professor

num = int(input("Digite um número:"))
raiz = int(math.sqrt(num))
d = 2

while d <= raiz and num % d != 0:
    d = d + 1

if d > raiz:
    print(num, 'é primo')
else: 
    print(num, 'não é primo', d, 'é um divisor')
