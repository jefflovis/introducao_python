"""num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
num3 = float(input("Digite o terceiro número:"))

#verificador = list(num1,num2,num3)
print(min(num1,num2,num3))

# solução do professor

num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
num3 = float(input("Digite o terceiro número:"))

menor = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
if num1 < menor:
    menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print('Resultado', menor) """

# melhor opção
menor = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
for i in range (3):
    n1 = int(input('Num'))
    if n1 < menor:
        menor = n1
print('Resultado', menor)