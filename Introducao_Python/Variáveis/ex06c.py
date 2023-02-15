numerador1 = 37
numerador2 = 38
denominador = 1
soma = 0.0

n = int(input('Num. termos '))
while n < 1 :
    n = int(input('Inválido, Informe o Num. termos positivo '))

for i in range (1, n+1):
    print(f'{numerador1}*{numerador2}/{denominador}')
    soma = soma + numerador1*numerador2 / denominador
    numerador1 = numerador1 - 1
    numerador2 = numerador2 - 1
    denominador = denominador + 1
    

    print('Resultado', soma)