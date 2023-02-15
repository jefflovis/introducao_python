"""num1 = int(input("Digite o primeiro número do intervalo:"))
num2 = int(input("Digite o ultimo número do intervalo número:"))

soma = 0
for i in range (num1,num2 + 1):
    if i%2 != 0:
        soma = soma + i
print(soma)"""

# Resolução do professor
n1 = int(input("Digite o primeiro número do intervalo:"))
n2 = int(input("Digite o ultimo número do intervalo número:"))

soma = 0

if n2 < n1: 
    n1, n2 = n2, n1
if n1 % n2 == 0:
    aux = n1 + 1
else: 
    aux = n1
for i  in range (n1, n2 + 1, 2):
    soma = soma +1