num1 = int(input("Digite o primeiro número do intervalo:"))
num2 = int(input("Digite o ultimo número do intervalo número:"))

celsius = 0
for i in range (num1,num2 + 1):
    celsius = (i - 32)*5/9
    print(celsius)