num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

if num1 < num2:
    mdc = num1
else: 
    mdc = num2

while num1 % mdc != 0 or num2 % mdc != 0:
    mdc = mdc -1

print(mdc)

