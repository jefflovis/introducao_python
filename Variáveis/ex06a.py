numerador = 1
denominador = 1
soma = 0.0

n = int(input('Num. termos '))
while n < 1 :
    n = int(input('Inválido, Informe o Num. termos positivo '))

for i in range (1, n+1):
    print(f'{numerador}/{denominador}')
    soma = soma + numerador / denominador
    numerador = numerador + 2
    denominador = denominador + 1
    

    print('Resultado', soma)