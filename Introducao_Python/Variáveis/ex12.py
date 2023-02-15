"""count = 1
soma = 0

while (count != 0): 
    n1 = int(input('Digite um número positivo: '))
    count = count + 1
    aux = count - 1

    if (n1 > 0):
        soma = soma + n1
        media = soma/ aux
        print(f'Média igual a: {media}')

    if (n1 <= 0):
        count = 0 """

    # Resolução do professor

soma = 0
qtd = 0
num = float(input(f'Informe o número {qtd + 1}:'))

while num >= 0:
    soma = soma + num
    qtd = qtd + 1
    num = float(input(f'Informe o número {qtd + 1}:'))


if qtd > 0:    
    soma = soma / qtd
    print('Resultado', soma)
else:
    print('Nenhum número válido digitado')