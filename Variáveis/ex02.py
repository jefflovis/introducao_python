"""num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

resto = (num1 % num2)
if (resto == 0):
    print(num1)
else:
    print(resto**2)"""

# resolvendo problema do denominador 0

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

while num2 == 0:
    num2 = int(input("Número informado inválido, por favor informar um denominador válido:"))

resto = (num1 % num2)
if (resto == 0):
    print(num1)
else:
    print(resto**2)