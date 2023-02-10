numerador = 2
denominador = 500
soma = 0.0

n = int(input('Num. termos '))
while n < 1 or n > 50:  # resolver o problema do denominador 0
    n = int(input('Inválido, Informe o Num. termos positivo '))

for i in range (1, n+1):
    print(f'{numerador}/{denominador}')
    soma = soma + numerador / denominador
    denominador = denominador - 10
    if numerador == 2:
        numerador = -5
    else:
        numerador = 2

    print('Resultado', soma)